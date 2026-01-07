from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

print(" Level 1: AI Campus Chatbot")
print("Type 'exit' to quit\n")

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break

    response = llm.invoke(query)
    print("Bot:", response.content)
