"""Flask Application Factory Pattern. Further reading: https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy"""

from flask import Flask

from config import Config
from src.extensions import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    from src.main import bp as main_bp

    app.register_blueprint(main_bp)

    from src.SentimentAnalyzer import bp as sentiment_analyzer_bp

    app.register_blueprint(sentiment_analyzer_bp, url_prefix="/SentimentAnalyzer")

    @app.route("/test/")
    def test_page():
        return "<h1>Testing the Flask Application Factory Pattern</h1>"

    return app
