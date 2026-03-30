from dotenv import load_dotenv
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

load_dotenv(override=True)

model = ChatOpenAI(model="gpt-4o-mini")

messages = [
    SystemMessage(content="Solve the following math problem"),
    HumanMessage(content="What is 2 + 2 ?")
]

result = model.invoke(messages)

print(f"Answer from AI is : {result.content}")

messages = [
    SystemMessage(content="Solve the following math problem"),
    HumanMessage(content="What is 2 + 2 ?"),
    AIMessage(content=result.content),
    HumanMessage(content="What is 1/1?")
]

result = model.invoke(messages)

print(f"Answer from AI is : {result.content}")


messages.append(AIMessage(result.content))

print(messages)