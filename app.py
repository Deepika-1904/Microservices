from fastapi import FastAPI, HTTPException
from models import Student
import repository


app = FastAPI(title="Student Marks Service")


@app.get("/")
def home():
    return {"message": "Student CRUD Microservice"}


@app.post("/students")
def create_student(student: Student):
    result = repository.create(student)

    if result is None:
        raise HTTPException(
            status_code=400,
            detail="Student with this ID already exists"
        )

    return result


@app.get("/students")
def get_students():
    return repository.get_all()


@app.get("/students/{student_id}")
def get_student(student_id: int):
    student = repository.get(student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    result = repository.update(student_id, student)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return result


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    result = repository.delete(student_id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {"message": "Student deleted successfully"}