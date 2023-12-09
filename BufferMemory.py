from langchain.chat_models.gigachat import GigaChat
import congif

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

chat = GigaChat(credentials=congif.token, verify_ssl_certs=False)

conversation = ConversationChain(
    llm=chat,
    verbose=True,
    memory=ConversationBufferMemory()
)
conversation.predict(input="почему небо синее?")

conversation.predict(input="I'm doing well! Just having a conversation with an AI.")
print(conversation.memory.load_memory_variables({}))
print(conversation.memory.load_memory_variables({}).get('history')[conversation.memory.load_memory_variables({}).get('history').rfind("AI")+4:])
print()
print(conversation.memory.buffer)
