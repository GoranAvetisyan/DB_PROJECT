
from fastapi import FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from sessions import session as db_session
import models as db_models
from sqlalchemy import DateTime
from datetime import date
from fastapi import Query
from sqlalchemy import func

app = FastAPI()

# CRUD - STUDENT TABLE

@app.post("/add_student", tags=["student"])
async def add_student(full_name: str, grade_point_average: float, student_age: int,
                      year_of_entry: int, student_gender: str):
    student_obj = db_models.Student(Name_Surname=full_name, gpa=grade_point_average, age=student_age,
                                    entry_year=year_of_entry, gender=student_gender)
    db_session.add(student_obj)
    db_session.commit()
    return f"Student Added: {student_obj.id} - {student_obj.Name_Surname}."


@app.get("/get_student/{student_id}", tags=["student"])
async def get_student(student_id: int):
    student = session_.query(models_.Student).filter(models_.Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Failed to get student by ID: Student not found.")
    return student
