import streamlit as st
from streamlit.logger import get_logger
logger = get_logger(__name__)

import os

#from dotenv import load_dotenv
#load_dotenv()
token = os.getenv('MY_HF_API_TOKEN')
token = os.getenv('home')
print(token)
st.title("Streamlit Israel")
st.text_area("Jira MDE")
repo_id = "microsoft/streamlit"
