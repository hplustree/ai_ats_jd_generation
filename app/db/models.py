from sqlalchemy import Column, String, Integer, SmallInteger, Float, TIMESTAMP, Text, func
from app.db.database import Base
from app.core.config import DB_JD_TABLE_NAME


class JobDescription(Base):
    __tablename__ = DB_JD_TABLE_NAME

    # Composite primary key columns
    job_id = Column(
        Integer,
        primary_key=True,  # Part of composite primary key
        index=True,
        nullable=False,
        doc="Unique job identifier."
    )

    user_id = Column(
        Integer,
        primary_key=True,  # Part of composite primary key
        nullable=False,
        index=True,
        doc="User identifier."
    )

    domain_id = Column(
        Integer,
        index=True
    )
    level_id = Column(
        Integer,
        index=True,
        doc="Related to tag."
    )

    designation = Column(
        String(255),
        nullable=False,
        doc="Job title or designation."
    )

    domain = Column(
        String(255),
        nullable=False,
        doc="Domain or industry the job belongs to."
    )

    min_exp = Column(
        String(20),
        index=True,
        doc="Minimum years of experience required."
    )

    max_exp = Column(
        String(20),
        index=True,
        doc="Maximum years of experience allowed."
    )

    availability = Column(
        Text,
        nullable=False,
        doc="Job availability type: 1=Full-Time, 2=Part-Time, 3=Contractual, 4=Temporary, 5=Seasonal.",
        comment="1=Full-Time, 2=Part-Time, 3=Contractual, 4=Temporary, 5=Seasonal"
    )

    number_of_positions = Column(
        Integer,
        nullable=False,
        default=1,
        doc="Number of job openings."
    )

    location = Column(
        String(255),
        nullable=False,
        doc="Primary job location."
    )

    qualification = Column(
        String(255),
        doc="Minimum required educational qualification."
    )

    technical_skills = Column(
        Text,
        nullable=False,
        doc="List of technical skills required."
    )

    #New
    job_location_city_id = Column(
        Integer,
        index=True
    )

    job_location_state_id = Column(
        Integer,
        index=True,
        doc="Related to state."
    )

    job_location_country_id = Column(
        Integer,
        index=True,
        doc="Related to country."
    )

    work_preference = Column(
        Text,
        nullable=False,
        doc="Work preference: 1=Remote, 2=WFO, 3=Hybrid.",
        comment="1=Remote, 2=WFO, 3=Hybrid"
    )

    job_duration = Column(
        Float,
        nullable=True
    )

    type_of_industries = Column(
        String(255)
    )

    sector = Column(
        Integer,
        nullable=True,
        index=True,
        doc="Employment sector: 1=Public, 2=Private, 3=Both.",
        comment="1=Public, 2=Private, 3=Both"
    )

    big4_experience = Column(
        Integer,
        nullable=True,
        index=True,
        doc="Big 4 experience: 1=Yes, 2=No.",
        comment="1=Yes, 2=No"
    )

    certification_needed = Column(
        String(255),
        index=True
    )

    compansation_type = Column(
        SmallInteger,
        index=True,
        nullable=True,
        comment="1=Hourly, 2=Yearly"
    )

    travel_required = Column(
        Integer,
        nullable=True,
        index=True,
        doc="Travel requirement: 1=No, 2=Occasional, 3=Frequent.",
        comment="1=No, 2=Occasional, 3=Frequent"
    )

    software = Column(
        Text,
        nullable=True,
        doc="List of software tools used in the job."
    )

    ai_jd_description = Column(
        Text,
        nullable=True,
        doc="Generated job description from AI."
    )

    status = Column(
        SmallInteger,
        nullable=True,
        index=True,
        comment="1=Open, 2=Closed"
    )

    created_by = Column(
        Integer
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        nullable=True,
        doc="Timestamp when the record was created."
    )

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=True,
        doc="Timestamp when the record was last updated."
    )