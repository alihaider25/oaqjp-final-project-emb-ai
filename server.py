"""Flask web application for emotion detection using Watson NLP."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector


app = Flask(__name__)


@app.route("/")
def home():
    """Render the home page of the emotion detection application."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze user text and return the detected emotions."""

    text_to_analyze = request.args.get("textToAnalyze")

    if text_to_analyze is None or text_to_analyze.strip() == "":
        return "Invalid input! Please enter a text to analyze."

    response = emotion_detector(text_to_analyze)

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    output = (
        "For the given statement, the system response is "
        f"'anger': {anger}, "
        f"'disgust': {disgust}, "
        f"'fear': {fear}, "
        f"'joy': {joy}, "
        f"and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return output


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)