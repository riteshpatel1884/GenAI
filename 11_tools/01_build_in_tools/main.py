from dotenv import load_dotenv
load_dotenv()

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# tools are also runnables so we can invoke them

search_tool = TavilySearchResults(max_result= 5)

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

prompt = ChatPromptTemplate.from_template(
    """
   You are a helpful assistent. summarise the following news in a clear bullet points.
   {news}
"""
)

chain = prompt | llm | StrOutputParser()

result = search_tool.run("Latest AI news of 2026")

new_result = chain.invoke({"news": result})

print(new_result)