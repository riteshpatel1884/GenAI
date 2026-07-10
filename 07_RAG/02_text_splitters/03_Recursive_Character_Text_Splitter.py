# https://youtu.be/yodh-oEFnb4?si=1oKCFdQTH8j8b4TW&t=4985

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

data = PyPDFLoader("MedLeafViT_IEEE_Paper.pdf")

docs = data.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 10,
    chunk_overlap = 10,
)

chunks = splitter.split_documents(docs)  

print(len(chunks))   # 85

# To see the first chunk
print(chunks[0].page_content)