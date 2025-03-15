from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import streamlit as st
import os

os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']

# Initializing Google Gemini AI Model 
gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")

response = gemini_model.invoke("Give me one math percentage problem for 6th gread indian student in Multipe Choice Option, also provide correct answer")
#print(response.content)

### Streamlit ###

st.header(" Math Exercise ")
st.subheader(" Generate Math Exercise for practice 🤖 ")


if st.button("Generate"):
    #MathProblem = gemini_model.invoke({"number" : number, "topic" : topic})
    st.write(response.content)
