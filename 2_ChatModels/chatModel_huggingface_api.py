import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# os.environ["HF_HOME"] = "D:/huggingface_cache"


load_dotenv()

# Step 1: Define the remote endpoint
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation",
    max_new_tokens=256,
    do_sample=False,
    provider="auto",  # Allows the HF router to select the active inference provider
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)

# Step 2: Wrap as a Chat Model
chat_model = ChatHuggingFace(llm=llm)

# Step 3: Invoke using standard LangChain messages
messages = [
    SystemMessage(content="You are a concise geography assistant. Be specific and provide only the answer to the question in no more than 2 lines."),
    HumanMessage(content="What is the capital of South Korea?"),
]

response = chat_model.invoke(messages)



import re

# Remove everything from <think> to </think>
cleaned_output = re.sub(
    r"<think>.*?</think>", "", response.content, flags=re.DOTALL
).strip()
print(cleaned_output)
# Output: Seoul is the capital of South Korea.



# print(response.content)