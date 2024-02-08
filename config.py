import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    AI_ENGINE = os.getenv("AI_ENGINE")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI") or "sqlite:///" + os.path.join(
        basedir, "app.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    AZURE_API_KEY = os.getenv("AZURE_API_KEY")
    AZURE_ENDPOINT_URI = os.getenv("AZURE_ENDPOINT_URI")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
