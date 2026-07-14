from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain.tools import tool
from rich import print


# When we have multiple tools then we need to inform the llm that we have multiple tools so we need to create a tool and then bind it(tool binding) then call it(tool calling) then execture it based on tool selected 

# Creating a tool
@tool 
def get_text_length(text: str) ->int:
    """ Return the number of character in a given text """
    return (len(text))


llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

# tool binding. provide all the tools in this list
llm_with_tool = llm.bind_tools([get_text_length])


result1 = llm.invoke("hello")
result2 = llm_with_tool.invoke("hello")

print(result1)

# as we r using from rich import print so result will be printed like this
# AIMessage(
#     content='Hello! How can I assist you today?',
#     additional_kwargs={},
#     response_metadata={
#         'token_usage': {
#             'completion_tokens': 10,
#             'prompt_tokens': 37,
#             'total_tokens': 47,
#             'completion_time': 0.020619524,
#             'completion_tokens_details': None,
#             'prompt_time': 0.001948555,
#             'prompt_tokens_details': None,
#             'queue_time': 0.16183372,
#             'total_time': 0.022568079
#         },
#         'model_name': 'llama-3.3-70b-versatile',
#         'system_fingerprint': 'fp_3272ea2d91',
#         'service_tier': 'on_demand',
#         'finish_reason': 'stop',
#         'logprobs': None,
#         'model_provider': 'groq'
#     },
#     id='lc_run--019f6064-7ee4-7182-8514-2006cde7522a-0',
#     tool_calls=[],
#     invalid_tool_calls=[],
#     usage_metadata={'input_tokens': 37, 'output_tokens': 10, 'total_tokens': 47}
# )

print()
print()
print(result2)
# AIMessage(
#     content="I'm here to help. Is there something I can help you with, or would you like to chat?",
#     additional_kwargs={},
#     response_metadata={
#         'token_usage': {
#             'completion_tokens': 23,
#             'prompt_tokens': 221,
#             'total_tokens': 244,
#             'completion_time': 0.082569991,
#             'completion_tokens_details': None,
#             'prompt_time': 0.010839655,
#             'prompt_tokens_details': None,
#             'queue_time': 0.161341241,
#             'total_time': 0.093409646
#         },
#         'model_name': 'llama-3.3-70b-versatile',
#         'system_fingerprint': 'fp_45180df409',
#         'service_tier': 'on_demand',
#         'finish_reason': 'stop',
#         'logprobs': None,
#         'model_provider': 'groq'
#     },
#     id='lc_run--019f6068-48f8-7130-b690-c424964cbac5-0',
#     tool_calls=[],
#     invalid_tool_calls=[],
#     usage_metadata={'input_tokens': 221, 'output_tokens': 23, 'total_tokens': 244}
# )


# There is a difference of token. Bina tool ke llm result me(result1) sirf 37 tokens hai jabki dusre AI message me jisme hamne 1 tool ko bind karke rakha hai usme we have 221 input tokens becoz jab ham kisi tool ko llm ke saath bind krte hai then jo uska metadata and docs strong hai wo sab kuch iske pass chala jata hai. Although dono ka content ka response almost same hai