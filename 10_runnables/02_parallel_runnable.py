# from dotenv import load_dotenv
# load_dotenv()

# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import RunnableParallel

# # components
# model = ChatGroq(
#     model="llama-3.3-70b-versatile"
# )

# parser = StrOutputParser()


# # 2 different prompts
# short_prompt = ChatPromptTemplate.from_template(
#     "Explain {topic} in 2 lines"
# )

# long_prompt = ChatPromptTemplate.from_template(
#     "Explain {topic} in 10 lines"
# )

# # input
# topic = "India"

# # 1st pipeline: short_prompt | model | parser
# # 2nd prompt long_prompt | model | parser

# chains = RunnableParallel({
#     "short": short_prompt | model | parser,
#     "detailed": long_prompt | model | parser
# })

# result = chains.invoke({"topic": topic})

# print(result)
# {'short': 'India is a vast and diverse country located in South Asia, known for its rich cultural heritage, historic landmarks, and vibrant cities. With a population of over 1.3 billion people, India is a melting pot of languages, religions, and traditions, offering a unique blend of modernity and tradition.', 'detailed': "India is a country located in South Asia.\nIt is the seventh-largest country by land area and has a diverse geography.\nIndia is home to over 1.3 billion people, making it the second-most populous country.\nThe country has a rich cultural heritage, with a history dating back to the Indus Valley Civilization.\nIndia is a federal parliamentary democratic republic, with a president as head of state.\nThe country has a diverse economy, with major industries in IT, textiles, and pharmaceuticals.\nIndia is home to many languages, including Hindi, English, and several regional languages.\nThe country is known for its vibrant festivals, such as Diwali and Holi.\nIndia is also home to many famous landmarks, including the Taj Mahal and the Golden Temple.\nThe country's cuisine is also diverse, with popular dishes like curry, tandoori chicken, and naan bread."}

# print(result['short'])
# India is a vast and diverse country located in South Asia, known for its rich cultural heritage, vibrant cities, and breathtaking natural beauty. With a population of over 1.3 billion people, India is a melting pot of languages, religions, and traditions, offering a unique and fascinating experience for visitors and locals alike.

# print(result['detailed'])

# India is a country located in South Asia.
# It is the seventh-largest country by land area and the second-most populous.
# India has a diverse geography, with mountains, rivers, and coastlines.
# The country has a rich cultural heritage, with many languages and religions.
# Hinduism, Islam, Christianity, and Sikhism are the main religions practiced.
# India is home to many ancient monuments, such as the Taj Mahal.
# The country has a rapidly growing economy, with major industries in IT and manufacturing.
# India is known for its vibrant cities, including Mumbai, Delhi, and Bangalore.
# The country has a rich culinary tradition, with popular dishes like curry and tandoori chicken.
# India is a democratic republic, with a parliamentary system of government.



# what if we want to provide some differnt topic in short and different in detailed pipeline then we will create a dictinary in result.


from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableLambda

# components
model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

parser = StrOutputParser()


# 2 different prompts
short_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in 2 lines"
)

long_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in 10 lines"
)

# input
topic = "India"

# 1st pipeline: short_prompt | model | parser
# 2nd prompt long_prompt | model | parser

# https://youtu.be/CUDT5E6jz84?si=bwC-r_rc7WXZQQRR&t=3123
chains = RunnableParallel({
    "short": RunnableLambda(lambda x:x['short']) | short_prompt | model | parser,
    "detailed": RunnableLambda(lambda x:x['detailed']) | long_prompt | model | parser
})

result = chains.invoke({"short": {"topic": "India"},
                        "detailed": {"topic": "USA"}})  

print(result)
# {'short': 'India is a vast and diverse country located in South Asia, known for its rich cultural heritage, vibrant cities, and breathtaking natural landscapes. With a population of over 1.3 billion people, India is a melting pot of languages, religions, and traditions, making it a unique and fascinating destination to explore.', 'detailed': "The United States of America (USA) is a country in North America.\nIt is a federal republic consisting of 50 states and a federal district.\nThe capital is Washington, D.C., and the largest city is New York City.\nThe USA is the world's third-most populous country, with over 331 million people.\nThe country has a diverse geography, including mountains, forests, and coastlines.\nThe USA is a global leader in economy, technology, and innovation.\nIt has a mixed economy, with a strong service sector and a significant manufacturing industry.\nThe country is known for its cultural diversity, with influences from European, African, and Asian cultures.\nThe USA is a major player in global politics and international relations.\nIt is a founding member of the United Nations and a key member of NATO and other international organizations."}
