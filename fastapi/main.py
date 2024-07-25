from fastapi import FastAPI, Path, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# Create a dictionary to hold student information
students = {
    1: {
        "name": "john",
        "age": 17,
        "year": "year_12"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

@app.get("/")
def index():
    return {"name": "first name yohannes"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student you want to view", gt=0)):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]

# Query parameter
@app.get("/get-by-name")
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    for i in students:
        if students[i]["name"] == name:
            return students[i]
    return {"Data": "Not Found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        raise HTTPException(status_code=400, detail="Student already exists")
    students[student_id] = Student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in students:
        raise HTTPException(status_code=400,detail="Student must in exits")
    students[student_id]=Student
    return students[student_id]