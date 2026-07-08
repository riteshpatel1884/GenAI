from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader("ritesh_ml.pdf")

docs = data.load()

print(docs)
print(len(docs))  # length of the docs is 1. It means it has 1 document in that list and har document me metadata as well as uska page_content hoga. 

# [] = list
# [()] = 1 document in the list with 1 metadata and 1 page_content

# length = no of pages in the pdf. 