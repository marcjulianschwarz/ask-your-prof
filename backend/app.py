from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv("/Users/marcjulianschwarz/Mac/Code/Envs/ask-your-prof/.env")


from profai.content import TextContent, read_transcripts, TextContentType, read_all_markdown
from pathlib import Path
from profai.chains import create_chain

texts, meta_data = read_transcripts(Path("/Volumes/WD/Mac/Code/Data/fau-tv/wissenschaftstag/transcripts"))

tc = TextContent(texts, meta_data, content_type=TextContentType.VTT, name="trans", session="test")
vs = tc.vectorstore()

chain = create_chain([tc])


app = Flask(__name__)
CORS(app, resources={r"/ask": {"origins": "http://localhost:1234"}})


@app.route("/ask", methods=["GET"])
def ask():
    question = request.args.get('question')
    res = chain.invoke({
        "question": question,
    })
    res = {
        "answer": res["answer"],
        "doc_ids": [doc.metadata["doc_name"] for doc in res["trans_doc"]]
    }

    return jsonify(res)