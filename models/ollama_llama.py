from langchain_community.chat_message_histories import ChastMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
from langchain_core.runnables import RunnableWithMessageHistory


def llamaChain():
    # Define the prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a coder."),
        ("user", "{text}")
    ])

    # Define the model
    llm = OllamaLLM(model="llama3.1")

    # Define the output parser
    output_parser = StrOutputParser()

    # Define the chain
    chain = prompt | llm | output_parser

    return chain


store = {}


def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChastMessageHistory()
    return store.get(session_id, [])


def do_message(session_id: str, text: str):
    chain = llamaChain()
    history = get_session_history(session_id)
    result = chain.invoke({"text": text, "history": history})
    history.add_message("user", text)
    history.add_message("assistant", result)
    return result
