import requests
import json
import sys

def emotion_detector(text_to_analyze):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(
        url, json=input_json, headers=headers
    )

    #task2
    # if response.status_code < 300:
    #     return response.text
    # else:
    #     return ''

    #task3
    formatted_content = json.loads(response.text)
    if response.status_code < 300:
        emotion_scores = formatted_content['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        return {
            'anger': emotion_scores['anger'],
            'disgust': emotion_scores['disgust'],
            'fear': emotion_scores['fear'],
            'joy': emotion_scores['joy'],
            'sadness': emotion_scores['sadness'],
            'dominant_emotion': dominant_emotion
        }
    else:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    

if __name__ == "__main__":
    print(emotion_detector(sys.argv[1]))