import os
from transformers import pipeline
from flask import Flask, request, jsonify


app = Flask(__name__)
model_name = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
pipe = pipeline('text-classification', model=model_name)


@app.route("/")
def classify_text():
    api_key = request.args.get('api_key')
    text = request.args.get('text')
    if api_key != os.environ.get('API_KEY'):
        return jsonify({"error": "Invalid API key"})
    if not text:
        return jsonify({"error": "No text provided"})
    result = pipe(text)
    return jsonify(result)
