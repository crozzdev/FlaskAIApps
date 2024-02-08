from flask_sqlalchemy import SQLAlchemy
import os
import sys
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
import openai
from langchain_openai import ChatOpenAI

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import Config


db = SQLAlchemy()


## Azure AI Text Analytics client setup
credential = AzureKeyCredential(Config.AZURE_API_KEY)
text_analytics_client = TextAnalyticsClient(
    endpoint=Config.AZURE_ENDPOINT_URI, credential=credential
)

# Langchain OPEN AI client setup
if Config.AI_ENGINE == "openai":
    openai.api_key = Config.OPENAI_API_KEY
    llm_name = "gpt-3.5-turbo"
    llm_agent = ChatOpenAI(model_name=llm_name, temperature=0)

