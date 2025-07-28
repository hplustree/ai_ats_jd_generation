from typing import Any, Dict, Union
from pydantic import ValidationError

from app.llm.llm import get_llm
from app.schemas.jd_input import JobDescriptionInput
from app.schemas.jd_output import JobDescriptionOutput
from app.jd_generation.jd_generation_prompt_template import JobDescriptionPromptCreator
from app.jd_generation.jd_formatter import format_job_input_data
from app.utils.retry_logic import async_retry


from app.core.logger import logger

class JobDescriptionGenerator:
    """Handles the complete job description generation pipeline."""

    def __init__(self) -> None:
        self.prompt_template = JobDescriptionPromptCreator()
        self.llm = None
        self._initialized = False

    async def initialize(self) -> None:
        """
        Initialize async components if not already initialized.
        Prevents reinitialization.
        """
        if self._initialized:
            return

        try:
            self.llm = await get_llm()
            self._initialized = True
            logger.info("JobDescriptionGenerator successfully initialized.")
        except Exception as exc:
            logger.exception("Initialization failed for JobDescriptionGenerator.")
            raise RuntimeError("Failed to initialize required components.") from exc

    @async_retry(max_attempts=3, logger_prefix="JobDescriptionGenerator")
    async def _generate_job_description(
        self, input_data: Dict[str, Any]
    ) -> JobDescriptionOutput:
        """
        Generate job description asynchronously.

        Raises:
            RuntimeError: If not initialized or generation fails.
        """
        if not self._initialized:
            raise RuntimeError("Call `await initialize()` before generating.")

        try:
            prompt_chain = (
                self.prompt_template.create_job_description_prompt()
                | self.llm
                | self.prompt_template.parser
            )
            logger.info("Generating job description...")
            # print(f"Input data: \n {input_data}")  # Debugging line
            raw_result = await prompt_chain.ainvoke(input_data)
            jd_output = JobDescriptionOutput(**raw_result)
            logger.info("Job description generated and validated.")
            return jd_output

        except ValidationError as exc:
            logger.error("Parsing error: %s", exc)
            raise RuntimeError("Invalid output structure from LLM.") from exc
        
        except ValueError as exc:
            logger.error("Invalid LLM result: %s", exc)
            raise RuntimeError("Invalid job description result.") from exc

        except Exception as exc:
            logger.error("Error generating job description: %s", exc, exc_info=True)
            raise RuntimeError("Job description generation failed due to internal error.") from exc

    async def generate_job_description_async(
        self, 
        input_data: dict
    ) -> Union[JobDescriptionOutput, dict]:
        
        """
        Full async pipeline: validate input, generate job description, store results.

        Returns:
            dict: Job description output or error message.
        """
        try:
            if not self._initialized:
                await self.initialize()

            if not isinstance(input_data, dict):
                raise ValueError("Input must be a dictionary.")

            validated_input = JobDescriptionInput(**input_data)
            formatted_input = await format_job_input_data(validated_input)
            output = await self._generate_job_description(formatted_input)

            return output

        except ValidationError as e:
            logger.error("Input schema validation failed: %s", e)
            return {
                "error": "Validation failed. Ensure all required fields are correctly filled.",
                "details": e.errors()
            }
        
        except ValueError as e:
            logger.error(f"Input validation error: {e}")
            return {"error": f"Input validation error: {str(e)}. Please correct the input data."}
        
        except RuntimeError as e:
            logger.error(f"Runtime error: {e}")
            return {"error": str(e)}
        
        except Exception as e:
            logger.exception("Unexpected failure in generation pipeline.")
            return {"error": f"Unexpected error occurred: {str(e)}"}