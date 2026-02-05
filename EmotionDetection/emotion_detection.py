def emotion_detector(text_to_analyse):
    if not text_to_analyse or not text_to_analyse.strip():
        # Return None values for blank input with status 400
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    
    req_ulr = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    req_headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    req_json = { "raw_document": { "text": text_to_analyse } } 

    response = requests.post(req_ulr, headers=req_headers, json=req_json)
    response.raise_for_status()

    response_dict = json.loads(response.text)
    
    emotions = response_dict["emotionPredictions"][0]["emotion"]
    
    result = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": max(emotions, key=lambda e: emotions[e])
    }

    return result
