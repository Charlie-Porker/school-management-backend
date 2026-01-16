from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import SessionLocal
from models.class_model import Class
from schemas import ClassCreate

router = APIRouter(
    prefix="/classes",
    tags=["classes"]
)

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET all classes
@router.get("/")
def get_classes(db: Session = Depends(get_db)):
    """Get all classes"""
    classes = db.query(Class).all()
    return classes

# GET single class
@router.get("/{class_id}")
def get_class(class_id: int, db: Session = Depends(get_db)):
    """Get one class by ID"""
    class_obj = db.query(Class).filter(Class.id == class_id).first()
    if not class_obj:
        raise HTTPException(status_code=404, detail="Class not found")
    return class_obj

# POST - Create class
@router.post("/")
def create_class(class_data: ClassCreate, db: Session = Depends(get_db)):
    """Create a new class"""
    # Check if class name already exists
    existing_class = db.query(Class).filter(Class.class_name == class_data.class_name).first()
    if existing_class:
        raise HTTPException(status_code=400, detail="Class with this name already exists")
    
    db_class = Class(
        class_name=class_data.class_name,
        teacher_id=class_data.teacher_id,
        room_number=class_data.room_number,
        capacity=class_data.capacity,
        academic_year=class_data.academic_year
    )
    
    db.add(db_class)
    try:
        db.commit()
        db.refresh(db_class)
        return db_class
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Class already exists")

# PUT - Update class
@router.put("/{class_id}")
def update_class(class_id: int, class_data: ClassCreate, db: Session = Depends(get_db)):
    """Update a class"""
    db_class = db.query(Class).filter(Class.id == class_id).first()
    if not db_class:
        raise HTTPException(status_code=404, detail="Class not found")
    
    db_class.class_name = class_data.class_name
    db_class.teacher_id = class_data.teacher_id
    db_class.room_number = class_data.room_number
    db_class.capacity = class_data.capacity
    db_class.academic_year = class_data.academic_year
    
    try:
        db.commit()
        db.refresh(db_class)
        return db_class
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Class name already exists")

# DELETE class
@router.delete("/{class_id}")
def delete_class(class_id: int, db: Session = Depends(get_db)):
    """Delete a class"""
    db_class = db.query(Class).filter(Class.id == class_id).first()
    if not db_class:
        raise HTTPException(status_code=404, detail="Class not found")
    
    db.delete(db_class)
    db.commit()
    return {"message": f"Class {db_class.class_name} deleted successfully"}