# from langchain_community.document_loaders import TextLoader

# loader = TextLoader("../01_development_plan.txt")
# docs = loader.load()

# # # To things will be shown 1. page_content 2. metadata
# # to access only page_content


# print(docs[0].page_content)  




from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate
load_dotenv() 

data =  TextLoader("../01_development_plan.txt")

docs = data.load()
templete = ChatPromptTemplate.from_messages(
    [("system", "you are an AI that extract only headings of the texts and number them from 1 as serial no"),
     ("human", "{data}")]
)
model = init_chat_model("google_genai:gemini-2.5-flash-lite")

prompt = templete.format_messages(data = docs[0].page_content)
response = model.invoke(prompt)
print(response.content)
