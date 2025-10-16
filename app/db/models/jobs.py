from math import fabs
from sqlalchemy import (
    Column,
    DateTime,
    String,
    Integer,
    TIMESTAMP,
    Text,
    func,
    ForeignKey,
    BigInteger,
    Float,
    SmallInteger,
)
from app.db.database import Base
from sqlalchemy.orm import relationship

from app.core.config import DB_JD_TABLE_NAME


class JobDescription(Base):
    __tablename__ = DB_JD_TABLE_NAME

    # Composite primary key columns
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        unique=True,
        index=True,
        nullable=False,
    )

    external_job_id = Column(Integer, index=True, default=None, nullable=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True,
        doc="User identifier.",
    )

    domain_id = Column(BigInteger, ForeignKey("domains.id"), index=True)

    designation_id = Column(
        Integer,
        ForeignKey("designations.id"),
        nullable=False,
        doc="Job title or designation.",
    )

    min_exp = Column(
        String(20), index=True, doc="Minimum years of experience required."
    )

    max_exp = Column(String(20), index=True, doc="Maximum years of experience allowed.")

    availability = Column(
        Text,
        nullable=False,
        doc="Job availability type: 1=Full-Time, 2=Part-Time, 3=Contractual, 4=Temporary, 5=Seasonal.",
        comment="1=Full-Time, 2=Part-Time, 3=Contractual, 4=Temporary, 5=Seasonal",
    )

    number_of_positions = Column(
        Integer, nullable=False, default=1, doc="Number of job openings."
    )

    qualification = Column(
        String(255), doc="Minimum required educational qualification."
    )

    technical_skills = Column(
        Text, nullable=False, doc="List of technical skills required."
    )

    job_location_city_id = Column(
        Integer,
        # ForeignKey("cities.id"),
        index=True,
    )

    job_location_state_id = Column(
        Integer,
        # ForeignKey("states.id"),
        index=True,
    )

    job_location_country_id = Column(
        Integer,
        # ForeignKey("countries.id"),
        index=True,
    )

    work_preference = Column(
        Text,
        nullable=False,
        doc="Work preference: 1=Remote, 2=WFO, 3=Hybrid.",
        comment="1=Remote, 2=WFO, 3=Hybrid",
    )

    sector = Column(
        Integer,
        nullable=False,
        index=True,
        doc="Employment sector: 1=Public, 2=Private, 3=Both.",
        comment="1=Public, 2=Private, 3=Both",
        default=3,
    )

    big4_experience = Column(
        Integer,
        nullable=True,
        index=True,
        doc="Big 4 experience: 1=Yes, 2=No.",
        comment="1=Yes, 2=No",
    )

    certification_needed = Column(String(255), index=True)

    compensation_type = Column(SmallInteger, index=True, comment="1=Hourly, 2=Yearly")

    travel_required = Column(
        Integer,
        index=True,
        doc="Travel requirement: 1=No, 2=Occasional, 3=Frequent.",
        comment="1=No, 2=Occasional, 3=Frequent",
    )

    software = Column(
        Text, nullable=False, doc="List of software tools used in the job."
    )

    ai_jd_description = Column(Text, doc="Generated job description from AI.")

    status = Column(SmallInteger, index=True, comment="1=Open, 2=Closed")

    # Weightages
    certification_weightage = Column(
        Float,
        nullable=False,
        default=0.10,
    )

    education_weightage = Column(
        Float,
        nullable=False,
        default=0.10,
    )

    experience_weightage = Column(
        Float,
        nullable=False,
        default=0.25,
    )

    roles_responsibility_weightage = Column(
        Float,
        nullable=False,
        default=0.25,
        doc="Weight for roles and responsibility matching (default: 0.25)",
    )

    project_weightage = Column(
        Float,
        nullable=False,
        default=0.00,
    )

    skill_weightage = Column(
        Float,
        nullable=False,
        default=0.30,
    )

    is_deleted = Column(Integer, nullable=False, default=0, comment="1=True, 0=False")

    created_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        nullable=True,
        doc="Timestamp when the record was created.",
    )

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=True,
        doc="Timestamp when the record was last updated.",
    )

    deleted_at = Column(DateTime(timezone=True), nullable=True, server_default=None)

    # Relationships
    user = relationship("User", back_populates="jobs", foreign_keys=[user_id])
    domain = relationship("Domain", back_populates="jobs", foreign_keys=[domain_id])
    designation = relationship("Designation", back_populates="jobs", foreign_keys=[designation_id])
