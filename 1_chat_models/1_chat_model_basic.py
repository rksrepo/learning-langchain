from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(override=True)

model = ChatOpenAI(model="gpt-4o-mini")

result = model.invoke("What is 2+2?")

# print(result)

print(result.content)