from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timedelta
from typing import Union
from fastapi import Depends, FastAPI, HTTPException, status
from user_auth import AuthHandler
from database_util import database_methods


app = FastAPI()
auth_handler = AuthHandler()
db_method=database_methods()


##Class for user data to login and register
class UserData(BaseModel):
    username:str
    password: str
    restaurant_name: Optional[str]
    user_tier: Optional[str] = 'free'

class Pinecone_Query(BaseModel):
    query:str
    restaurant_id:str
    
class GPT_Query(BaseModel):
    query:str
    prompt:str
    
  
@app.get('/healthz',status_code=status.HTTP_200_OK)
def healthz():
    return {"Server": "Running"}  
    
@app.post('/register', status_code=status.HTTP_201_CREATED)
async def register(auth_details: UserData):
    user_fetch_status=db_method.fetch_user(auth_details.username)
    if user_fetch_status != 'no_user_found' or user_fetch_status == 'Exception': 
        #Can add logs
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Username is taken')
    hashed_password = auth_handler.get_password_hash(auth_details.password)
    user_status=db_method.add_user(auth_details.username,hashed_password,auth_details.restaurant_name,auth_details.user_tier)
    if user_status=='failed_insert':
        #Can add logs
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Error')
    
@app.post('/forgot_password',status_code=status.HTTP_201_CREATED)
async def reset_password(auth_details: UserData):
    fetch_user_status=db_method.fetch_user(auth_details.username)
    if isinstance(fetch_user_status, str) and fetch_user_status == 'no_user_found':
        #Can add logs
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid username and/or password')
    hashed_password = auth_handler.get_password_hash(auth_details.password)
    user_status=db_method.update_password(auth_details.username,hashed_password)
    if user_status=='update_failed':
        #Can add logs
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Error')
    #Can add logs

@app.post('/login',status_code=status.HTTP_200_OK)
async def login(auth_details: UserData):
    fetch_user_status=db_method.fetch_user(auth_details.username)
    if isinstance(fetch_user_status, str) and fetch_user_status == 'no_user_found':
        #Can add logs
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid username and/or password')
    print(fetch_user_status[2])
    if not auth_handler.verify_password(auth_details.password, fetch_user_status[2]):
        #Can add logs
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid username and/or password')
    token = auth_handler.encode_token(fetch_user_status[1])
    #Can add logs
    return { 'token': token }

@app.get('/get_restaurant_id',status_code=status.HTTP_200_OK)
def get_restaurant_id(username=Depends(auth_handler.auth_wrapper)):
    return db_method.fetch_user(username)[8]

@app.get('/query_pinecone',status_code=status.HTTP_200_OK)
def query_pinecone(pinecone_query:Pinecone_Query,username=Depends(auth_handler.auth_wrapper)):
    return db_method.query_pinecone(pinecone_query.query,pinecone_query.restaurant_id)

@app.get('/query_gpt',status_code=status.HTTP_200_OK)
def query_gpt(gpt_query:GPT_Query,username=Depends(auth_handler.auth_wrapper)):
    return db_method.chat_gpt(gpt_query.query,gpt_query.prompt)