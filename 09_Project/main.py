from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
) # creating embedding models. use hugging face embedding model for free

vectorstore = Chroma(
    persist_directory= "chroma_DB",
    embedding_function=embedding_model
)

retriever = vectorstore.as_retriever(
    search_type = "mmr",
    search_kwargs = {
        "k" : 4,
        "fetch_k":10,
        "lambda_mult" :0.5
    }
)
#  "fetch_k":10, means initially hame 10 chaiye fir usme mmr lagayange and after that we will get 4.
# lambda_mult: value is between 0 and 1. 0 means bahut hi jada diverse result aayega and 1 means bahut kam diverse result aayega.



llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

#prompt template 
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a helpful AI assistant.

Use ONLY the provided context to answer the question.

If the answer is not present in the context,
say: "I could not find the answer in the document."
"""
        ),
        (
            "human",
            """Context:
{context}

Question:
{question}
"""
        )
    ]
)

print("Rag system created ")

print("press 0 to exit ")

while True:
    query = input("You : ")
    if query == "0":
        break 
    
    docs = retriever.invoke(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )
    
    final_prompt = prompt.invoke({
        "context" :context,
        "question": query
    })
    
    response = llm.invoke(final_prompt)

    print(f"\n AI: {response.content}")

# query: can tell me about word2vec framework

# https://youtu.be/yodh-oEFnb4?si=B0hHdPA2Yca9HJVV&t=12302