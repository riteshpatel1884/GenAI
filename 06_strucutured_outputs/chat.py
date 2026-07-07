
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv() 

model = init_chat_model("groq:meta-llama/llama-4-scout-17b-16e-instruct")


# creating schema
class Movie(BaseModel):
    title:str
    release_year:Optional[int]
    genre:List[str]
    director:str
    cast:List[str]
    ratings:Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)  # parser will check if all information is correct in Movie are not 
prompt = ChatPromptTemplate.from_messages([
    ("system",
"""
Extract movie information from the paragraph {format_instrucxtions}
"""),
("human",
"""
{paragraph}
""")
]
)

para  = input("Give a paragraph: ")
# now put this para inside {paragraph} in human role

final_prompt = prompt.invoke(
    {"paragraph": para,
     "format_instrucxtions":parser.get_format_instructions()}
)
response = model.invoke(final_prompt)
print(response.content)