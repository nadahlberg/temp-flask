import os
from transformers import pipeline
from flask import Flask
from flask import Flask, request, jsonify

app = Flask(__name__)
pipe = pipeline('text-classification')


@app.route("/")
def classify_text():
    api_key = request.args.get('api_key')
    text = request.args.get('text')
    if api_key != os.environ.get('API_KEY'):
        return jsonify({"error": "Invalid API key"}), 403
    if not text:
        return jsonify({"error": "No text provided"}), 400
    result = pipe(text)
    return jsonify(result)
