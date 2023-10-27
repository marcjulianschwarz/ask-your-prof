import os
from pathlib import Path
from typing import List

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS


def create_vectorstore(
    name: str,
    chunks: List[str] = None,
    metadata: List[dict] = None,
    embedding=OpenAIEmbeddings(),
    vectorstore=FAISS,
    vectorstore_path=Path("vectorstores"),
):
    if os.path.exists(vectorstore_path / name):
        vectorstore = vectorstore.load_local(
            vectorstore_path / name, embeddings=embedding
        )
        return vectorstore
    elif chunks and metadata:
        vectorstore = vectorstore.from_texts(
            chunks, metadatas=metadata, embedding=embedding
        )
        vectorstore.save_local(vectorstore_path / name)
        return vectorstore
    elif chunks:
        vectorstore = vectorstore.from_texts(chunks, embedding=embedding)
        vectorstore.save_local(vectorstore_path / name)
    else:
        raise ValueError(
            "Either a vectorstore with the given name must exist or chunks and metadata must be provided."
        )
