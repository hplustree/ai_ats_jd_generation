from typing import List, Optional, Literal
from pydantic import BaseModel, Field, field_validator, model_validator


class JobDescriptionInput(BaseModel):
    """
    Input model for job description generation with validation and normalized enum mappings.
    """

    job_id: Optional[int] = Field(
        default=None, ge=1, description="Unique job identifier"
    )

    user_id: Optional[int] = Field(default=None, ge=1, description="User identifier")

    designation: str = Field(min_length=1, description="Designation for the job role")

    domain: str = Field(description="Department or domain (e.g., IT, Finance)")

    min_experience: float = Field(
        ge=0, description="Minimum years of experience required"
    )

    max_experience: float = Field(
        ge=0, description="Maximum years of experience allowed"
    )

    availability: List[Literal[1, 2, 3, 4, 5]] = Field(
        min_length=1,
        description="List of job availability options: 1=Full-Time, 2=Part-Time, 3=Contractual, 4=Temporary, 5=Seasonal",
    )

    number_of_positions: int = Field(ge=1, description="Number of openings available")

    location: str = Field(description="Job location (e.g., Remote, Mumbai)")

    qualification: List[str] = Field(
        min_length=1, description="List of minimum educational qualifications required"
    )

    technical_skills: List[str] = Field(
        min_length=1, description="List of required technical skills"
    )

    work_preference: List[Literal[1, 2, 3]] = Field(
        min_length=1,
        description="List of preferred work modes: 1=Remote, 2=WFO, 3=Hybrid",
    )

    sector: Optional[Literal[1, 2, 3]] = Field(
        default=None, description="Employment sector: 1=Public, 2=Private, 3=Both"
    )

    software: Optional[List[str]] = Field(
        default=None, description="List of required software tools"
    )

    big4_experience: Optional[Literal[1, 2]] = Field(
        default=None, description="Big 4 experience: 1=Yes, 2=No"
    )

    travel_required: Optional[Literal[1, 2, 3]] = Field(
        default=None, description="Travel requirement: 1=No, 2=Occasional, 3=Frequent"
    )
    additional_info: Optional[str] = Field(
        default=None,
        description="Additional information or special requirements for the job",
    )

    store_db: bool = Field(description="Whether to store data in the database")

    # Validators

    @model_validator(mode="after")
    def validate_store_db_requirements(self):
        """Ensure job_id and user_id are present if store_db is True"""
        if self.store_db:
            if self.user_id is None:
                raise ValueError("user_id is required when store_db is True.")
        return self

    @field_validator("max_experience")
    @classmethod
    def validate_experience_range(cls, max_exp, info):
        """Ensure max_experience >= min_experience"""
        min_exp = info.data.get("min_experience")
        if min_exp is not None and max_exp < min_exp:
            raise ValueError(
                "Maximum experience cannot be less than minimum experience."
            )
        return max_exp

    @field_validator("technical_skills")
    @classmethod
    def validate_technical_skills(cls, v):
        """Ensure technical_skills list is not empty or whitespace"""
        if not v or not all(skill.strip() for skill in v):
            raise ValueError("Technical skills must not be empty.")
        return v

    # NEW VALIDATOR for qualification
    @field_validator("qualification")
    @classmethod
    def validate_qualifications(cls, v):
        """Ensure qualifications list is not empty or whitespace"""
        if not v or not all(qual.strip() for qual in v):
            raise ValueError("Qualifications must not be empty.")
        return v
