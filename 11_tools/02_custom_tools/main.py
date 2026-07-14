from langchain.tools import tool

@tool   # decorator for creating a tool 
def get_greeting(name: str) -> str:
    """Generate a greeting message for user"""   # docs string 
    return f"Hello {name}, Welcome to the AI world"

# This was a function and we made it a tool using @tool

# since it is a toll so we can invoke it

result = get_greeting.invoke({"name": "Ritesh"})

print(result )
print(get_greeting.name )  # name of the tool
print(get_greeting.description )  # description of the tool
print(get_greeting.args )  # argumetns of the tool that it needed.

