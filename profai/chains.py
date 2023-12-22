from operator import itemgetter
from typing import List

from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.vectorstores.base import VectorStore, VectorStoreRetriever
from profai.content import TextContent

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


def create_chain(contents: List[TextContent]):
    
    PROMPT = GENERAL_CONTEXT_PROMPT
    answer_chain = PROMPT.prompt | ChatOpenAI() | StrOutputParser()


    docs = {
        content.name + "_doc": itemgetter("question") | content.retriever() for content in contents
    }
    docs["question"] = itemgetter("question")

    contexts = {
        content.name: lambda x: _combine_documents_transcript(x[content.name + "_doc"]) for content in contents
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


# def create_simple_chain(vectorstore: VectorStore):
#     retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

#     PROMPT = create_answer_with_context_prompt()

#     docs = {
#         "docs": itemgetter("question") | retriever,
#         "question": itemgetter("question"),
#     }

#     context = {
#         "context": lambda x: _combine_documents_transcript(x["docs"]),
#         "docs": itemgetter("docs"),
#         "question": itemgetter("question"),
#     }

#     answer = {
#         "answer": PROMPT | ChatOpenAI() | StrOutputParser(),
#         "docs": itemgetter("docs"),
#     }

#     chain = RunnablePassthrough() | docs | context | answer
#     return chain


# def create_transcript_slides_chain(
#     transcript_vectorstore: VectorStore, slides_vectorstore: VectorStore
# ):
#     transcript_retriever = transcript_vectorstore.as_retriever(search_kwargs={"k": 5})
#     slides_retriever = slides_vectorstore.as_retriever(search_kwargs={"k": 5})

#     PROMPT = create_answer_with_transcript_and_slides_prompt()

#     docs = {
#         "transcript_docs": itemgetter("question") | transcript_retriever,
#         "slides_docs": itemgetter("question") | slides_retriever,
#         "question": itemgetter("question"),
#     }

#     context = {
#         "transcript": lambda x: _combine_documents_transcript(x["transcript_docs"]),
#         "slides": lambda x: _combine_documents(x["slides_docs"]),
#         "transcript_docs": itemgetter("transcript_docs"),
#         "slides_docs": itemgetter("slides_docs"),
#         "question": itemgetter("question"),
#     }

#     answer = {
#         "answer": PROMPT | ChatOpenAI() | StrOutputParser(),
#         "transcript_docs": itemgetter("transcript_docs"),
#         "slides_docs": itemgetter("slides_docs"),
#     }

#     chain = RunnablePassthrough() | docs | context | answer

#     return chain
