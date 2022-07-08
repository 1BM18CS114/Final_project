from flask import Flask, request, jsonify

import requests

import preprocessing_truth_detection
import preprosessing_summary
import models

from misc import summarize_passage, detect_truth




app = Flask(__name__)

@app.route('/sum', methods=['GET'])
def get_summary():

    # Gets the request from URL
    text = str(request.args['query'])

    # Get the Text Preprocessed so the model can accept it and predict the output
    txt = preprosessing_summary.text_clean(text)

    # Load the model and get the Prediction/Output
    sumarize_passage = models.load_model_summarization(txt)

    # Summarizing the text
    return summarize_passage(text)
    

@app.route('/truth', methods=['GET'])
def get_true_or_false():

    # Gets the request from URL
    text = str(request.args['query'])

    # Get the Text Preprocessed so the model can accept it and predict the output
    txt = preprocessing_truth_detection.cleaning(text)

    # Load the model and get the Prediction/Output
    detct_truth = models.load_model_truth_detection(txt)

    # Get the Truth or False Prediction
    return detect_truth(text)

if __name__ == "__main__":
    app.run()
