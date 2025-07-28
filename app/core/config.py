import os
from dotenv import load_dotenv

load_dotenv()

# Azure OpenAI configuration
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
AZURE_DEPLOYMENT_MODEL_NAME = os.getenv("AZURE_DEPLOYMENT_MODEL_NAME")

# # Database configuration
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_JD_TABLE_NAME = os.getenv("DB_JD_TABLE_NAME")

if not all([DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_JD_TABLE_NAME]):
    raise EnvironmentError("One or more required environment variables are missing.")
