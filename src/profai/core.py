from pathlib import Path

from profai.content import TextContent
from profai.prompts import GENERAL_CONTEXT_PROMPT, Prompt


class Prof:
    def __init__(
        self,
        video_path: str | Path,
        transcript_path: str | Path,
        slides_path: str | Path,
        vectorstore_path: str | Path,
        session_name: str,
        system_prompt: Prompt = GENERAL_CONTEXT_PROMPT,
        
    ):
        self.video_path = Path(video_path)
        self.transcript_path = Path(transcript_path)
        self.slides_path = Path(slides_path)
        self.vectorstore_path = Path(vectorstore_path)
        self.system_prompt = system_prompt
        self.session_name = session_name
        self.known_contents = []

    def add_content(self, content: TextContent):
        self.known_contents.append(content)


    def ask(self, question: str):
        if self.chain:
            return self.chain.invoke({"question": question})
        else:
            raise ValueError(
                "The profs mode has not been set yet. Try transcript_mode or transcript_slides_mode."
            )



   