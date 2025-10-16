from sqlalchemy import Column, String, Integer, BigInteger, DateTime, func
from sqlalchemy.orm import relationship
from app.db.database import Base


class Designation(Base):
    __tablename__ = "designations"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        unique=True,
        index=True,
        nullable=False,
    )

    name = Column(String(255), nullable=False, doc="Job title or designation.")

    domain_id = Column(BigInteger, nullable=False, index=True)

    created_at = Column(DateTime, nullable=False, server_default=func.now())

    updated_at = Column(
        DateTime, nullable=False, server_default=func.now(), onupdate=func.now()
    )

    jobs = relationship(
        "JobDescription",  # Use string name
        back_populates="designation",
    )
