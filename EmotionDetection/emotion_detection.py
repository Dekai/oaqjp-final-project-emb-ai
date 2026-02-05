import requests
import json

def emotion_detector(text_to_analyse):
    req_ulr = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    req_headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    req_json = { "raw_document": { "text": text_to_analyse } } 

    response = requests.post(req_ulr, headers=req_headers, json=req_json)
    response.raise_for_status()

    resq_dict = json.loads(response.text)
    # Get emotions
    emotions = resq_dict["emotionPredictions"][0]["emotion"]
    
    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]

    # get dominant_emotion
    dominant_emotion = max(
        emotions,
        key=lambda e: emotions[e]
    )

    # build response
    result = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion,
    }

    return result