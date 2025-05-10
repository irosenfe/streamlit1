import streamlit as st
from streamlit.logger import get_logger
logger = get_logger(__name__)

import os

#from dotenv import load_dotenv
#load_dotenv()
#token = os.getenv('MY_HF_API_TOKEN')
#token = os.getenv('home')
st.title("Streamlit Israel")
st.text_area("Jira Wiki MDE")
# repo_id = "microsoft/streamlit"


import streamlit as st
from streamlit.logger import get_logger
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace

from dotenv import load_dotenv
logger = get_logger(__name__)


import os


if os.getenv('USER', "None") == 'appuser': # streamlit
    ht_token = st.secrets['HF_TOKEN']
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = ht_token
else:
    # ALSO ADD HERE YOUR PROXY VARS
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.environ["MY_HF_API_TOKEN"]
# load_dotenv()

st.title("my gen AI app")
repo_id = "microsoft/Phi-3-mini-4k-instruct"
temp = 1
print(repo_id, temp)
logger.info(f"{temp=}")

with st.form("sample_app"):
    txt = st.text_area("Enter text:", "which price will INTEL be next year?")
    sub = st.form_submit_button("submit")
    if sub:
        print(sub)
        llm = HuggingFaceEndpoint(
                repo_id=repo_id,  #3.8B model
                task="text-generation",
                temperature=temp
                )
        print(llm)
        chat = ChatHuggingFace(llm=llm, verbose=True)
        print(chat)
        logger.info("invoking")
        ans = chat.invoke(txt)
        st.info(ans.content)
        logger.info("Done")

