import webvtt


def get_transcript_and_metadata(path: str, doc_name: str):
    captions = webvtt.read(path)

    texts = []
    metadata = []

    for caption in captions:
        meta = {
            "start_time": caption.start,
            "end_time": caption.end,
            "doc_name": doc_name,
        }
        metadata.append(meta)
        texts.append(caption.text)
    return texts, metadata
