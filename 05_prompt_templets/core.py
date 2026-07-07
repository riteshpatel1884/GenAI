# from dotenv import load_dotenv
# from langchain.chat_models import init_chat_model
# load_dotenv() 

# model = init_chat_model("groq:meta-llama/llama-4-scout-17b-16e-instruct")

# response = model.invoke("Can you give me the key insights of Bahubali movie")
# print(response.content)

# So kabhi bhi agar ek speficic task ke liye AI banana ho. As if i need to write same prompt multiple times we to avoiud writing it we use chat prompt templets.


from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

load_dotenv() 

model = init_chat_model("groq:meta-llama/llama-4-scout-17b-16e-instruct")

prompt = ChatPromptTemplate.from_messages([
    ("system",
"""
You are an expert Information Extraction Assistant.

Your task is to carefully analyze the given paragraph and extract all meaningful and useful information from it.

Instructions:

• Identify the main subject or title.
• Determine the content type (Movie, Book, Person, Company, Event, Product, Technology, Place, etc.).
• Extract all named entities such as:
  - People (director, actors, author, founder, composer, etc. whenever applicable)
  - Organizations
  - Locations
  - Countries
  - Languages
• Extract important attributes such as:
  - Genre or category
  - Release year or date
  - Ratings or scores
  - Awards or achievements
  - Important numbers
  - Important dates
• Identify the major topics discussed.
• Extract the most important keywords.
• List all important facts mentioned in the paragraph.
• Identify the key events or actions described.
• Detect the overall sentiment (Positive, Neutral, or Negative).
• Generate:
  1. A one-line summary.
  2. A short summary (2–4 sentences).
  3. 4–6 concise bullet points covering the most important information.

Additional Instructions:

- Extract only information explicitly present in the paragraph.
- Do not invent or assume facts.
- Ignore filler sentences and focus on meaningful information.
- If some information is unavailable, simply omit it instead of guessing.
- Keep the output well-organized with clear section headings.
- Be concise while preserving all important details.
"""),
("human",
"""
Analyze the following paragraph and extract all useful information.

Paragraph:

{paragraph}
""")
]
)

para  = input("Give a paragraph: ")
# now put this para inside {paragraph} in human role

final_prompt = prompt.invoke(
    {"paragraph": para}
)
response = model.invoke(final_prompt)
print(response.content)