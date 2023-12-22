from operator import itemgetter
from typing import List

from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from profai.content import TextContent, TextContentType

from profai.prompts import (
    GENERAL_CONTEXT_PROMPT,
)


def _combine_documents_transcript(docs, document_separator="\n\n"):
    doc_strings = [
        f"Document Name: {doc.metadata['doc_name']}\nTimestamp: {doc.metadata['start_time']}\nContent: {doc.page_content}"
        for doc in docs
    ]
    return document_separator.join(doc_strings)


def _combine_documents(docs, document_separator="\n\n"):
    doc_strings = [f"Content: {doc.page_content}" for doc in docs]
    return document_separator.join(doc_strings)

def get_doc_combiner(content: TextContent):
    if content.content_type == TextContentType.VTT:
        return _combine_documents_transcript
    elif content.content_type == TextContentType.MARKDOWN:
        return _combine_documents
    else:
        raise ValueError("Unknown content type.")


def create_chain(contents: List[TextContent]):
    
    PROMPT = GENERAL_CONTEXT_PROMPT
    answer_chain = PROMPT.prompt | ChatOpenAI() | StrOutputParser()


    docs = {
        content.name + "_doc": itemgetter("question") | content.retriever() for content in contents
    }
    docs["question"] = itemgetter("question")

    contexts = {
        content.name: lambda x: get_doc_combiner(content)(x[content.name + "_doc"]) for content in contents
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

