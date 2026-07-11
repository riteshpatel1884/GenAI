from langchain_community.document_loaders import ArxivLoader

loader = ArxivLoader(
    query="Large Language Models",
    load_max_docs=2
)

docs = loader.load()

print(len(docs))
print(docs[0].metadata)