
from enum import Enum
import os
from pathlib import Path
from typing import List
import webvtt

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS

VECTOR_STORE_PATH = Path("vectorstores")

class TextContentType(Enum):
    VTT = "vtt"
    MARKDOWN = "markdown"

class TextContent:

    def __init__(self, texts: List[str], metadata: List[dict], content_type: TextContentType, name: str, session: str) -> None:
        self.texts = texts
        self.metadata = metadata
        self.content_type = content_type
        self.name = name
        self.vs = None
        self.session_name = session

    def _chunk(self):
        if self.content_type == TextContentType.VTT:
            return get_transcript_chunks(self.texts, self.metadata)
        elif self.content_type == TextContentType.MARKDOWN:
            chunks = naive_text_chunk(self.texts[0])
            return chunks, [self.metadata[0] for _ in range(len(chunks))]
        else:
            raise ValueError("Unknown content type.")


    def vectorstore(self):
        chunked_texts, chunked_metadata = self._chunk()
        vs_name = self.session_name + "_" + self.name + "_" + self.content_type.value
        vs = create_vectorstore(vs_name, chunked_texts, chunked_metadata)
        self.vs = vs
        return vs

    def retriever(self):
        if self.vs is None:
            self.vectorstore()
        return self.vs.as_retriever(search_kwargs={"k": 5})


def _exists_vectorstore(name: str):
    return os.path.exists(VECTOR_STORE_PATH / name)

def create_vectorstore(
        name: str,
        chunks: List[str],
        metadata: List[dict] = None,
        embedding=OpenAIEmbeddings(),
        vectorstore=FAISS,
    ):
        if _exists_vectorstore(name):
            print(
                f"The vectorstore {name} already exists. Change the name or delete it to generate a new one."
            )
            vectorstore = vectorstore.load_local(
                VECTOR_STORE_PATH / name, embeddings=embedding
            )
            return vectorstore
        elif chunks and metadata:
            vectorstore = vectorstore.from_texts(
                chunks, metadatas=metadata, embedding=embedding
            )
            vectorstore.save_local(VECTOR_STORE_PATH / name)
            return vectorstore
        elif chunks:
            vectorstore = vectorstore.from_texts(chunks, embedding=embedding)
            vectorstore.save_local(VECTOR_STORE_PATH / name)
            return vectorstore
        else:
            raise ValueError(
                "Either a vectorstore with the given name must exist or chunks and metadata must be provided."
            )


def read_all_markdown(markdown_path: Path):
    markdowns = markdown_path.glob("*.md")
    texts = []
    metadata = []
    for markdown in markdowns:
        doc_name = markdown.stem
        texts.append(markdown.read_text())
        metadata.append(
            {
                "doc_name": doc_name,
            }
        )
    return texts, metadata


def read_transcripts(transcript_path: Path):
    transcripts = transcript_path.glob("*.txt")

    texts = []
    metadata = []

    for transcript in transcripts:
        captions = webvtt.read(transcript)
        doc_name = transcript.stem

        caption_texts = []
        caption_metadata = []

        for caption in captions:
            meta = {
                "start_time": caption.start,
                "end_time": caption.end,
                "doc_name": doc_name,
            }
            caption_metadata.append(meta)
            caption_texts.append(caption.text)

        texts.extend(caption_texts)
        metadata.extend(caption_metadata)

    return texts, metadata


def get_transcript_chunks(texts, metadata, chunk_size=10):
    n = len(texts)
    chunks = []
    chunked_metadata = []
    for i in range(0, n - chunk_size, chunk_size):
        chunk_captions = texts[i : i + chunk_size]
        chunks.append(" ".join(chunk_captions))

        chunked_metadata.append(
            {
                "start_time": metadata[i]["start_time"],
                "end_time": metadata[i + chunk_size - 1]["end_time"],
                "doc_name": metadata[i]["doc_name"],
            }
        )
    return chunks, chunked_metadata

def naive_text_chunk(text: str, chunk_size=1000, overlap=0.5):
    overlap = int(chunk_size * overlap)
    chunks = []
    start = 0
    end = chunk_size
    while start < len(text):
        chunks.append(text[start:end])
        start += chunk_size - overlap
        end = start + chunk_size
    return chunks