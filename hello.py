from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash-exp",api_key = "AIzaSyB34Cgg2dUnIR1WwK2TYquLV0tpFvvZTOA" )

st.title("generative AI")
user_input = st.text_input ("wrinte some")

if user_input:
    response = llm.invoke(user_input)
    st.write(response.content)
 
# how to run this application?
# open terminal and write cammand  >  streamlit run filename whit .py