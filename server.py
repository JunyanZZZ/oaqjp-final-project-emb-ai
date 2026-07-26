"""
Run text analyzer on localhost 5000
"""
from flask import Flask, request, render_template
from EmotionDetection import emotion_detection
app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector():
    """
    Analyze the given text from the input
    """
    text = request.args.get('textToAnalyze')
    response = emotion_detection.emotion_detector(text)
    dominant_emo = response.get('dominant_emotion')
    if dominant_emo is None:
        return 'Invalid text! Please try again!'

    return (f"For the given statement, the system response is "
           f"'anger': {response['anger']}, "
           f"'disgust': {response['disgust']}, "
           f"'fear': {response['fear']}, "
           f"'joy': {response['joy']}, "
           f"'sadness': {response['sadness']}, "
           f"The dominant emotion is {dominant_emo}.")


@app.route('/')
def render():
    """
    Render home page
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
