from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv(override=True)

model = ChatOpenAI(model = "gpt-4o-mini")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are comedian who tells jokes about {topic}"),
        ("human", "Tell me {count} jokes")
    ]
)

chain = prompt_template | model | StrOutputParser()

result = chain.invoke({"topic": "doctors", "count": 2})

print(result)