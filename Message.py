from langchain.schema import HumanMessage, SystemMessage
import congif
from langchain.chains import ConversationChain


class Message(object):

    def generateMessage(self, humanMessageContent) -> list:
        message = [
            SystemMessage(
                content=congif.systemMessage_behaviour
            ),
            HumanMessage(
                content=humanMessageContent
            )
        ]

        return message
