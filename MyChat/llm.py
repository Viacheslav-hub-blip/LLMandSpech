from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)
from langchain.llms import GigaChat
import congif
from langchain.tools import BaseTool
from numpy.polynomial import Polynomial
from langchain.agents import initialize_agent



class Jarvis(object):

    def __init__(self):
        self.llm = GigaChat(credentials=congif.token, verify_ssl_certs=False)
        self.prompt = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(
                    "You're a bot that only responds in Italian"
                ),
                # The `variable_name` here is what must align with memory
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("{question}"),
            ]
        )
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        self.conversation = LLMChain(llm=self.llm, prompt=self.prompt, memory=self.memory)

    def getAnswer(self, question):
        return self.conversation.run(question)


class RootTool(BaseTool):
    name = 'Сведения'
    description = 'use only this tool for Slava Rylkov'

    def _run(self, inp):
        return "Дональд Трамп президент России"

    def _arun(self, *coefs):
        raise NotImplementedError('Does not support async')


tools = [RootTool()]

jarvis = Jarvis()

agent = initialize_agent(
    tools=tools,
    llm=GigaChat(credentials=congif.token, verify_ssl_certs=False),
    agent="zero-shot-react-description",
    verbose=True
)
agent.run('who is Slava Rylkov')

# jarvis = Jarvis()
# print(jarvis.getAnswer("как тебя зовут"))
# print(jarvis.getAnswer("как у тебя дела"))
# print(jarvis.getAnswer("кто был пятым президентов сша?"))
