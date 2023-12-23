from operator import itemgetter
from typing import List

from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough

from profai.content import TextContent
from profai.prompts import GENERAL_CONTEXT_PROMPT, GENERAL_CONTEXT_PROMPT_DE


def create_chain(contents: List[TextContent]):
    PROMPT = GENERAL_CONTEXT_PROMPT

    answer_chain = PROMPT.prompt | ChatOpenAI() | StrOutputParser()

    docs = {
        content.name + "_doc": itemgetter("question") | content.retriever()
        for content in contents
    }
    docs["question"] = itemgetter("question")

    contexts = {
        content.name: lambda x: content.combine_docs(x[content.name + "_doc"])
        for content in contents
    }
    contexts["question"] = itemgetter("question")

    for content in contents:
        contexts[content.name + "_doc"] = itemgetter(content.name + "_doc")

    answer = {
        "answer": answer_chain,
    }

    for content in contents:
        answer[content.name] = itemgetter(content.name)
        answer[content.name + "_doc"] = itemgetter(content.name + "_doc")

    chain = RunnablePassthrough() | docs | contexts | answer

    return chain
