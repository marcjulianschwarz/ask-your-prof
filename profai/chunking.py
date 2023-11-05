def get_chunks(texts, metadata, chunk_size=10):
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
