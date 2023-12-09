"""Память сущностей запоминает данные факты о конкретных сущностях в разговоре. Она извлекает информацию о сущностях (используя LLM) и со временем
 наращивает свои знания об этой сущности (также используя LLM)."""

from langchain.memory import ConversationEntityMemory
from langchain.llms import GigaChat
from langchain.chains import ConversationChain
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE

import congif

llm = GigaChat(credentials=congif.token, verify_ssl_certs=False)
memory = ConversationEntityMemory(llm=llm)

_input = {"input": "Deven & Sam are working on a hackathon project"}
memory.load_memory_variables(_input)
memory.save_context(
    _input,
    {"output": "That sounds like a great project! What kind of project are they working on"}
)
memory.load_memory_variables({"input": 'who is Sam'})

print(memory)

conversation = ConversationChain(
    llm=llm,
    verbose=True,
    prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
    memory=ConversationEntityMemory(llm=llm)
)  # создание разговора, цупочки разговора

conversation.predict(input="Deven & Sam are working on a hackathon project")
print(conversation.memory.entity_store.store)
