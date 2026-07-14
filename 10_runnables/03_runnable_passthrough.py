# from dotenv import load_dotenv
# load_dotenv()

# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import (
#     RunnableParallel,
#     RunnablePassthrough,
# )

# model = ChatGroq(
#     model="llama-3.3-70b-versatile"
# )
# parser = StrOutputParser()

# code_prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a code generator"),
#     ("human", "{topic}")
# ])

# explain_prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful assistant, who explains code in simple words"),
#     ("human", "Explain the following code in simple words")
# ])

# seq = code_prompt | model | parser  | explain_prompt | model | parser

# result = seq.invoke({"topic": "Write a code for palindrome no in python"})

# print(result)

# If we want to extract code after code_prompt | model | parser then we will use runnable Passthrough

from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableParallel,
    RunnablePassthrough,
)

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)
parser = StrOutputParser()

code_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a code generator"),
    ("human", "{topic}")
])

explain_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant, who explains code in simple words"),
     ("human", "Explain the following code:\n\n{code}")
])

seq = code_prompt | model | parser  # ish sequence variable ke andar code hai. Now we need this code and as well as we need to pass this code further in one more parallel sequence

seq2 = RunnableParallel({
    "code": RunnablePassthrough(),
    "explanation": explain_prompt | model | parser
})

chain = seq | seq2

#  https://youtu.be/CUDT5E6jz84?si=yva8Op9_vVTiC1Im&t=4225
result = chain.invoke({"topic": "Write a code for palindrome no in python"})

print(result['code'])
print(result['explanation'])
