from typing import List
from pathlib import Path
#from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.chat_models.openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
from langchain.indexes import SQLRecordManager, index
from langchain.schema import Document
from langchain.schema.runnable import Runnable, RunnablePassthrough, RunnableConfig
from langchain.callbacks.base import BaseCallbackHandler

import chainlit as cl

from dotenv import load_dotenv
load_dotenv()

chunk_size = 1024
chunk_overlap = 50

embeddings_model = OpenAIEmbeddings()

PDF_STORAGE_PATH = "./pdfs"


print('all good')