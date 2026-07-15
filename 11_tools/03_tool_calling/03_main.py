from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain.tools import tool
from rich import print
from langchain_core.messages import HumanMessage


# Creating a tool
@tool 
def get_text_length(text: str) ->int:
    """ Return the number of character in a given text """
    return (len(text))


tools = {
    "get_text_length": get_text_length
}


llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

# tool binding. 
llm_with_tool = llm.bind_tools([get_text_length])

# history
messages = []

prompt = input("You: ")
query = HumanMessage(prompt)

messages.append(query)

print(messages)

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

llm_with_tool = llm.bind_tools([get_text_length])
result = llm_with_tool.invoke(messages)
# print(result)
# AIMessage(
#     content='',
#     additional_kwargs={
#         'tool_calls': [
#             {
#                 'id': 'y6jjztrvm',
#                 'function': {
#                     'arguments': '{"text":"Hello how are you"}',
#                     'name': 'get_text_length'
#                 },
#                 'type': 'function'
#             }
#         ]
#     },
#     response_metadata={
#         'token_usage': {
#             'completion_tokens': 18,
#             'prompt_tokens': 237,
#             'total_tokens': 255,
#             'completion_time': 0.040010393,
#             'completion_tokens_details': None,
#             'prompt_time': 0.013049439,
#             'prompt_tokens_details': None,
#             'queue_time': 0.161991329,
#             'total_time': 0.053059832
#         },
#         'model_name': 'llama-3.3-70b-versatile',
#         'system_fingerprint': 'fp_3272ea2d91',
#         'service_tier': 'on_demand',
#         'finish_reason': 'tool_calls',
#         'logprobs': None,
#         'model_provider': 'groq'
#     },
#     id='lc_run--019f641b-fbeb-7082-8dbd-e5ecf00c6727-0',
#     tool_calls=[
#         {
#             'name': 'get_text_length',
#             'args': {'text': 'Hello how are you'},
#             'id': 'y6jjztrvm',
#             'type': 'tool_call'
#         }
#     ],
#     invalid_tool_calls=[],
#     usage_metadata={'input_tokens': 237, 'output_tokens': 18, 'total_tokens': 255}
# )

# put this AIResposne(result) into messages as we have to maintain a history

messages.append(result)

print(messages)

# now it will loo like this
# [
#     HumanMessage(
#         content="Return the number of character in the given tex: 'Hello how are you' ",
#         additional_kwargs={},
#         response_metadata={}
#     ),
#     AIMessage(
#         content='',
#         additional_kwargs={
#             'tool_calls': [
#                 {
#                     'id': 'bpyhsh3hh',
#                     'function': {
#                         'arguments': '{"text":"Hello how are you"}',
#                         'name': 'get_text_length'
#                     },
#                     'type': 'function'
#                 }
#             ]
#         },
#         response_metadata={
#             'token_usage': {
#                 'completion_tokens': 18,
#                 'prompt_tokens': 237,
#                 'total_tokens': 255,
#                 'completion_time': 0.037671971,
#                 'completion_tokens_details': None,
#                 'prompt_time': 0.013293334,
#                 'prompt_tokens_details': None,
#                 'queue_time': 0.050271755,
#                 'total_time': 0.050965305
#             },
#             'model_name': 'llama-3.3-70b-versatile',
#             'system_fingerprint': 'fp_dae98b5ecb',
#             'service_tier': 'on_demand',
#             'finish_reason': 'tool_calls',
#             'logprobs': None,
#             'model_provider': 'groq'
#         },
#         id='lc_run--019f641f-6130-7c40-b1b1-197f297268cd-0',
#         tool_calls=[
#             {
#                 'name': 'get_text_length',
#                 'args': {'text': 'Hello how are you'},
#                 'id': 'bpyhsh3hh',
#                 'type': 'tool_call'
#             }
#         ],
#         invalid_tool_calls=[],
#         usage_metadata={'input_tokens': 237, 'output_tokens': 18, 'total_tokens': 255}
#     )
# ]

# now we need one more message ie tool message becoz tool ko bhi to response dena hai

# There can be a multiple tool so to call it we need to extrct its name like get_text_length

# First we need to check ki kya koi tool ki call aayi hai. and we will get to know about it using result

# if result.tool_calls:
#     # extract tool name
#     print(result.tool_calls[0]) 
# #     {
# #     'name': 'get_text_length',
# #     'args': {'text': 'Hello how are you'},
# #     'id': 'e1673kd1q',
# #     'type': 'tool_call'
# # }
#     tool_name = result.tool_calls[0]["name"]
# This is a string  'name': 'get_text_length', and def get_text_length(text: str) ->int: this is a function so we cant call get_text_length so for this we create a dictionary and inside it we will put all the tools. So if we extract any tool name then uska function bhi call ho jayega.

if result.tool_calls:
    # extract tool name
    tool_name = result.tool_calls[0]["name"]
    tool_message = tools[tool_name].invoke(result.tool_calls[0]) 
    print(tool_message)  # ToolMessage(content='17', name='get_text_length', tool_call_id='64h3f85rc')
    messages.append(tool_message)
    print(messages)
#  https://youtu.be/CUDT5E6jz84?si=Cnh_LSHN6Ujx_XBb&t=8879


# abb in sab messages ko wapis se LLM ke pass bhejange so that LLM ko ye pata ho ki kaha AI hai kaha human hai and kaha tool hai. sabka content bhi pata hoga.

result = llm_with_tool.invoke(messages)
print(result.content)  
# The given text 'Hello how are you' has 17 characters.

# Earlier LLM was not sure what we are asking but now it is sure that we r aksing to find length of characters.