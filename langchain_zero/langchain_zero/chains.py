from dotenv import load_dotenv
import os

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings


path_dotenv = r'C:\Users\ramon\Documents\workspace\longchain\.env'
load_dotenv(path_dotenv)


def translate_text_chain():
    llm = ChatOpenAI(temperature=0.6, model='gpt-3.5-turbo')

    parser = StrOutputParser()
    template = ChatPromptTemplate.from_messages([
        ('system', 'Traduza o texto a seguir para {language}'),
        ('user', '{user_text}')
    ])
    
    chain = template | llm | parser
    return chain


