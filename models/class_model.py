from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String, nullable=False, unique=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=True)
    room_number = Column(String, nullable=True)
    capacity = Column(Integer, nullable=True)
    academic_year = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


    students = relationship(
        "Student",
        back_populates="class_name",
        cascade="all, delete"
    )