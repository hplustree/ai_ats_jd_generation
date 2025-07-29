import json

from typing import List

from sqlalchemy import select, MetaData
from sqlalchemy.exc import IntegrityError

from datetime import datetime
import pytz
from typing import Optional

from app.db.database import AsyncSessionLocal, engine
from app.db.models import Base, JobDescription

from app.core.logger import logger

ist = pytz.timezone("Asia/Kolkata")
current_ist_time = datetime.now(ist)

metadata = MetaData()


class DatabaseManager:
    """
    Handles all asynchronous DB operations for job descriptions.
    """

    async def ensure_table_exists(self) -> None:
        """
        Create tables if they don't exist.
        Should be called once on application startup.
        """
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("All tables verified/created.")

    async def check_job_exists(self, job_id: int, user_id: str) -> bool:
        """
        Check if job_id and user_id combination already exists in JobDescription table.
        """
        async with AsyncSessionLocal() as session:
            stmt = select(JobDescription.job_id).where(
                JobDescription.job_id == job_id,
                JobDescription.user_id == user_id
            )
            result = await session.execute(stmt)
            exists = result.scalar() is not None
            logger.debug(f"Checked job_id {job_id} with user_id {user_id}: exists={exists}")
            return exists

    async def insert_job_description(
        self,
        job_id: int,
        user_id: str,
        designation: str,
        min_exp: str,
        max_exp: str,
        availability: List[int],
        number_of_positions: int,
        location: str,
        domain: str,
        qualification: str,
        technical_skills: List[str],
        work_preference: List[int],
        sector: Optional[int],
        big4_experience: Optional[int],
        travel_required: Optional[int],
        software: Optional[List[str]],
        ai_jd_description: dict
    ) -> None:
        async with AsyncSessionLocal() as session:
            try:
                record = JobDescription(
                    job_id=job_id,
                    user_id=user_id,
                    designation=designation,
                    min_exp=min_exp,
                    max_exp=max_exp,
                    availability=json.dumps(availability),
                    number_of_positions=number_of_positions,
                    location=location,
                    domain=domain,
                    qualification=qualification,
                    technical_skills=json.dumps(technical_skills) if technical_skills else None,
                    work_preference=json.dumps(work_preference),
                    sector=sector,
                    big4_experience=big4_experience,
                    travel_required=travel_required,
                    software=json.dumps(software) if software else None,
                    ai_jd_description=json.dumps(ai_jd_description) if ai_jd_description else None,
                )
                session.add(record)
                await session.commit()
                logger.info(f"Job description successfully inserted for job_id {job_id} and user_id {user_id}")

            except IntegrityError as ie:
                await session.rollback()
                logger.error(f"IntegrityError while inserting job_id {job_id}: {ie}", exc_info=True)
                raise RuntimeError("Integrity error during insertion.") from ie
            
            except Exception as e:
                await session.rollback()
                logger.error(f"Unexpected error while inserting job_id {job_id}: {e}", exc_info=True)
                raise RuntimeError("Unexpected error during insertion.") from e
