# To extract information of any web page. 
# uv add beautifulsoup4 lxml
from langchain_community.document_loaders import WebBaseLoader

url = "https://www.merriam-webster.com/dictionary/apply"
data =  WebBaseLoader(url)

docs = data.load() 
# print(len(docs))   # len = 1 since we have loaded only one page. 
# print(docs)  # [Document(metadata={'source': 'https://leaderlab.in', 'title': 'LeaderLab', 'language': 'en'}, page_content='LeaderLab')]

print(docs[0].page_content)




