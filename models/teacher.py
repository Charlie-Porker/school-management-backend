from doctest import FAIL_FAST
from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
from datetime import datetime

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(20), nullable=False)
    grade = Column(String, nullable=False)
    emergency_contact = Column(String(20), nullable=True)
    relationship = Column(String, nullable=True)
    address = Column(String, nullable=False)
    date_of_joining = Column(DateTime, nullable=False)
    teacher_id = Column(String(20), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    