# from dotenv import load_dotenv
# load_dotenv()

# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# # 1. prompt templete
# prompt = ChatPromptTemplate.from_template(
#     "Explain {topic} in simple word"
# )

# # 2. model
# model = ChatGroq(
#     model="llama-3.3-70b-versatile"
# )

# # 3. structured output parser
# parser = StrOutputParser()


# # step ny step manual flow
# formatted_prompt = prompt.format_messages(topic="Machine Learning")

# #call model manually
# response = model.invoke(formatted_prompt)

# # parse the output manually
# final_output = parser.parse(response.content)

# print(final_output)




from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# runnable
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple word"
)

# runnable
model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

# runnable
parser = StrOutputParser()


# prompt la response model me jayega. Model ka parser me and parser ka chain me jayega.
chain = prompt | model | parser 

result = chain.invoke("DEEP LEARNING")

print(result)