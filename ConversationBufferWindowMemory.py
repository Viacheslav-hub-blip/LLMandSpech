"""ConversationBufferWindowMemory сохраняет список взаимодействий в разговоре с течением времени.
Он использует только последние K взаимодействий. Это может быть полезно для
сохранения скользящего окна самых последних взаимодействий,
чтобы буфер не становился слишком большим."""

from langchain.memory import ConversationBufferWindowMemory
from langchain.chat_models.gigachat import GigaChat
import congif

from langchain.chains import ConversationChain

memoryt = ConversationBufferWindowMemory(k=1, return_messages=True)
memoryt.save_context({"input": "hi"}, {"output":"whats up"})
memoryt.save_context({"input": "not much you"}, {"output": "not much"})
#print(memoryt.load_memory_variables({}))

conversation_with_summary = ConversationChain(
    llm = GigaChat(credentials=congif.token, verify_ssl_certs=False),
    memory = ConversationBufferWindowMemory(k=2),
    verbose=True
)
print(conversation_with_summary.predict(input="Hi"))

print(conversation_with_summary.predict(input="какая ожидается погода зимой?"))
print(conversation_with_summary.prompt.template)

