from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.messages import SystemMessage, HumanMessage, AIMessage
import os

load_dotenv(override=True)

model = ChatOpenAI(model="gpt-4o-mini")

chat_history = []

system_message = SystemMessage("You are a helpful AI Assistant")
chat_history.append(system_message)

while True:
    query = input("You : ")
    if query.lower() == 'exit':
        break
    chat_history.append(HumanMessage(content=query))

    result = model.invoke(chat_history)
    response = result.content

    chat_history.append(AIMessage(content=response))

    print(f"AI : {response}")


print("--- Message History ---")
print(chat_history)

