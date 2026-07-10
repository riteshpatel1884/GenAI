from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

from langchain_core.documents import Document 

docs = [
    Document(
        page_content="Python is widely used in Artificial Intelligence.",
        metadata={"source": "AI_book"}
    ),
    Document(
        page_content="Pandas is used for data analysis in Python.",
        metadata={"source": "DataScience_book"}
    ),
    Document(
        page_content="Neural networks are used in deep learning.",
        metadata={"source": "DL_book"}
    ),
]
# currently we have 3 docs

# chromaDB also generates embedding but iske liye isko batana padta hai kiske through generate krna hai. 

#  Initialize your Embedding Model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")





vector_store = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory="chrome_DB"    # Storing in our local system 
)

result = vector_store.similarity_search("What is used for data analysis", k=2)
# k menas kitne result chahte ho.

for r in result: 
    print(r)

    # uv add sentence-transformers