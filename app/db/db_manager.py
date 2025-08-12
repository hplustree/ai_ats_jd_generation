import json

from typing import List

from sqlalchemy import select, MetaData
from sqlalchemy.exc import IntegrityError

from datetime import datetime
import pytz
from typing import Optional
from app.db.models import Domain 
from app.db.database import AsyncSessionLocal, engine
from app.db.models import Base, JobDescription ,User

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


    async def check_users_exists(self, user_id: int) -> bool:
        """
        Check if user_id exists in JobDescription table.
        """
        async with AsyncSessionLocal() as session:
            stmt = select(User.id).where(
                User.id == user_id
            )
            result = await session.execute(stmt)
            exists = result.scalar() is not None
            logger.debug(f"Checked user_id {user_id}: exists={exists}")
            return exists

    async def check_job_exists(self, external_job_id: int, user_id: int) -> bool:
        """
        Check if external_job_id and user_id combination already exists in JobDescription table.
        """
        async with AsyncSessionLocal() as session:
            stmt = select(JobDescription.external_job_id).where(
                JobDescription.external_job_id == external_job_id,
                JobDescription.user_id == user_id
            )
            result = await session.execute(stmt)
            exists = result.scalar() is not None
            logger.debug(f"Checked external_job_id {external_job_id} with user_id {user_id}: exists={exists}")
            return exists

    async def insert_job_description(
        self,
        external_job_id: int,
        user_id: int,
        domain_id: int, 
        designation: str,
        min_exp: str,
        max_exp: str,
        availability: List[int],
        number_of_positions: int,
        # location: str,
        qualification: str,
        technical_skills: List[str],
        work_preference: List[int],
        sector: Optional[int],
        big4_experience: Optional[int],
        travel_required: Optional[int],
        software: Optional[List[str]],
        ai_jd_description: dict
    ) -> int: 
        async with AsyncSessionLocal() as session:
            try:
                record = JobDescription(
                    external_job_id=external_job_id, 
                    user_id=user_id,
                    domain_id=domain_id,  
                    designation=designation,
                    min_exp=min_exp,
                    max_exp=max_exp,
                    availability=json.dumps(availability),
                    number_of_positions=number_of_positions,
                    # location=location,
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
                await session.refresh(record) 
                
                logger.info(f"Job description successfully inserted for external_job_id {external_job_id} and user_id {user_id}, got ID {record.id}")
                return record.id  

            except IntegrityError as ie:
                await session.rollback()
                logger.error(f"IntegrityError while inserting external_job_id {external_job_id}: {ie}", exc_info=True)
                raise RuntimeError("Integrity error during insertion.") from ie
            
            except Exception as e:
                await session.rollback()
                logger.error(f"Unexpected error while inserting external_job_id {external_job_id}: {e}", exc_info=True)
                raise RuntimeError("Unexpected error during insertion.") from e
            
    
    async def get_or_create_domain(self, domain_name: str) -> int:
        """
        Get domain_id by name, or create if doesn't exist.
        Returns the domain_id.
        """
        async with AsyncSessionLocal() as session:
            try:
                # First, try to find existing domain
                stmt = select(Domain.id).where(Domain.name == domain_name)
                result = await session.execute(stmt)
                domain_id = result.scalar()
                
                if domain_id:
                    logger.debug(f"Found existing domain '{domain_name}' with id {domain_id}")
                    return domain_id
                
                # Domain doesn't exist, create new one
                new_domain = Domain(
                    name=domain_name,
                    status=1,  # Active
                    total_used=0
                )
                session.add(new_domain)
                await session.commit()
                await session.refresh(new_domain)
                
                logger.info(f"Created new domain '{domain_name}' with id {new_domain.id}")
                return new_domain.id
                
            except Exception as e:
                await session.rollback()
                logger.error(f"Error handling domain '{domain_name}': {e}", exc_info=True)
                raise RuntimeError(f"Error handling domain: {e}") from e
