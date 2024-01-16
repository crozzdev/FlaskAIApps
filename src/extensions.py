from flask_sqlalchemy import SQLAlchemy
import os
import sys
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import Config


db = SQLAlchemy()


credential = AzureKeyCredential(Config.AZURE_API_KEY)
text_analytics_client = TextAnalyticsClient(
    endpoint=Config.AZURE_ENDPOINT_URI, credential=credential
)
