from langchain_ollama import ChatOllama
import streamlit as st 


llm = ChatOllama(
    model="qwen2.5-coder:7b",
    temperature=0,
    # other params...
)

messages = [
    (
        "system",
        "You are a system that can controll multiple robots in a environment. Your Name Is LARS[Large Action Robotic Systems] , user will ask you some random questions so respond accordingly",
    ),
    ("human", " Who are you, what all can you do"),
]


ai_msg = llm.invoke(messages)
print(ai_msg.content)