from profai.chains import get_simple_chain, get_transcript_slides_chain
from profai.embeddings import create_vectorstore


class Prof:
    def __init__(self):
        self.chain = get_simple_chain(create_vectorstore("zimmermann_chunked_10"))

    def transcript_mode(self):
        self.chain = get_simple_chain(create_vectorstore("zimmermann_chunked_10"))

    def transcript_slides_mode(self):
        t_vs = create_vectorstore("zimmermann_chunked_10_total")
        s_vs = create_vectorstore("slides_1000_400")
        self.chain = get_transcript_slides_chain(t_vs, s_vs)

    def ask(self, question: str):
        return self.chain.invoke({"question": question})
