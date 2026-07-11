# load the pdf
# split in chunks
# create the embeddings
# store in this.
# Now we will write code of database in this file as when we will run our main file they multiple embeddings of same database will be created so to avoid this we write our db realted code in db file

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chat_models import init_chat_model
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

data = PyPDFLoader("/Deep+Learning+Ian+Goodfellow.pdf")
docs = data.load()

# creating chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap=200
)
#  now we need to create embeddings of these chunks and store it in the chromaDB
 
chunks = splitter.split_documents(docs)

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="chroma_DB"
)

