import os
import streamlit as st
from langchain import OpenAI, LLMChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
 

st.title("Text Summarizer") 
def clear_text():
    st.session_state['text'] = ""
    
st.button("clear text input", on_click=clear_text)
#OPENAI_KEY=st.text_area("Copy & Paste your OPENAI_KEY", key="OPENAI_KEY")
#OPENAI_KEY=os.getenv('OPENAI_KEY')
#text_input = st.empty() 
#if st.button("Clear text input"): 
# text_input.text_area("Copy & Paste your text data",height=320, value='')

OPENAI_KEY = st.text_input("Copy & Paste your OPENAI_KEY", type='password') 
os.environ["OPENAI_API_KEY"] = OPENAI_KEY
text=st.text_area("Copy & Paste your text data",height=320, key="text")
#text = text_input.text_area("Copy & Paste your text data",height=320)

tokens = st.slider('Insert a number', max_value=1000)
st.write('Max number of tokens: ', tokens)

submit= st.button("Generate Summary")



#os.environ["OPENAI_API_KEY"] = st.secrets["key"]
#os.environ["OPENAI_API_KEY"] = OPENAI_KEY
llm_model = OpenAI(temperature=0, max_tokens=tokens)
text_splitter = CharacterTextSplitter()
except Exception as e: 
# Display the exception if the OPENAI_KEY is not valid 
st.exception(e) 
# Stop the execution of the app 
st.stop()
split_texts = text_splitter.split_text(text)
docs = [Document(page_content=t) for t in split_texts]
chain = load_summarize_chain(llm_model)


if submit:

    with st.spinner(text="Wait a moment..."):
            response = chain.run(docs)
            
    st.text_area("Output data",value=response, height=320)
    #text_output.text_area("Output data",value=response, height=320)
def clear_text():
    st.session_state['submit'] = ""
    
st.button("clear text output", on_click=clear_text)
#text_output = st.empty()
#if st.button("Clear text output"): 
# text_output.text_area("Output data",value='', height=320)

    
    
