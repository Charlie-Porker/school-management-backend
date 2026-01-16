from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import SessionLocal
from models.teacher import Teacher
from schemas import TeacherCreate

router = APIRouter(
    prefix="/teachers",
    tags=["teachers"]
)

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET all teachers
@router.get("/")
def get_teachers(db: Session = Depends(get_db)):
    """Get all teachers"""
    teachers = db.query(Teacher).all()
    return teachers

# GET single teacher
@router.get("/{teacher_id}")
def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    """Get one teacher by ID"""
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

# POST - Create teacher
@router.post("/")
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    """Create a new teacher"""
    existing_teacher = db.query(Teacher).filter(Teacher.email == teacher.email).first()
    if existing_teacher:
        raise HTTPException(status_code=400, detail="Teacher with this email already exists")
    
    existing_teacher_id = db.query(Teacher).filter(Teacher.teacher_id == teacher.teacher_id).first()
    if existing_teacher_id:
        raise HTTPException(status_code=400, detail="Teacher with this ID already exists")
    
    db_teacher = Teacher(
    first_name=teacher.first_name,
    last_name=teacher.last_name,
    email=teacher.email,
    phone=teacher.phone,
    grade=teacher.grade,
    emergency_contact=teacher.emergency_contact,
    relationship=teacher.relationship,
    address=teacher.address,
    date_of_joining=teacher.date_of_joining,
    teacher_id=teacher.teacher_id
)
    
    db.add(db_teacher)
    try:
        db.commit()
        db.refresh(db_teacher)
        return db_teacher
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Teacher already exists")

# PUT - Update teacher
@router.put("/{teacher_id}")
def update_teacher(teacher_id: int, teacher: TeacherCreate, db: Session = Depends(get_db)):
    """Update a teacher"""
    db_teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not db_teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    
    db_teacher.first_name = teacher.first_name
    db_teacher.last_name = teacher.last_name
    db_teacher.email = teacher.email
    db_teacher.phone = teacher.phone
    db_teacher.grade = teacher.grade
    db_teacher.emergency_contact = teacher.emergency_contact
    db_teacher.relationship = teacher.relationship
    db_teacher.date_of_joining = teacher.date_of_joining
    db_teacher.address = teacher.address
    db_teacher.teacher_id = teacher.teacher_id
    
    try:
        db.commit()
        db.refresh(db_teacher)
        return db_teacher
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email or teacher ID already exists")

# DELETE teacher
@router.delete("/{teacher_id}")
def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    """Delete a teacher"""
    db_teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not db_teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    
    db.delete(db_teacher)
    db.commit()
    return {"message": f"Teacher {db_teacher.first_name} {db_teacher.last_name} deleted successfully"}