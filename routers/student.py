from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import SessionLocal
from models.student import Student
from schemas import StudentCreate, StudentResponse, StudentUpdate
from typing import List

router = APIRouter(
    prefix="/students",
    tags=["students"]
)

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET all students
@router.get("/", response_model=List[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()


# GET single student
@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


# POST - Create student
@router.post("/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# PUT - Update student
@router.put("/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student: StudentUpdate,
    db: Session = Depends(get_db)
):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")

    for key, value in student.model_dump(exclude_unset=True).items():
        setattr(db_student, key, value)

    db.commit()
    db.refresh(db_student)
    return db_student



# DELETE student
@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    """Delete a student"""
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail=f"Student with ID {student_id} not found")
    
    db.delete(db_student)
    db.commit()
    return {"message": f"Student {db_student.first_name} {db_student.last_name} deleted successfully"}

