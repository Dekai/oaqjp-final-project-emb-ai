from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/emotionDetector", methods=['GET', 'POST'])
def emotion_detector_route():
    if request.method == 'POST':
        text = request.form.get('textToAnalyze', '')
    else:
        text = request.args.get('textToAnalyze', '')
    
    if text.strip():
        result = emotion_detector(text)
        return {
            'anger': result['anger'],
            'disgust': result['disgust'],
            'fear': result['fear'],
            'joy': result['joy'],
            'sadness': result['sadness'],
            'dominant_emotion': result['dominant_emotion']
        }
    return {'error': 'No text provided'}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
