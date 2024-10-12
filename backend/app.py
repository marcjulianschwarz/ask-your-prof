import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

load_dotenv()

from pathlib import Path

from profai.chains import create_chain
from profai.content import MarkdownContent, VTTContent

tc = VTTContent.from_path(Path(os.environ["TRANSCRIPT_PATH"]), "trans")
chain = create_chain([tc])

app = Flask(__name__)
# CORS(app, resources={r"/ask": {"origins": "http://localhost:1234"}})
CORS(app, resources={r"/ask": {"origins": "http://localhost:5173"}})


# @app.route("/ask", methods=["GET"])
# def ask():
#     question = request.args.get("question")
#     res = chain.invoke(
#         {
#             "question": question,
#         }
#     )
#     res = {
#         "answer": res["answer"],
#         "docs": [
#             {
#                 "content": doc.page_content,
#                 "id": doc.metadata["doc_name"],
#             }
#             for doc in res["trans_doc"]
#         ],
#     }

#     return jsonify(res)


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data["question"]
    prompt = data["prompt"]
    res = chain.invoke(
        {
            "question": question,
            "prompt": prompt,
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


@app.route("/video", methods=["GET"])
def video():
    doc_id = request.args.get("doc_id")
    return send_from_directory(os.environ["VIDEO_PATH"], doc_id + ".m4v")
