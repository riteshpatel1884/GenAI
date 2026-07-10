from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
data = PyPDFLoader("/Deep+Learning+Ian+Goodfellow.pdf")
docs = data.load()

templete = ChatPromptTemplate.from_messages(
    [
        ("system", "you are an AI that summarises the text"),
        ("human", "{data}")
    ]
)
model = init_chat_model("groq:meta-llama/llama-4-scout-17b-16e-instruct")

prompt = templete.format_messages(data = docs)
result = model.invoke(prompt)
print(result.content)


# It means we cant feed these much amount of pages at once. So first we need to do chunking then store each chunks in vector database 

# To store the chunks in vectorDB. First generate embeddin of each chunks then store their embedding in the vector db. Refer 08_vector_DB folder

# jo user


from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter


load_dotenv()
data = PyPDFLoader("/Deep+Learning+Ian+Goodfellow.pdf")
docs = data.load()


# creating chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(docs)
templete = ChatPromptTemplate.from_messages(
    [
        ("system", "you are an AI that summarises the text"),
        ("human", "{data}")
    ]
)
model = init_chat_model("groq:meta-llama/llama-4-scout-17b-16e-instruct")

prompt = templete.format_messages(data = docs)
result = model.invoke(prompt)
print(result.content)