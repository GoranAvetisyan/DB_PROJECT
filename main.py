
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



@app.get("/get_all_students", tags=["student"])
async def get_all_students(skip: int = 0, limit: int = 100):
    students_query = session_.query(models_.Student).offset(skip).limit(limit)
    return students_query.all()

@app.put("/update_student/{student_id}", tags=["student"])
async def update_studnet(student_id_: int, new_name_srn_: str, new_gpa_: float, new_age_: int, new_entry_year: int, gender_: str = ""):
    if (obj := session_.query(models_.Student).filter(models_.Student.id == student_id_).first()) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Failed to update student: No student with such ID.")
    if new_name_srn_:
        obj.Name_Surname = new_name_srn_
    if new_gpa_:
        obj.gpa = new_gpa_
    if new_age_:
        obj.age = new_age_
    if new_entry_year:
        obj.entry_year = new_entry_year
    if gender_:
        obj.gender = gender_
    session_.add(obj)
    session_.commit()
    return f"Successfully updated student with ID:{obj.id}."

@app.delete("/delete_student/{student_id}", tags=["student"])
async def delete_student(student_id_: int):
    if (obj := session_.query(models_.Student).filter(models_.Student.id == student_id_).first()) is not None:
        session_.delete(obj)
        session_.commit()
        
        return f"Student deleted: {obj.id} - {obj.Name_Surname}."
