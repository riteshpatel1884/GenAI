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

print(len(chunks))   # 85

# To see the first chunk
print(chunks[0].page_content)
# Hierarchical Adaptive Token Refinement for Offline, Edge-Deployable 
# Identification of Indian Medicinal Plants 
# Ayush Bhushan 
# Department of Computer Science and Engineering 
# KIET Group of Institutions, Ghaziabad, India 
# Abstract 
# Field identification of medicinal plants remains largely dependent on internet-connected tools such as PlantNet and iNaturalist, 
# neither of which is tuned to the roughly 8,000 species used