from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.messages import SystemMessage, HumanMessage
import os

load_dotenv(override=True)

messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
]


openai = ChatOpenAI(model="gpt-4o-mini")
openai_result = openai.invoke(messages)
print(f"Answer from OpenAI: {openai_result.content}")

anthropic_api_key=os.getenv("ANTHROPIC_API_KEY")
anthropicai = ChatOpenAI(base_url="https://api.anthropic.com/v1", api_key=anthropic_api_key, model="claude-haiku-4-5")
anthropicai_result = anthropicai.invoke(messages)
print(f"Answer from Anthropic: {anthropicai_result.content}")

or_api_key=os.getenv("OPEN_ROUTER_API_KEY")
or_ai = ChatOpenAI(model="google/google/gemini-2.0-flash", base_url="https://openrouter.ai/api/v1", api_key=or_api_key)
orai_result = anthropicai.invoke(messages)
print(f"Answer from Gemini through Open Router: {orai_result.content}")