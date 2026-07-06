# from dotenv import load_dotenv
# from langchain.chat_models import init_chat_model
# load_dotenv() 

# model = init_chat_model("groq:meta-llama/llama-4-scout-17b-16e-instruct")

# while True:  # Now user and AI will talk infinite time
#     prompt = input("You: ")
#     response = model.invoke(prompt)
#     print("AI:", response.content)


# The above code will work fine but AI will not remember ur previous asked question or resposne. So we need to save the history in a list


# from dotenv import load_dotenv
# from langchain.chat_models import init_chat_model
# load_dotenv() 

# model = init_chat_model("groq:meta-llama/llama-4-scout-17b-16e-instruct")


# history = []
# while True:
#     prompt = input("You: ")
#     history.append(prompt)
#     response = model.invoke(history)
#     history.append(response.content)
#     print("AI:", response.content)


#The above code is good but only for testing and its a short time memory.
# Problems With Your Current Short-Term Memory**

# No role separation (no system / user / assistant distinction)
# Just raw strings → weak conversation structure
# Memory keeps growing infinitely
# Will hit token limit
# API cost increases over time
# Slower response as history grows
# No trimming mechanism
# No summarization of old chats
# Not production scalable

#Langchain provideed a messages feature to store the history