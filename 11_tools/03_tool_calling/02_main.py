from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain.tools import tool
from rich import print

# Creating a tool
@tool 
def get_text_length(text: str) ->int:
    """ Return the number of character in a given text """
    return (len(text))


llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

# tool binding. 
llm_with_tool = llm.bind_tools([get_text_length])


# result1 = llm.invoke("Return the number of character in the given text: 'Hello how are you'")
# result2 = llm_with_tool.invoke("Return the number of character in the given text: 'Hello how are you'")

# print(result1)

# print()
# print()
# print(result2)


# AIMessage(
#     content="To find the number of characters in the given text 'Hello how are you', we count each 
# letter, space, and punctuation mark.\n\nHere's the count:\n1. H\n2. e\n3. l\n4. l\n5. o\n6. 
# (space)\n7. h\n8. o\n9. w\n10. (space)\n11. a\n12. r\n13. e\n14. (space)\n15. y\n16. o\n17. 
# u\n\nThere are 17 characters in the given text.",
#     additional_kwargs={},
#     response_metadata={
#         'token_usage': {
#             'completion_tokens': 114,
#             'prompt_tokens': 51,
#             'total_tokens': 165,
#             'completion_time': 0.215652861,
#             'completion_tokens_details': None,
#             'prompt_time': 0.002497691,
#             'prompt_tokens_details': None,
#             'queue_time': 0.051395779,
#             'total_time': 0.218150552
#         },
#         'model_name': 'llama-3.3-70b-versatile',
#         'system_fingerprint': 'fp_dae98b5ecb',
#         'service_tier': 'on_demand',
#         'finish_reason': 'stop',
#         'logprobs': None,
#         'model_provider': 'groq'
#     },
#     id='lc_run--019f6070-65f7-7842-a6c4-2baa60e697cd-0',
#     tool_calls=[],
#     invalid_tool_calls=[],
#     usage_metadata={'input_tokens': 51, 'output_tokens': 114, 'total_tokens': 165}
# )


# AIMessage(
#     content='',
#     additional_kwargs={
#         'tool_calls': [
#             {
#                 'id': 'xfvkmrc69',
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
#             'prompt_tokens': 236,
#             'total_tokens': 254,
#             'completion_time': 0.041404396,
#             'completion_tokens_details': None,
#             'prompt_time': 0.012043866,
#             'prompt_tokens_details': None,
#             'queue_time': 0.161066475,
#             'total_time': 0.053448262
#         },
#         'model_name': 'llama-3.3-70b-versatile',
#         'system_fingerprint': 'fp_3272ea2d91',
#         'service_tier': 'on_demand',
#         'finish_reason': 'tool_calls',
#         'logprobs': None,
#         'model_provider': 'groq'
#     },
#     id='lc_run--019f6070-6997-7e10-999a-8d62931be378-0',
#     tool_calls=[
#         {
#             'name': 'get_text_length',
#             'args': {'text': 'Hello how are you'},
#             'id': 'xfvkmrc69',
#             'type': 'tool_call'
#         }
#     ],
#     invalid_tool_calls=[],
#     usage_metadata={'input_tokens': 236, 'output_tokens': 18, 'total_tokens': 254}
# )

# result1 ke content me wo response de rha hai but result2 ke content me wo khali hai.
# and result1 ke kewards argument khali hai =  additional_kwargs={},
# while result2 ka keyword argument me 
#additional_kwargs={
    #     'tool_calls': [
    #         {
    #             'id': 'xfvkmrc69',
    #             'function': {
    #                 'arguments': '{"text":"Hello how are you"}',
    #                 'name': 'get_text_length'
    #             },
    #             'type': 'function'
    #         }
    #     ]
    # },

# It means abb jo ye llm hai jisko hamne bind krke rtakha hai wo suggest kr rha hai ki aap ye wala tool call kr shakte ho ie get_text_length and usko ek argument bhejoge ie 'arguments': '{"text":"Hello how are you"}',
# result2 ka output_tokens': 18 hai due to additional keyword argument


# tool execution

result = llm_with_tool.invoke("Return the number of character in the given text: 'Hello how are you'")


# checking if there is any tool call if yes then extract that tool call
if result.tool_calls:    
    tool_call = result.tool_calls[0]
    tool_result = get_text_length.invoke(tool_call["args"])
    
    # send back to llm
    final_response = llm.invoke(f"the length of text is {tool_result}")

print(final_response.content)
print(result.tool_calls[0])
# {
#     'name': 'get_text_length',
#     'args': {'text': 'Hello how are you'},
#     'id': '5dfd7f44z',
#     'type': 'tool_call'
# }

# sending this arguments to our function 
print(get_text_length.invoke({'text': 'Hello how are you'}))  # 17

# if we send the whole dictionary then 
print(get_text_length.invoke({
    'name': 'get_text_length',
    'args': {'text': 'Hello how are you'},
    'id': 'dgcstan0z',
    'type': 'tool_call'
}))   
# we got a tool message
# ToolMessage(content='17', name='get_text_length', tool_call_id='dgcstan0z')

# Now we will maintain a history in 03_main.py