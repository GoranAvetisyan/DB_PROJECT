import requests
from faker import Faker
from random import randint, choice
from datetime import date, timedelta

BASE_URL = "http://127.0.0.1:8000"

def create_student(student_name, student_gpa, student_age, enrollment_year, student_gender):
    endpoint = f"{BASE_URL}/add_student"
    payload = {
        "name_srn_": student_name,
        "gpa_": student_gpa if student_gpa is not None else 0.0,
        "age_": student_age,
        "entry_year_": enrollment_year,
        "gender_": student_gender
    }
    response = requests.post(endpoint, params=payload)
    try:
        result = response.json()
        if response.status_code == 200:
            print("Student successfully added.")
        else:
            print(f"Error adding student: {response.status_code}")
            print(f"Response details: {result}")
    except ValueError:
        print(f"Error parsing response. HTTP status: {response.status_code}")
        print(f"Response text: {response.text}")

if __name__ == "__main__":
    fake_gen = Faker()

    for _ in range(10):
        create_student(
            student_name=fake_gen.name(),
            student_gpa=(randint(1, 100) / 10.0) if randint(0, 1) else None,
            student_age=randint(18, 30),
            enrollment_year=randint(2010, 2023),
            student_gender=choice(["Male", "Female"])
        )

#написать продолжение через 30-40 минут 
