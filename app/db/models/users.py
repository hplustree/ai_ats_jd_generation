from sqlalchemy import (
    Column,
    String,
    Integer,
    func,
    SmallInteger,
    DECIMAL,
    DateTime
)
from app.db.database import Base
from sqlalchemy.orm import relationship

from app.core.config import DB_USER_TABLE_NAME

class User(Base):
    __tablename__ = DB_USER_TABLE_NAME

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    fname = Column(String(50), nullable=False)

    lname = Column(String(50), nullable=False)

    gender = Column(Integer, doc="This id related to Tags")

    is_primary = Column(
        SmallInteger, nullable=False, index=True, default=1, comment="1-Yes, 2-No"
    )

    signup_type = Column(
        SmallInteger,
        nullable=False,
        index=True,
        default=1,
        comment="1-Website, 2-Linkedin, 3-Google",
    )

    email = Column(String(255), nullable=False)

    password = Column(String(255), nullable=False)

    linked_in_token = Column(String(255), nullable=True)

    google_token = Column(String(255), nullable=True)

    contact_number = Column(String(100))

    profile_percentage = Column(DECIMAL(5, 2))

    status = Column(
        SmallInteger,
        nullable=False,
        index=True,
        default=1,
        comment="1-Active, 2-Inactive",
    )  # Selection Field

    is_verified = Column(
        SmallInteger,
        nullable=False,
        index=True,
        default=0,
        comment="1-Verified, 0-Unverified",
    )  # Selection Field

    is_approved = Column(
        SmallInteger,
        nullable=False,
        index=True,
        default=1,
        comment="1-Pending, 2-Approved, 3-Unapproved",
    )  # Selection Field

    is_deleted = Column(
        SmallInteger,
        nullable=False,
        index=True,
        default=0,
        comment="0-Not Deleted, 1-Deleted",
    )  # Selection Field

    datetime_created = Column(DateTime(timezone=True), server_default=func.now())

    datetime_modified = Column(DateTime(timezone=True), onupdate=func.now())

    # ForeignKey
    role_id = Column(
        SmallInteger,
        # ForeignKey("roles.id"),
        nullable=False,
        index=True,
        default=1,
        comment="1-SuperAdmin, 2-CompanyAdmin, 3-Candidate",
    )

    employer_id = Column(Integer, 
                        #  ForeignKey("employers.id"),
                          index=True)

    # Relationship
    # employer = relationship(
    #     "Employer", back_populates="users", foreign_keys=[employer_id]
    # )
    # role = relationship("Role", back_populates="users", foreign_keys=[role_id])

    # user_details = relationship(
    #     "UserDetails", back_populates="user", foreign_keys="UserDetails.user_id"
    # )
    # sessions = relationship("Session", back_populates="user", foreign_keys="Session.user_id")
    jobs = relationship(
        "JobDescription", back_populates="user", foreign_keys="JobDescription.user_id"
    )
