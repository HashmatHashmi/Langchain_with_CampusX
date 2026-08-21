from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-5.6-luna", 
    temperature=0.7,
    max_completion_tokens=20,
)

result = llm.invoke("What is the capital of South Korea?")

print(result.content)