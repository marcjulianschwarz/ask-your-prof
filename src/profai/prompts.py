from langchain.prompts import ChatPromptTemplate

class Prompt:

    def __init__(self, text: str, desc: str = None):
        self.text = text
        self.prompt = ChatPromptTemplate.from_template(text)
        self.desc = desc

    def supports(self, placeholder: str):
        placeholder = "{" + placeholder + "}"
        return placeholder in self.text

    def supported_placeholders(self):
        return [
            placeholder[1:-1]
            for placeholder in self.text.split("{")
            if placeholder.endswith("}")
        ]
    

GENERAL_CONTEXT_PROMPT = Prompt("""Answer the question in a concise way.

You will have access to parts of a lecture transcript (see CONTEXT) that may help you answer the question. 
Please try to answer the question using only the information in the context. 
For this it might help to summarize the context in your own words.

If you can not answer the question that way, answer with "I have to use my general knowledge." 
and then answer the question using your general knowledge.

Only use your general knowledge when it is absolutely necessary.
In all other cases, try to answer the question using only the information in the context.

CONTEXT: {trans}

QUESTION: {question}""")


