from operator import itemgetter

from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.vectorstores.base import VectorStore

from profai.prompts import (
    create_answer_with_context_prompt,
    create_answer_with_transcript_and_slides_prompt,
)


def _combine_documents_transcript(docs, document_separator="\n\n"):
    doc_strings = [
        f"Document Name: {doc.metadata['doc_name']}\nTimestamp: {doc.metadata['start_time']}\nContent:{doc.page_content}"
        for doc in docs
    ]
    return document_separator.join(doc_strings)


def _combine_documents(docs, document_separator="\n\n"):
    doc_strings = [f"Content: {doc.page_content}" for doc in docs]
    return document_separator.join(doc_strings)


def create_simple_chain(vectorstore: VectorStore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    PROMPT = create_answer_with_context_prompt()

    context = {
        "context": itemgetter("question") | retriever | _combine_documents,
        "question": itemgetter("question"),
    }

    chain = context | PROMPT | ChatOpenAI() | StrOutputParser()
    return chain


def create_transcript_slides_chain(
    transcript_vectorstore: VectorStore, slides_vectorstore: VectorStore
):
    transcript_retriever = transcript_vectorstore.as_retriever(search_kwargs={"k": 5})
    slides_retriever = slides_vectorstore.as_retriever(search_kwargs={"k": 5})

    PROMPT = create_answer_with_transcript_and_slides_prompt()

    docs = {
        "transcript_docs": itemgetter("question") | transcript_retriever,
        "slides_docs": itemgetter("question") | slides_retriever,
        "question": itemgetter("question"),
    }

    context = {
        "transcript": lambda x: _combine_documents_transcript(x["transcript_docs"]),
        "slides": lambda x: _combine_documents(x["slides_docs"]),
        "transcript_docs": itemgetter("transcript_docs"),
        "slides_docs": itemgetter("slides_docs"),
        "question": itemgetter("question"),
    }

    answer = {
        "answer": PROMPT | ChatOpenAI() | StrOutputParser(),
        "transcript_docs": itemgetter("transcript_docs"),
        "slides_docs": itemgetter("slides_docs"),
    }

    chain = RunnablePassthrough() | docs | context | answer

    return chain
