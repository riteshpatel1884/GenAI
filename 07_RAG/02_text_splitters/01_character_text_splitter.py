# from langchain_community.document_loaders import TextLoader
# from langchain_text_splitters import CharacterTextSplitter

# splitter = CharacterTextSplitter(
#     chunk_size = 10,
#     chunk_overlap = 1
# )

# data = TextLoader("../02_text_splitters/notes.txt")

# docs = data.load()

# chunks =  splitter.split_documents(docs)
# print((len(chunks)))  # 1: It means only one chunk is created.
# print((chunks))
# [Document(metadata={'source': '../02_text_splitters/notes.txt'}, page_content='Hi my name is Ritesh Patel\nWhat is your name')]

# /n means there is a new line
# So if we give one more extra space in notes.txt then 2 chunks will be created. 


# from langchain_community.document_loaders import TextLoader
# from langchain_text_splitters import CharacterTextSplitter

# splitter = CharacterTextSplitter(
#     chunk_size = 10,
#     chunk_overlap = 1
# )

# data = TextLoader("../02_text_splitters/notes1.txt")

# docs = data.load()

# chunks =  splitter.split_documents(docs)
# print((len(chunks)))   # 2
# # Hi my name is Ritesh Patel - chunk 1

# # What is your name - chunk 2
# print((chunks))





# To make the chunks as character based we use separator parameter.

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter


splitter = CharacterTextSplitter(
    separator="",
    chunk_size=10,
    chunk_overlap=1
)

data = TextLoader("../02_text_splitters/notes.txt")

docs = data.load()

chunks =  splitter.split_documents(docs)
print((len(chunks)))   # 6 - now abb 6-6 character ka 1 chunk hoga


#  Printing all chunks
for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i}:")
    print(repr(chunk.page_content))
    print("Length:", len(chunk.page_content))
    print("-" * 30)