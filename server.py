from langchain_ollama import OllamaLLM
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a coder."),
    ("user", "{input}")
])

llm = OllamaLLM(model="llama3.1")

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

print(chain.invoke({"input": "what is java?"}))
