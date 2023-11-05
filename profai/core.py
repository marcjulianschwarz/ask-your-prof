import os
from pathlib import Path
from typing import List

import webvtt
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS

from profai.chains import create_simple_chain, create_transcript_slides_chain
from profai.chunking import get_chunks, naive_text_chunk


class Prof:
    def __init__(
        self,
        video_path: str | Path,
        transcript_path: str | Path,
        slides_path: str | Path,
        vectorstore_path: str | Path,
    ):
        self.video_path = Path(video_path)
        self.transcript_path = Path(transcript_path)
        self.slides_path = Path(slides_path)
        self.vectorstore_path = Path(vectorstore_path)

    def transcript_mode(self, transcript_name="transcript"):
        transcripts, metadata = self._read_transcripts()
        chunked_transcripts, chunked_metadata = get_chunks(transcripts, metadata)

        vs = self._create_vectorstore(
            transcript_name, chunked_transcripts, chunked_metadata
        )
        self.chain = create_simple_chain(vs)

    def transcript_slides_mode(
        self, transcript_name="transcript", slides_name="slides"
    ):
        transcripts, metadata = self._read_transcripts()
        chunked_transcripts, chunked_metadata = get_chunks(transcripts, metadata)

        slides, _ = self._read_all_markdown()
        chunked_slides = []
        for slide in slides:
            chunked_slides.extend(naive_text_chunk(slide))

        t_vs = self._create_vectorstore(
            transcript_name, chunked_transcripts, chunked_metadata
        )
        s_vs = self._create_vectorstore(slides_name, chunked_slides)
        self.chain = create_transcript_slides_chain(t_vs, s_vs)

    def ask(self, question: str):
        if self.chain:
            return self.chain.invoke({"question": question})
        else:
            raise ValueError(
                "The profs mode has not been set yet. Try transcript_mode or transcript_slides_mode."
            )

    def _exists_vectorstore(self, name: str):
        return os.path.exists(self.vectorstore_path / name)

    def _create_vectorstore(
        self,
        name: str,
        chunks: List[str],
        metadata: List[dict] = None,
        embedding=OpenAIEmbeddings(),
        vectorstore=FAISS,
    ):
        if self._exists_vectorstore(name):
            print(
                f"The vectorstore {name} already exists. Change the name or delete it to generate a new one."
            )
            vectorstore = vectorstore.load_local(
                self.vectorstore_path / name, embeddings=embedding
            )
            return vectorstore
        elif chunks and metadata:
            vectorstore = vectorstore.from_texts(
                chunks, metadatas=metadata, embedding=embedding
            )
            vectorstore.save_local(self.vectorstore_path / name)
            return vectorstore
        elif chunks:
            vectorstore = vectorstore.from_texts(chunks, embedding=embedding)
            vectorstore.save_local(self.vectorstore_path / name)
            return vectorstore
        else:
            raise ValueError(
                "Either a vectorstore with the given name must exist or chunks and metadata must be provided."
            )

    def _read_transcripts(self):
        transcripts = self.transcript_path.glob("*.txt")

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

    def _read_all_markdown(self):
        markdowns = self.slides_path.glob("*.md")
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
