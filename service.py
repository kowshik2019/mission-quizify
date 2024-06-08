import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
import os
import tempfile
import uuid
from tasks.task_3.task_3 import DocumentProcessor

