# School Management System Backend

A RESTful backend API built with **FastAPI** for managing core school operations such as students, classes, and related academic data.  
This project is designed as a learning and portfolio project to demonstrate backend development skills using Python.

---

## Features

- Student management (create, read, update, delete)
- Structured API routing with FastAPI
- Data validation using Pydantic schemas
- Database integration using SQLAlchemy ORM
- Automatic API documentation with Swagger UI
- Clean and scalable project structure

---

## Tech Stack

- **Python**
- **FastAPI**
- **SQLAlchemy**
- **Pydantic**
- **SQLite** (for development)
- **Uvicorn**

---

## Project Structure

```bash
backend/
│
├── app/
│ ├── main.py
│ ├── database.py
│ ├── schemas.py
│ ├── models/
│ ├── venv/
│ ├── routers/
│ ├── school.db│
├── .gitignore
└── README.md
```


---

## How to Run the Project Locally

### Clone the repository
```bash
git clone https://github.com/yourusername/school-management-backend.git
cd school-management-backend
```

Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

Install dependencies
pip install FastAPi uvicorn sqlalchemy

Run the application
uvicorn app.main:app --reload

API Documentation

## Once the server is running, open your browser and visit:

Swagger UI:
http://127.0.0.1:8000/docs

ReDoc:
http://127.0.0.1:8000/redoc

## These pages allow you to test all API endpoints interactively.

### Example Endpoints
- Method	Endpoint	Description
- POST	/students	Create a new student
- GET	/students	Get all students
- GET	/students/{id}	Get a student by ID
- PUT	/students/{id}	Update a student
- DELETE	/students/{id}	Delete a student
---
## Learning Goals
### This project was built to:
- Understand REST APIs and HTTP concepts
- Practice backend architecture
- Learn database modeling with SQLAlchemy
- Apply request/response validation
- Build scalable backend systems with FastAPI

### Future Improvements
- Authentication & authorization (JWT)
- Role-based access (admin, teacher)
- Class and subject management
- Fee and payment tracking
- Unit and integration tests
- Deployment to cloud services
---
  
## Author
Charles Porker *Backend Developer (Python / FastAPI)*.
  
## License
This project is for learning and portfolio purposes.
