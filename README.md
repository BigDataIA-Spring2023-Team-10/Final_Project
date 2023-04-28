# ReviewReformer


![0_s0_g_f0OUuc1blVC](https://user-images.githubusercontent.com/114544202/235055460-06eb1bc9-4a2d-4d49-96e5-e0caeae8f6fb.jpg)


[![PyPI](https://img.shields.io/pypi/pyversions/locust.svg)](https://pypi.org/project/locust/)
![Tests](https://github.com/kshitijzutshi/DAMG7245-Final-Project/actions/workflows/testing_workflow.yml/badge.svg)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
![](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

# Code Labs Documentation

[Access the codelabs document here](https://codelabs-preview.appspot.com/?file_id=1527BIJDrvCVDCDX2OYgTlA1reW1iXBZcRcyp0hcj4Dw#5) 🚀





# Application Link

[Access the Application link here]() 🚀


[FastApi Documentation](http://bigdata7245-finalproject.ue.r.appspot.com/docs) 🚀


# Vidoe Link

[Video Link](https://drive.google.com/file/d/1StfPrUxc7K9zh2GHFB28IJRHHt5zxwGI/view?usp=sharing) 🚀

# Overview 📝

The main problem faced by restaurent owner is to get a feeback from the customer using his services and  provide restaurant owners with insights into their business by analyzing the reviews they receive on social sites or any other Internet platform. Yelp is a popular platform where customers can leave reviews and ratings for businesses, including restaurants. However, analyzing these reviews manually can be time-consuming and may not provide the insights that restaurant owners need to improve their business.

# Goals 🎯
The goal of this project is to provide restaurant owners with a dashboard that displays the sentiment and topics of their Yelp reviews, as well as recommendations on how to improve their business based on the analysis. This can help restaurant owners make data-driven decisions that can lead to increased customer satisfaction and business success. We are trying to use data engineering techniques to automatically collect, preprocess, and analyze Yelp reviews for restaurants
By visualizing this data, we tend to provide restaurant owners with actionable insights that can help them improve their business.


# Dataset Source 🔦

The source of data for this project we used is Yelp's API (Application Programming Interface). The Yelp API provides access to a wealth of data, including business information, reviews, ratings, photos, and more. With the Yelp API, we have access to  collect data for specific restaurants based on their Yelp business ID, location, or other criteria. A brief preview of data is as below


![image](https://user-images.githubusercontent.com/114544202/235063605-c99417bb-9205-4b04-bf83-c22a838af154.png)


# Process Outline

1. Data gathering from he yelp API and dataging in Database
2. Data Preprocessing   
3. Understanding the Dataset - Exploratory Data Analysis(EDA)
4. Building a pipeline system using Airflow to scrape data on regular basis and also using various tools/softwares(AWS Cloudwatch , Streamlit, GCP)
5. Using OpenAi Api to suggest the steps of action that can be used to improve the business based on the reviews provided
6. Build a web application using streamlit for showcasing the results.


# Project overall Architecture

Project Architecture Diagram and technologies used




![84106459-fecb-454b-b581-00d55bc65bc5](https://user-images.githubusercontent.com/114544202/235215628-5d4b8169-da9f-4379-aec2-bdcf90d97a3f.png)


Project Requirements and Technology dependencies

### Requirements and dependencies

```

fastapi==0.95.1
frozenlist==1.3.3
gitdb==4.0.10
GitPython==3.1.31
🐍 Python ➡ 3.9.7
altair==4.1.0
📊 matplotlib==3.5.0
🔢 numpy==1.19.5
google-api-core==2.11.0
google-auth==2.17.3
google-auth-oauthlib==1.0.0
google-cloud==0.34.0
google-cloud-core==2.3.2
google-cloud-storage==2.8.0
google-crc32c==1.5.0
google-resumable-media==2.5.0
googleapis-common-protos==1.59.0
streamlit==1.21.0
toml==0.10.2
watchfiles==0.19.0
uvicorn==0.21.1
uvloop==0.17.0
validators==0.20.0
watchfiles==0.19.0
wcwidth==0.2.6
websockets==11.0.2
yarl==1.9.1
zipp==3.15.0
```



# Milestones

| Time Frame  | Tasks                                                               |
|:-----------:|:-------------------------------------------------------------------:|
| Day 1 - 5   | Data Gathering from yelp API and Data cleaninng and processing, EDA                               |
| Day 5 - 10  | Setup of Data pipeline, Streamlit Integration, and Cloud Deployment |
| Day 10 - 15 | System integration, App enhancements, Testing and documentation     |



# Project Folder Structure


```
📦 
├─ .DS_Store
├─ .gitignore
├─ Airflow  
│  └─ dags.py <-- Airflow DAGs for yelp Data Extraction
├─ Data  <-- Yelp reviews data extracted csv
│  ├─ rev-id-_ab50qdWOk0DdB6XOrBitw.csv
│  ├─ review-id-VQcCL9PiNL_wkGf-uF3fjg.csv
│  ├─ review-id-_ab50qdWOk0DdB6XOrBitw.csv
│  ├─ review-id-ac1AeYqs8Z4_e2X5M3if2A.csv
│  ├─ review-id-iSRTaT9WngzB8JJ2YKJUig.csv
│  └─ review-id-oBNrLz4EDhiscSlbOl8uAw.csv
├─ Dataset EDA  <-- EDA for extracted Data
│  ├─ yelp_review_Sentiment_WordCloud.ipynb
│  └─ yelp_review_Sentiment_analysis.ipynb
├─ FastApi  <--  Backend APIs
│  ├─ Dockerfile
│  ├─ app.yaml
│  ├─ database_util.py
│  ├─ logging_util.py
│  ├─ main.py
│  ├─ requirements.txt
│  └─ user_auth.py
├─ README.md
├─ Streamlit <-- Streamlit Frontend business Logic
│  ├─ Pages
│  │  ├─ 01_Login.py
│  │  ├─ 02_Register.py
│  │  ├─ 03_Forgot_Password.py
│  │  ├─ Analyse Reviews.py
│  │  └─ Upload Reviews.py
│  └─ home.py
└─ requirements.txt  <-- requirements.txt
```

# Steps to be followed for Accessing the codebase:


```
1. Clone this repo locally `git clone <repo-url>`

2. Setup the local python enviornment.

3. Install all the dependencies from the requirements.txt file
`pip install -r requirements.txt`

4. Install all local dependencies 
`pip install -e .`

5. Create `.env` file.

The Following Details in env file needed to be updated to Configure to streamlit and GCP


host = "" <-- DB HostName 
user = "" <-- DB Username
password = "" <-- DB password
db = "" <-- DB password
bucket_name = "" <-- Aws Bucket Name
open_api_key="" <-- Open API Key
Embedding_Model = "text-embedding-ada-002"
pinecone_api_key ="" <-- pinecone API key
pinecone_environment="us-central1-gcp" <--pinecone region


[gcp_service_account]
type= ""
project_id= ""
private_key_id= ""
private_key= ""
client_email=""
client_id= ""
auth_uri= ""
token_uri= ""
auth_provider_x509_cert_url= ""
client_x509_cert_url= ""

This Credentials can be obtained after successfully creating GCP account and post creation of project

In order to obtain pinecone credentials one can use below steps

Sign up for a Pinecone account: If you haven't already, go to the Pinecone website and sign up for a free account.

Create an API key: Once you have logged into your Pinecone account, go to the "API Keys" section of the dashboard and click "Create API Key".

Name your API key: Give your API key a name that is easy to remember and helps you identify its purpose.

Copy your API key: Once you have created your API key, copy it to your clipboard or save it in a secure location.

```














### Team Member

| NUID | Team Member       |
|:-----:|---------------|
| 002766036       | Anuj Kumar |
| 002794258      |  Hitesh  Pant            |
| 002773080      |  Kunal Bhoyar              |
| 002772221      |  Snehashis Lenka              |


WE ATTEST THAT WE HAVEN'T USED ANY OTHER STUDENT'S WORK IN OUR ASSIGNMENT AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK.














