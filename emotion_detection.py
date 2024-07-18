import requests # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyze): # Function - emotion_detector that takes a string input (text_to_analyze)
    # URL for the emotion detector service
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    # Set the Headers required for the HTTP request
    HEADER = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    input_json = { "raw_document": { "text": text_to_analyze } } # Create a dictionary with text to analyze
    response = requests.post(URL, json = input_json, headers = HEADER) # Send a POST request to the API with the text and headers
    return response.text # Return the response text from the API