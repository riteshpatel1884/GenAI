from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()
model = init_chat_model("groq:meta-llama/llama-4-scout-17b-16e-instruct")

result = model.invoke("Hi")
print(result.content)





