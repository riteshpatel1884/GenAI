from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
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
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory="chrome_DB"    # Storing in our local system 
)

result = vector_store.similarity_search("What is used for data analysis", k=2)
# k menas kitne result chahte ho.

for r in result: 
    print(r)   #page_content='Pandas is used for data analysis in Python.' metadata={'source': 'DataScience_book'}


# When we run this file once then 3 documents ki embeddings create hokar db me store ho jayegi but when we will rerun this file then again 3 documents ki embedding create hokr db me uske niche add ho jayega.

retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)

retrieved_docs = retriever.invoke("Explain deep learning")

for doc in retrieved_docs:
    print(doc.page_content)    # Neural networks are used in deep learning.





# vector_store ke andar hi similarity_search algorithm hai and ye aur retriever same hi kaam kr rhe hai jo query ko dekh kr documents me se kisi ek similar ko nikal karkre de dega. 
# So main use of retriever is
# 1. Vector_store ko ham invoke nhi kar shakte it means ye runnable nhi hai so we cant include it in our chain.  Retrivers ko ham invoke kr shakte hai so there are runnables.

#2. Vector_store me sirf ek hi algo exist krti hai ie similarity search while in retriver they have miltiple techniques(10 almost)

# retriever = vector_store.as_retriever(
#     search_kwargs={"k": 2}
# )
#  Nothing mentioned so by defauly similarity search algo is applied