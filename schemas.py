from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    age: int
    gender: str
    parent_name: str
    parent_email: EmailStr
    parent_phone: str
    student_id: str
    date_of_birth: datetime
    date_of_admission: datetime
    parent_id: Optional[int] = None
    allergies: Optional[str] = None
    media_consent: bool
    email: EmailStr
    phone: str
    address: str
    class_enrolled: str
    current_class: str


class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    parent_name: Optional[str] = None
    parent_email: Optional[EmailStr] = None
    parent_phone: Optional[str] = None
    student_id: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    date_of_admission: Optional[datetime] = None
    parent_id: Optional[int] = None
    allergies: Optional[str] = None
    media_consent: Optional[bool] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    class_enrolled: Optional[str] = None
    current_class: Optional[str] = None



class StudentResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int
    gender: str
    class_enrolled: str
    current_class: str

    class Config:
        from_attributes = True

class TeacherCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    grade: str
    emergency_contact: str
    relationship: str
    address: str
    date_of_joining: datetime
    teacher_id: str
    
class TeacherResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    grade: str

    class Config:
        from_attributes = True


class ClassCreate(BaseModel):
    class_name: str
    teacher_id: Optional[int] = None
    room_number: Optional[int] = None
    capacity: Optional[int] = None
    academic_year: str

class ClassResponse(BaseModel):
    id: int
    class_name: str
    teacher_id: int
    room_number: int
    capacity: int
    academic_year: str

    class Config:
        from_attributes = True