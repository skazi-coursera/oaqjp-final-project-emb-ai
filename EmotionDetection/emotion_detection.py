
import requests # Import the requests library to handle HTTP requests
import json # Import the json library to handle json

def emotion_detector(text_to_analyze): # Function - emotion_detector that takes a string input (text_to_analyze)
    
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # URL for the emotion detector service
    HEADER = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # Set the Headers required for the HTTP request
    input_json = { "raw_document": { "text": text_to_analyze } } # Create a dictionary with text to analyze
    response = requests.post(URL, json = input_json, headers = HEADER) # Send a POST request to the API with the text and headers
    formatted_response = json.loads(response.text) # Parsing the JSON response from the API
    emotion = formatted_response['emotionPredictions'][0] # Set variable to store emotions    
    anger_score = emotion['emotion']['anger'] # Initialize variables for all emotions
    
    # Initialize variables for dominant_emotion
    dominant_score = anger_score
    dominant_emotion = "anger"

    disgust_score = emotion['emotion']['disgust']
    if disgust_score > dominant_score: # If disgust_score is greater than dominant_score, reset dominant_score & dominant_emotion
        dominant_score = disgust_score
        dominant_emotion = "disgust"

    fear_score = emotion['emotion']['fear']
    if fear_score > dominant_score: # If fear_score is greater than dominant_score, reset dominant_score & dominant_emotion
        dominant_score = fear_score
        dominant_emotion = "fear"

    joy_score = emotion['emotion']['joy']
    if joy_score > dominant_score: # If joy_score is greater than dominant_score, reset dominant_score & dominant_emotion
        dominant_score = joy_score
        dominant_emotion = "joy"

    sadness_score = emotion['emotion']['sadness']
    if sadness_score > dominant_score: # If sadness_score is greater than dominant_score, reset dominant_score & dominant_emotion
        dominant_score = sadness_score
        dominant_emotion = "sadness"

    # Return a dictionary containing emotion analysis results 
    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion}
