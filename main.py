from fastapi import FastAPI
from database import engine, Base
from routers import class_router, student, teacher

# Create tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="School Management System API",
    description="API for managing students, teachers, classes, and more",
    version="1.0.0"
)

# Include routers
app.include_router(student.router)
app.include_router(teacher.router)
app.include_router(class_router.router)

# Root endpoint
@app.get("/")
def root():
    return {
        "message": "Welcome to School Management System API",
        "docs": "/docs",
        "endpoints": {
            "students": "/students",
            "teachers": "/teachers",
            "classes": "/classes"
        }
    }