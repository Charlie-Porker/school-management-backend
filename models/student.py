from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    parent_name = Column(String, nullable=False)
    parent_email = Column(String(100), nullable=False)
    parent_phone = Column(String(20), nullable=False)
    student_id = Column(String(50), nullable=False, unique=True)
    date_of_birth = Column(DateTime, nullable=False)
    date_of_admission = Column(DateTime, nullable=False)
    parent_id = Column(Integer, nullable=True)
    allergies = Column(String, nullable=True)
    media_consent = Column(Boolean, nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(20), nullable=False)
    address = Column(String, nullable=False)
    class_enrolled = Column(String, nullable=False)
    current_class = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class_id = Column(Integer, ForeignKey("classes.id"))

class_name = relationship(
    "Class",
    back_populates="students"
)