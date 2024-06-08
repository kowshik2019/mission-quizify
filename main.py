import streamlit as st
from service import file_uploader
from tasks.task_3.task_3 import DocumentProcessor

####### SCREEN 1
st.title("Screen 1")

with st.form("Load Data"):
    # PDF file loader for Screen 1
    
    # TASK 2: VectorStore Information
    if load_documents(): # Load if there are existing db/ and files
        read_from_chroma()      # Instantiate and Read from Chroma  
        ask_for_more_documents  # Ask if there are more documents to ingest
    else:
        mount_google_embedder() # Mount embeddings function for Chroma TASK 1
        ingest_documents()      # Ingest if there are no existing db/ and files TASK 2
        embed_to_chroma()       # Embed and Store into VectorStore, return Vector Store
    
    st.form_submit_button("Submit")

####### SCREEN 2
# Task 3: 

st.title("Screen 2")
processor = DocumentProcessor()
processor.ingest_documents()
# TASK 3: DocumentProcessor Information
# Utilize the Streamlit file uploader widget to allow users to upload PDF files.
# For each uploaded PDF file:
# Generate a unique identifier and append it to the original file name before saving it temporarily.
# Use Langchain's PyPDFLoader on the path of the temporary file to extract pages.
# Clean up by deleting the temporary file after processing.
# Keep track of the total number of pages extracted from all uploaded documents.
