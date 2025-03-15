from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import streamlit as st
import os

os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']

### Streamlit ###
import streamlit as st

st.header(" Math Exercise ")

st.subheader(" Generate Math Exercise for practice 🤖")

# topic = st.text_input("Topic for tweet :")

# number = st.number_input("Enter a Number of tweets 1 to 10 :", min_value = 1, max_value = 10, value = 1, step = 1)

"""
if st.button("Generate"):
    tweets = tweet_chain.invoke({"number" : number, "topic" : topic})
    st.write(tweets.content)

"""
