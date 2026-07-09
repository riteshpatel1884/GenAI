 # For this we will use tit token to split

# uv add tiktoken
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import TokenTextSplitter

data = PyPDFLoader("MedLeafViT_IEEE_Paper.pdf")

docs = data.load()

splitter = TokenTextSplitter(
    chunk_size = 100,
    chunk_overlap = 10,
)

chunks = splitter.split_documents(docs)

print(len(chunks))