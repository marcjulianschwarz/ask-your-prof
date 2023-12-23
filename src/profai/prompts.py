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


GENERAL_CONTEXT_PROMPT = Prompt(
    """Answer the question (see QUESTION) in a concise way.

You will have access to parts of a lecture transcript (see CONTEXT) that may help you answer the question. 
Please try to answer the question using only the information in the context. 
For this it might help to summarize the context in your own words.

If you can not answer the question that way, answer with "I have to use my general knowledge." 
and then answer the question using your general knowledge.

Only use your general knowledge when it is absolutely necessary.
In all other cases, try to answer the question using only the information in the context.

CONTEXT: {trans}

QUESTION: {question}"""
)


GENERAL_CONTEXT_PROMPT_DE = Prompt(
    """Beantworten Sie die Frage (siehe FRAGE) auf eine knappe Weise.
Sie erhalten Zugang zu Teilen eines Vorlesungstranskripts (siehe KONTEXT), das Ihnen helfen könnte, die Frage zu beantworten.
Versuchen Sie bitte, die Frage ausschließlich mit den Informationen aus dem Kontext zu beantworten.
Hierfür könnte es hilfreich sein, den Kontext in Ihren eigenen Worten zusammenzufassen.
Wenn Sie die Frage auf diese Weise nicht beantworten können, antworten Sie mit "Ich muss mein Allgemeinwissen nutzen."
und beantworten Sie dann die Frage unter Verwendung Ihres Allgemeinwissens.
Nutzen Sie Ihr Allgemeinwissen nur, wenn es absolut notwendig ist.
In allen anderen Fällen versuchen Sie, die Frage ausschließlich mit den Informationen aus dem Kontext zu beantworten.

KONTEXT: {trans}

FRAGE: {question}
"""
)
