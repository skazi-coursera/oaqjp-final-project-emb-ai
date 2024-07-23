"""
server.py
This module handles the server functionality for the application. It manages 
incoming requests, processes data, and sends appropriate responses to clients.
"""
# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created:
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detection():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the label and its 
        confidence score for the provided text.'''
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        concatenated_string = "Invalid text! Please try again!."
    else:
        concatenated_string = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f" and 'sadness': {response['sadness']}"
        f". The dominant emotion is joy.")

    return concatenated_string

@app.route("/")
def render_index_page():
    '''This function initiates the rendering of the main 
    application page over the Flask channel'''
    return render_template('index.html')

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
