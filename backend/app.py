from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS

load_dotenv("/Users/marcjulianschwarz/Mac/Code/Envs/ask-your-prof/.env")

from pathlib import Path

from profai.chains import create_chain
from profai.content import MarkdownContent, VTTContent

tc = VTTContent.from_path(Path("/Volumes/WD/Mac/Code/Data/georg/transcripts"), "trans")
chain = create_chain([tc])

app = Flask(__name__)
# CORS(app, resources={r"/ask": {"origins": "http://localhost:1234"}})
CORS(app, resources={r"/ask": {"origins": "http://localhost:5173"}})


@app.route("/ask", methods=["GET"])
def ask():
    question = request.args.get("question")
    res = chain.invoke(
        {
            "question": question,
        }
    )
    res = {
        "answer": res["answer"],
        "docs": [
            {
                "content": doc.page_content,
                "id": doc.metadata["doc_name"],
            }
            for doc in res["trans_doc"]
        ],
    }

    return jsonify(res)
