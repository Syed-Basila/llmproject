from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

# Streamlit UI
st.title("Demo Chat Bot")
input_txt = st.text_input("Please enter your queries here..")

# Create the prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Your name is Basi's assistant."),
    ("user", "User query: {query}")
])

# Initialize the LLM model
llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_txt:
    st.write(chain.invoke({"query": input_txt}))
