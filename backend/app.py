from pathlib import Path

from flask import Flask, jsonify, request

from profai.core import Prof

prof = Prof(
    Path("/Users/marcjulianschwarz/Mac/Code/Data/fau_tv/wissenschaftstag/videos"),
    Path("/Users/marcjulianschwarz/Mac/Code/Data/fau_tv/wissenschaftstag/transcripts"),
    Path(""),
    Path("/Users/marcjulianschwarz/Mac/Code/GitHub/ask-your-prof/vectorstores"),
)

prof.transcript_mode(transcript_name="wissenschaftstag_transcript")

app = Flask(__name__)


@app.route("/ask/<question>", methods=["GET"])
def ask(question):
    res = prof.ask(question)
    return jsonify({"answer": res.answer})
