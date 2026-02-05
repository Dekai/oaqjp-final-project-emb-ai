"""
Emotion Detection Flask Web Server.

This server provides a REST API endpoint /emotionDetector for text emotion analysis
using Watson NLP. Supports error handling for blank inputs and returns formatted
emotion scores with dominant emotion identification.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector


app = Flask(__name__)


@app.route("/")
def home():
    """
    Render the main index.html page for the emotion detection web app.

    Returns:
        Rendered HTML template.
    """
    return render_template('index.html')


@app.route("/emotionDetector", methods=['GET', 'POST'])
def emotion_detector_route():
    """
    REST API endpoint for emotion detection analysis.

    Accepts text input via GET (?textToAnalyze=...) or POST form data.
    Returns JSON with emotion scores, dominant emotion, and formatted response.
    Handles blank input errors with status 400.

    Returns:
        JSON: Emotion analysis results or error message.
    """
    if request.method == 'POST':
        text = request.form.get('textToAnalyze', '')
    else:
        text = request.args.get('textToAnalyze', '')

    result = emotion_detector(text)

    # Error handling for blank/invalid input
    if result['dominant_emotion'] is None:
        return jsonify({
            'processed_text': text or '',
            'response': 'Invalid text! Please try again!'
        }), 400

    # Format response as customer requested
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({
        'processed_text': text,
        'emotion_analysis': result,
        'response': response_text
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
