import json
from pathlib import Path

from langchain.prompts import ChatPromptTemplate

PROMPTS_PATH = Path("prompts")
CONF_PATH = PROMPTS_PATH / "conf.json"

conf = CONF_PATH.read_text()
conf = json.loads(conf)


def load_prompt(name: str):
    prompt_path = PROMPTS_PATH / name
    return prompt_path.read_text()


def create_answer_with_context_prompt():
    if "context" in conf:
        return ChatPromptTemplate.from_template(load_prompt(conf["context"]))
    else:
        raise ValueError("No context prompt found in conf.json")


def create_answer_with_transcript_and_slides_prompt():
    if "transcript_and_slides" in conf:
        return ChatPromptTemplate.from_template(
            load_prompt(conf["transcript_and_slides"])
        )
    else:
        raise ValueError("No transcript_and_slides prompt found in conf.json")
