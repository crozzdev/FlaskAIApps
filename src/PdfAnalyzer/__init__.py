from flask import Blueprint

bp = Blueprint("PdfAnalyzer", __name__)

from src.PdfAnalyzer import routes