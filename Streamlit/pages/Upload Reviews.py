import streamlit as st
import pandas as pd
from google.cloud import storage
from google.oauth2 import service_account
import tempfile
import os
import requests

# Define the API endpoint URL
URL = 'http://bigdata7245-finalproject.ue.r.appspot.com'

if "login_success" not in st.session_state:
    st.session_state['login_success'] = False

def uploadReviewsPage():
    with st.form("Upload_form", clear_on_submit=True):

        uploaded_file=st.file_uploader("Choose an review file",type='csv',accept_multiple_files=False)
        submitted = st.form_submit_button("Upload File")
        
        with st.spinner('Wait for it...'):
            if uploaded_file is not None:
                # Create API client.
                credentials = service_account.Credentials.from_service_account_info(st.secrets["gcp_service_account"])
                storage_client = storage.Client(credentials=credentials)
                
                bucket = storage_client.get_bucket(st.secrets["bucket_name"])
                
                # Save uploaded file to a temporary file
                with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                    tmp_file.write(uploaded_file.read())
                    tmp_file.flush()
                    os.fsync(tmp_file.fileno())
                    
                    ##Request fastapi for the resturant_id
                    restaurant_id=""
                    headers = {"Authorization": "Bearer " + st.session_state['login_token']}
                    res = requests.get(URL + '/get_restaurant_id', headers=headers)
                    if res.status_code == 200:
                         restaurant_id = res.json()
                    # Upload the temporary file to Cloud Storage
                    blob = bucket.blob(f"raw_reviews/{str(uploaded_file.name).split('.')[0]}-id-{restaurant_id}.csv")
                    blob.upload_from_filename(tmp_file.name)
                    
                # Delete the temporary file
                os.unlink(tmp_file.name)
                st.success('Recording uploaded successfully!')
                st.session_state.upload_success = True
            elif submitted and uploaded_file is None:
                st.warning('Select a file to upload')


if __name__ == "__main__":
    if st.session_state['login_success']:
        uploadReviewsPage()
    else:
        st.write("Login to access this page!")