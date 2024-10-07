import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def getllama(Input_text,Numofwords,Blog):
    ##LLAMA MODEL
    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin', # Location of downloaded GGML model
                    model_type='llama', # Model type Llama
                    config={'max_new_tokens': 256,
                            'temperature': 0.01})
    ## prompt template
    Template= """ write a blog for {Blog} job profile for a topic {Input_text} within {Numofwords} words."""
    prompt=PromptTemplate(input_variables=["Blog","Input_text","Numofwords"],template=Template)
    
    ## Generate the response from LLama 2 model 
    response= llm(prompt.format(style=Blog,text=Input_text,num_words=Numofwords))
    print(response)
    return response

#title of the app

st.set_page_config(page_title="Generate Blogs", layout="centered", initial_sidebar_state="collapsed")  
st.header("Generate Blogs")
Input_text= st.text_input("Enter the blog Topic")

#creating the columns
col1, col2= st.columns([5,5])
with col1:
    Numofwords=st.text_input("Numbers of words")
with col1:
    Blog=st.selectbox("Writing the Blog for",("Reserches","Data scientist","Common people"),index=0)
submit= st.button("Generate")

if submit:
    st.write(getllama(Input_text,Numofwords,Blog))