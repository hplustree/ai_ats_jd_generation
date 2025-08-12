# AI ATS JD Generation

This project automates the generation of Job Descriptions (JD) using AI. It is organized into modular components for configuration, database management, prompt engineering, LLM integration, and utility functions.

## Project Structure

```
.
├── Dockerfile
├── main.py
├── requirements.txt
├── readme.md
├── app/
│   ├── core/
│   │   ├── config.py         # Configuration management
│   │   ├── logger.py         # Logging setup
│   ├── db/
│   │   ├── database.py       # Database connection and setup
│   │   ├── db_manager.py     # Database operations/ORM
│   │   ├── models.py         # Database models/schemas
│   ├── jd_generation/
│   │   ├── jd_formatter.py   # Formatting generated JDs
│   │   ├── jd_generation_prompt_template.py # Prompt templates for JD generation
│   │   ├── jd_generator.py   # Core JD generation logic
│   │   └── prompts/          # Prompt files (Markdown)
│   ├── llm/
│   │   ├── llm.py            # LLM (Large Language Model) integration
│   ├── schemas/
│   │   ├── jd_input.py       # Input data schemas
│   │   ├── jd_output.py      # Output data schemas
│   ├── utils/
│   │   ├── retry_logic.py    # Utility for retrying operations
│   └── __pycache__/          # Python bytecode cache
├── logs/
│   └── app.log               # Application logs
```

## Main Components

- **main.py**: Entry point for the application.
- **Dockerfile**: Containerization setup for deployment.
- **requirements.txt**: Python dependencies.
- **app/core/**: Handles configuration and logging.
- **app/db/**: Manages database connections, models, and operations.
- **app/jd_generation/**: Contains the logic and templates for generating and formatting job descriptions.
- **app/llm/**: Integrates with LLMs for text generation.
- **app/schemas/**: Defines input and output data schemas.
- **app/utils/**: Utility functions (e.g., retry logic).
- **logs/**: Stores application logs.

## Getting Started

1. **Install dependencies:**
	```sh
	pip install -r requirements.txt
	```
2. **Run the application:**
	```sh
	python main.py
	```
3. **(Optional) Run in Docker:**
	```sh
	docker build -t ai-ats-jd-generation .
	docker run -it --rm ai-ats-jd-generation
	```

## Notes
- Update configuration in `app/core/config.py` as needed.
- Prompts for JD generation are in `app/jd_generation/prompts/`.
- Logs are written to `logs/app.log`.