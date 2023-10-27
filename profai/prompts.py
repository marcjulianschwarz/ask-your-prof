from langchain.prompts import ChatPromptTemplate

ANSWER_WITH_CONTEXT = """Answer the question in a concise way.
You will have access to parts of a lecture transcript (see CONTEXT) that may help you answer the question. 
Please try to answer the question using only the information in the context. For this it might help to summarize the context in your own words.
If you can not answer the question that way, answer with "I have to use my general knowledge." and then answer the question using your general knowledge.
Only use your general knowledge when it is absolutely necessary. In all other cases, try to answer the question using only the information in the context.

CONTEXT: {context}

QUESTION: {question}
"""


ANSWER_WITH_TRANSCRIPT_AND_SLIDES = """
A student asks you a question about the lecture (see QUESTION).

Your task will be to answer the question in a concise but complete way using parts of the lectures transcript and slides.
The transcript is provided after TRANSCRIPT and the slides are provided after SLIDES.
Please try to answer the question using only the information from the transcript and the slides. 

You should always state the sources for your answer at the end.
The sources can be from the transcript, the slides or even both.
When one of the sources is from the transcript, add the document name and timestamp.
When one of the sources is from the slides, add only the document name.
The document name and timestamps are provided in the transcript and slides.

Provide LaTeX euqations when they are present in the slides or transcript. Use the double dollar sign ($$) to start and end a LaTeX equation.

If you can not answer the question in the way described before, answer with "I have to use my general knowledge." and then answer the question using your general knowledge.

TRANSCRIPT: {transcript}

SLIDES: {slides}

QUESTION: {question}
"""


ANSWER_WITH_CONTEXT_TEMPLATE = ChatPromptTemplate.from_template(ANSWER_WITH_CONTEXT)
ANSWER_WITH_TRANSCRIPT_AND_SLIDES_TEMPLATE = ChatPromptTemplate.from_template(
    ANSWER_WITH_TRANSCRIPT_AND_SLIDES
)
