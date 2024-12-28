from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Date, Float
from sqlalchemy.orm import declarative_base
import subprocess
import sessions

Base = declarative_base()

#create class Student

class Student(Base):
    __tablename__ = "Students"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    Name_Surname = Column(String(150), nullable=False) 
    gpa = Column(Float, nullable=False)
    age = Column(Integer, nullable=False)
    entry_year = Column(Integer, nullable=False)
    gender = Column(String(15), nullable=False)

#create class faculty

class Faculty(Base):
    __tablename__ = "Faculty"
    
    faculty_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    decan = Column(String(20), nullable=True)
    capacity = Column(Integer, nullable=True)

#create class Study


class Study(Base):
    __tablename__ = "Study"
    
    student_id = Column(Integer, ForeignKey("Students.id"), primary_key=True, nullable=False)
    faculty_id = Column(Integer, ForeignKey("Faculty.faculty_id"), nullable=False)
    group_number = Column(Integer, nullable=False)
    scholarship = Column(Integer, nullable=True)
    speciality = Column(String(50), nullable=False)
    course = Column(Date)


Base.metadata.create_all(sessions.engine) 
