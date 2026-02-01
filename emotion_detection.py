import requests
import json

def emotion_detector(text_to_analyse):
    req_ulr = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    req_headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    req_json = { "raw_document": { "text": text_to_analyse } } 

    response = requests.post(req_ulr, headers=req_headers, json=req_json)
    response.raise_for_status()

    return response.text