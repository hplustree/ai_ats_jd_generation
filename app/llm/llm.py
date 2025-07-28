from typing import Optional

from langchain_openai import AzureChatOpenAI
from app.core.config import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_VERSION,
    AZURE_DEPLOYMENT_MODEL_NAME,
)

from app.core.logger import logger

class AzureLLMClient:
    """
    Thread-safe singleton client for Azure OpenAI's Chat model with async support.
    """
    _instance: Optional[AzureChatOpenAI] = None

    @classmethod
    async def get_llm(cls) -> AzureChatOpenAI:
        """
        Initialize and return the singleton AzureChatOpenAI instance.

        Returns:
            AzureChatOpenAI: Configured instance of Azure OpenAI LLM.

        Raises:
            RuntimeError: If initialization fails or response check fails.
        """
        if cls._instance is not None:
            return cls._instance

        try:
            llm = AzureChatOpenAI(
                azure_deployment=AZURE_DEPLOYMENT_MODEL_NAME,
                azure_endpoint=AZURE_OPENAI_ENDPOINT,
                api_key=AZURE_OPENAI_API_KEY,
                api_version=AZURE_OPENAI_API_VERSION,
                temperature=0.2,
                streaming=False,
                max_retries=3,
                timeout=50.0
            )
            
            logger.info("Azure OpenAI LLM initialized successfully.")

            cls._instance = llm
            return cls._instance

        except Exception as exc:
            logger.exception("Azure OpenAI LLM initialization failed")
            cls._instance = None
            raise RuntimeError("Azure OpenAI LLM initialization failed") from exc


async def get_llm() -> AzureChatOpenAI:
    """
    Wrapper for backward compatibility with previous `get_llm` usage.

    Returns:
        AzureChatOpenAI: Initialized LLM instance.
    """
    return await AzureLLMClient.get_llm()
