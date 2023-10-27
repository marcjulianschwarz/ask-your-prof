def get_chunk(texts, metadata):
    n = len(texts)
    chunks = []
    chunked_metadata = []
    for i in range(0, n - 10, 10):
        chunk_captions = texts[i : i + 10]
        chunks.append(" ".join(chunk_captions))

        chunked_metadata.append(
            {
                "start_time": metadata[i]["start_time"],
                "end_time": metadata[i + 9]["end_time"],
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
