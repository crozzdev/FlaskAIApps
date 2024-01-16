from flask import render_template, request
from src.SentimentAnalyzer import bp
from src.extensions import db, text_analytics_client
from src.models.process import Process


@bp.route("/")
def index():
    return render_template("SentimentAnalyzer/index.html")


@bp.route("/analyze", methods=["POST"])
def sentiment_analyzer():
    documents = []
    text = request.form["text"]
    documents.append(text)
    sentiment = text_analytics_client.analyze_sentiment(
        documents, show_opinion_mining=True
    )[0]["sentiment"]
    new_process = Process(text=text, sentiment=str(sentiment))
    db.session.add(new_process)
    db.session.commit()
    return render_template("SentimentAnalyzer/index.html", sentiment=sentiment)
