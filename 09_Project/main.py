
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()


templete = ChatPromptTemplate.from_messages(
    [
        ("system", "you are an AI that summarises the text"),
        ("human", "{data}")
    ]
)
model = init_chat_model("groq:meta-llama/llama-4-scout-17b-16e-instruct")


print(result.content)