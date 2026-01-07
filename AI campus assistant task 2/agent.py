from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool

# Tool
def campus_rules(query: str) -> str:
    query = query.lower()

    if "car" in query or "parking" in query:
        return "Cars are allowed only in designated parking zones."

    if "phone" in query:
        return "Mobile phones are not allowed during exams."

    if "id" in query:
        return "ID card is mandatory inside the campus."

    if "library" in query:
        return "Silence must be maintained in library areas."

    if "lab" in query:
        return "Entry to labs is allowed only with faculty permission."

    return "Please follow all official campus rules."

tools = [
    Tool(
        name="CampusRules",
        func=campus_rules,
        description="Answer questions related to campus rules"
    )
]

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    max_iterations=2
)

print("Level 3: Agentic Campus Rules Assistant")
print("Type 'exit' to quit\n")

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break

    response = agent.run(query)
    print("Agent:", response)
