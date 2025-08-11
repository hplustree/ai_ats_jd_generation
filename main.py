from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError
import uvicorn
import logging

from app.schemas.jd_input import JobDescriptionInput
from app.schemas.jd_output import JobDescriptionOutput
from app.jd_generation.jd_generator import JobDescriptionGenerator
from app.db.db_manager import DatabaseManager
from fastapi.responses import JSONResponse
from app.core.logger import logger


# Singleton instances for DB and JD generator
db = DatabaseManager()
jd_generator = JobDescriptionGenerator()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manage application lifespan events (startup and shutdown).
    """
    # Startup
    logger.info("Starting application initialization...")
    await db.ensure_table_exists()
    await jd_generator.initialize()
    logger.info("App startup complete.")
    yield
    # Shutdown
    logger.info("Application shutdown initiated.")

# Create FastAPI app with lifespan
app = FastAPI(
    title="AI Job Description Generator API",
    lifespan=lifespan
)


# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/generate-job-description/", response_model=JobDescriptionOutput)
async def generate_job_description_endpoint(input_data: JobDescriptionInput) -> JobDescriptionOutput:
    """
    Generate an AI-powered job description from structured input.
    """
    input_dict = input_data.model_dump()

    logger.info(f"Received job description generation request")

    try:
        # Check if store_db is True and validate existing records
        if input_data.store_db:
            job_id = input_data.job_id

            if await db.check_job_exists(job_id):
                raise HTTPException(
                    status_code=409, 
                    detail=f"JD is already generated for job id {job_id} ."
                )

        # Generate JD
        result = await jd_generator.generate_job_description_async(input_dict)

        # If LLM returned error
        if isinstance(result, dict) and "error" in result:
            logger.error(f"LLM error: {result['error']}")
            raise HTTPException(status_code=400, detail=result["error"])

        # Store in database if store_db is True
        if input_data.store_db:
            try:
                # Convert the Pydantic model to dict for JSON storage
                ai_jd_dict = result.model_dump()

                await db.insert_job_description(
                    job_id=input_data.job_id,
                    user_id=input_data.user_id,
                    designation=input_data.designation,
                    min_exp=str(input_data.min_experience),
                    max_exp=str(input_data.max_experience),
                    availability=input_data.availability,
                    number_of_positions=input_data.number_of_positions,
                    # location=input_data.location,
                    # domain=input_data.domain,
                    qualification=input_data.qualification,
                    technical_skills=input_data.technical_skills,
                    work_preference=input_data.work_preference,
                    sector=input_data.sector,
                    big4_experience=input_data.big4_experience,
                    travel_required=input_data.travel_required,
                    software=input_data.software,
                    ai_jd_description=ai_jd_dict
                )
            except RuntimeError as insert_err:
                logger.warning(f"DB insert failed for job id {input_data.job_id}: {insert_err}")
        # Return the modified output format
        response = {
            "job_id": input_data.job_id,
            "user_id": input_data.user_id,
            "job_description": result.model_dump()
        }

        logger.info(f"Successfully processed.")
        return JSONResponse(content=response)

    except ValidationError as ve:
        logger.error(f"Validation error: {ve.errors()}")
        raise HTTPException(status_code=422, detail=ve.errors())
    
    except RuntimeError as re:
        logger.error(f"Runtime error: {re}")
        raise HTTPException(status_code=400, detail=str(re))
    
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)