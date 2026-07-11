from langchain_community.document_loaders import ArxivLoader

docs = ArxivLoader(
    query="large language models",
    load_max_docs=2
).load()

for doc in docs:
    print(doc.metadata["Title"])