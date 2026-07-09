# from langchain_community.document_loaders import PyPDFLoader

# data = PyPDFLoader("MedLeafViT_IEEE_Paper.pdf")

# docs = data.load()

# print(docs)
# print(len(docs))  # length of the docs is 8. It means it has 8 document in that list and har document me metadata as well as uska page_content hoga. 

# [] = list
# [(),(),(),(),(),(),(),()] = 8 document in the list with 1 metadata and 1 page_content in each document

# length = no of pages in the pdf. 




from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
load_dotenv() 

data =  PyPDFLoader("MedLeafViT_IEEE_Paper.pdf")

docs = data.load()
templete = ChatPromptTemplate.from_messages(
    [("system", "you are an AI that extract only headings of the texts and number them from 1 as serial no"),
     ("human", "{data}")]
)
model = init_chat_model("google_genai:gemini-2.5-flash-lite")

# There can be a problem that the model will not able to read all the 8 pages of pdf so we need to give small data like page 1
# prompt = templete.format_messages(data = docs[0].page_content)

prompt = templete.format_messages(data = docs)
response = model.invoke(prompt)
print(response.content)
