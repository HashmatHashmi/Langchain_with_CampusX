from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(
    # model_name="gpt-4o",
     model="gpt-5.6-luna",
)

result = llm.invoke("What is the capital of South Korea?")

print(result)

