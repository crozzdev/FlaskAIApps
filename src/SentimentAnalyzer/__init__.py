from flask import Blueprint

bp = Blueprint("SentimentAnalyzer", __name__)

from src.SentimentAnalyzer import routes
