
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


@app.post("/add_study", tags=["study"])
async def add_study(group_number_: int, scholarship_: int, speciality_: str,
                      course_: date):
    obj = models_.Study(group_number = group_number_, scholarship = scholarship_, 
                        speciality = speciality_, course = course_)
    session_.add(obj)
    session_.commit()
    return f"Study Added: {obj.student_id} - {obj.speciality}"

@app.get("/get_study/{student_id}", tags=["study"])
async def get_study(student_id: int):
    study = session_.query(models_.Study).filter(models_.Study.student_id == student_id).first()
    if study is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Failed to get study by ID: Study not found.")
    return study

#CREATE STUDY TABLE(CRUD)

@app.put("/update_study/{student_id}", tags=["study"])
async def update_study(student_id_: int, new_group_number_: int, new_scholarship_: int, new_speciality_: str,
                      new_course_: date):
    if (obj := session_.query(models_.Study).filter(models_.Study.student_id == student_id_).first()) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Failed to update study")
    if new_group_number_:
        obj.group_number = new_group_number_
    if new_scholarship_:
        obj.scholarship = new_scholarship_
    if new_speciality_:
        obj.speciality = new_speciality_
    if new_course_:
        obj.course = new_course_
    session_.add(obj)
    session_.commit()
    return f"Successfully updated study for student with ID:{obj.id}."

@app.delete("/delete_study/{student_id}", tags=["study"])
async def delete_study(student_id_: int):
    if (obj := session_.query(models_.Study).filter(models_.Study.student_id == student_id_).first()) is not None:
        session_.delete(obj)
        session_.commit()
        return f"Study deleted: {obj.student_id}."
