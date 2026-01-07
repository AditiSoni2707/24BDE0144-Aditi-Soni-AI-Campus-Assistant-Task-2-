from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings

# Load document
loader = TextLoader("data/rules.txt")
docs = loader.load()

# Split text
splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# Create vector DB
vectorstore = Chroma.from_documents(
    chunks,
    embedding=OpenAIEmbeddings()
)

# Create RAG chain
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever()
)

print(" Level 2: RAG Campus Assistant")
print("Type 'exit' to quit\n")

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break

    result = qa.run(query)
    print("Answer:", result)

