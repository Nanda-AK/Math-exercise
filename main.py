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

###########################################################################
Math_template ="""
Can you generate Math problem for grade 6th student on {Math_Topic} with multiple choise answer and also provide answer with explanation
"""

Math_prompt = PromptTemplate(template = Math_template, input_variables =['Math_Topic'])

#Create LLM Chain using theprompt template and Model
Math_chain = Math_prompt | gemini_model




### Streamlit ###

st.header(" Math Exercise ")
st.subheader(" Generate Math Exercise for practice 🤖 ")

Math_topic = st.selectbox("Choose a topic for the tweet:", ["Percentage", "LCM", "HCF"])
st.write("You selected:", Math_topic)

if st.button("Generate"):
    Math_Q = Math_chain.invoke({"Math_topic" : Math_topic})
    st.write(Math_Q.content)

