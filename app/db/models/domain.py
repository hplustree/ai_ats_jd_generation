from math import fabs
from sqlalchemy import (
    Column,
    String,
    Integer,
    func,
    ForeignKey,
    BigInteger,
    DateTime,
    SmallInteger,
)
from app.db.database import Base
from sqlalchemy.orm import relationship

from app.core.config import DB_DOMAIN_TABLE_NAME


class Domain(Base):
    __tablename__ = DB_DOMAIN_TABLE_NAME

    id = Column(
        BigInteger, primary_key=True, autoincrement=True, index=True, nullable=False
    )
    name = Column(String(155), nullable=False, index=True)
    status = Column(
        SmallInteger, nullable=False, default=1, comment="1-Active,2-Inactive"
    )
    total_used = Column(Integer, nullable=False, default=0)
    created_at = Column(
        DateTime(timezone=True), nullable=True, server_default=func.now()
    )
    updated_at = Column(
        DateTime(timezone=True),
        nullable=True,
        server_default=func.now(),
        onupdate=func.now(),
    )

    def __repr__(self):
        return f"<Domain(id={self.id}, name='{self.name}', status={self.status})>"

    # Relationships
    # technical_softwares = relationship("TechnicalSoftware", back_populates="domain", foreign_keys="TechnicalSoftware.domain_id")
    # technical_skills = relationship("TechnicalSkill", back_populates="domain", foreign_keys="TechnicalSkill.domain_id")
    jobs = relationship(
        "JobDescription",
        back_populates="domain",
        foreign_keys="JobDescription.domain_id",
    )
