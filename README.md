# 24BDE0144-Aditi-Soni-AI-Campus-Assistant-Task-2-
I have built an Ai Campus assistant using langchain and openai showing three levels 1)Basic LLM interaction 2) RAG  3) Agentic AI using decision making

In level 1)
File: app.py , 
Its direct interaction with LLM , demonstrates prompt to give response flow

In level 2)
File: rag.py
,Data: rules.txt
,I have loaded campus rules from an external txt file and ai gets thes answers from the files only

In level 3)
Uses an agentic ai , the agent reasons step by step and safely stops if information is not available


step 1)
Create a Virtual Environment
On Windows:
python -m venv .venv
.venv\Scripts\activate


step 2)
To Install Dependencies:
 pip install -r requirements.txt

step 3)
Add API Key


step 4)
To Run the Levels:
python app.py         # Level 1
python rag.py          # Level 2
python agent.py        # Level 3


Technologies Used
Python
,LangChain
,OpenAI API




