"""
Flask wrapper around your existing RAG script.
This just takes your second file (the retrieval + Groq chat loop) and exposes
it as a POST /chat endpoint instead of a `while True: input()` loop, so the
HTML/CSS/JS UI can talk to it.

Run with:
    pip install flask flask-cors
    python app.py

Then open http://127.0.0.1:5000 in your browser.

NOTE: run your ingestion script (the PyPDFLoader + Chroma.from_documents one)
at least once BEFORE starting this, so that the "chroma_DB" folder exists.
This file only *reads* from that folder — it never re-creates embeddings.
"""

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv

from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

app = Flask(__name__)
CORS(app)

# ---- Load everything ONCE at startup (not per-request) ----

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="chroma_DB",
    embedding_function=embedding_model
)

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "fetch_k": 10,
        "lambda_mult": 0.5
    }
)

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

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

print("RAG system loaded. Waiting for requests...")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True) or {}
    query = (data.get("query") or "").strip()

    if not query:
        return jsonify({"error": "Empty query"}), 400

    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    final_prompt = prompt.invoke({
        "context": context,
        "question": query
    })

    response = llm.invoke(final_prompt)

    # collect page numbers of the chunks used, for the "footnote" markers in the UI
    pages = []
    for doc in docs:
        page = doc.metadata.get("page")
        if page is not None and page not in pages:
            pages.append(page)

    return jsonify({
        "answer": response.content,
        "pages": pages
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)