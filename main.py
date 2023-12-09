from langchain.chat_models.gigachat import GigaChat
import congif
from Message import Message
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain

chat = GigaChat(credentials=congif.token, verify_ssl_certs=False)

prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "You are a nice chatbot having a conversation with a human."
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("ты не устаешь?")
    ]
) #promt - настройка ответов сети

conversation = ConversationChain(
    llm=chat,
    verbose=True,
    memory=ConversationBufferMemory()
)
conversation.predict(input="переведи на английский слово привет")
print(conversation)
print(conversation.memory.load_memory_variables({}))
print('rfind', conversation.memory.load_memory_variables({}).get('history')[conversation.memory.load_memory_variables({}).get('history').rfind("AI")+4:])

print('следующий запрос')
print(conversation.run(Message().generateMessage("какое самое последнее событие в мире ты знаешь")))

# memory = ConversationBufferMemory(return_messages=True)
# memory.chat_memory.add_user_message("hi")
# memory.chat_memory.add_ai_message("whats up?")
# memory.chat_memory.add_user_message("nice")
# print(memory.load_memory_variables({}))



