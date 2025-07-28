from typing import List
from pydantic import BaseModel

class JobDescriptionOutput(BaseModel):
    job_title: str
    location: str
    availability: str
    summary: str
    roles_responsibilities: List[str]
    required_skills: List[str]
    preferred_qualifications: List[str]

    class Config:
        extra = "ignore"
