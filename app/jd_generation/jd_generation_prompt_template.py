from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain_core.output_parsers import JsonOutputParser
from app.schemas.jd_output import JobDescriptionOutput
from pathlib import Path

from app.core.logger import logger


SYSTEM_PROMPT_PATH = Path("app/jd_generation/prompts/jd_system_prompt.md")
HUMAN_PROMPT_PATH = Path("app/jd_generation/prompts/jd_human_prompt.md")


class JobDescriptionPromptCreator:
    """
    Creates job description prompts using LangChain's ChatPromptTemplate,
    leveraging system and human message templates, and JSON output parsing.
    """

    def __init__(self) -> None:
        self.parser = JsonOutputParser(pydantic_object=JobDescriptionOutput)

    def _load_prompt(self, path: Path) -> str:
        """
        Safely load the prompt content from a markdown file.
        """
        try:
            prompt_file = path.read_text(encoding="utf-8")
            return prompt_file
        except Exception as e:
            logger.exception(f"Failed to load prompt file: {path}")
            raise FileNotFoundError(f"Could not read prompt from {path}: {e}") from e

    def create_job_description_prompt(self) -> ChatPromptTemplate:
        """
        Constructs a complete chat prompt using system and human templates.
        """
        try:
            system_template = self._load_prompt(SYSTEM_PROMPT_PATH)
            human_template = self._load_prompt(HUMAN_PROMPT_PATH)

            system_prompt = SystemMessagePromptTemplate.from_template(system_template)
            human_prompt = HumanMessagePromptTemplate.from_template(human_template)

            chat_prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])

            prompt_with_format = chat_prompt.partial(
                format_instructions=self.parser.get_format_instructions()
            )

            logger.info("Job description prompt template successfully created.")
            return prompt_with_format

        except Exception as e:
            logger.exception("Failed to create job description prompt.")
            raise ValueError(f"Prompt construction failed: {str(e)}") from e
