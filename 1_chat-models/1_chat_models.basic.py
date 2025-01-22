# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

from dotenv import load_dotenv
# from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama


# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
# model = ChatOpenAI(model="gpt-4o-mini")
model = ChatOllama(model="llama3.2")

# Invoke the model with a message
result = model.invoke("What is 3 / 3")
print("Full result:")
print(result)
print("Content only:")
print(result.content)

# poetry run python3 1_chat-models/1_chat_models.basic.py
# poetry add langchain-ollama
# poetry env activate