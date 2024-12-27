import requests
from faker import Faker
from random import randint, choice
from datetime import date, timedelta

BASE_URL = "http://127.0.0.1:8000"

#добавляем раздел студент

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


#добавляем раздел инфо про студента

def add_study(group_number, scholarship, speciality, course):
    url = f"{BASE_URL}/add_study"

    params = {
        "group_number_": group_number,
        "scholarship_": scholarship if scholarship is not None else 0,
        "speciality_": speciality,
        "course_": course.isoformat()  # Convert date to string in ISO format
    }

    response = requests.post(url, params=params)
    try:
        json_response = response.json()
        if response.status_code == 200:
            print(f"Study Added")
        else:
            print(f"Failed to add study. Status code: {response.status_code}")
            print(f"Response content: {json_response}")
    except ValueError:
        print(f"Failed to parse response as JSON. Status code: {response.status_code}")
        print(f"Response content: {response.text}")

if __name__ == "main":
    fake = Faker()

    for _ in range(10):
        add_study(
            group_number=randint(101, 999),
            scholarship=randint(0, 1) * randint(100, 1000),
            speciality=fake.job(),
            course=date(randint(2010, 2023), randint(1, 28), randint(1, 12))
        )  

#создаём факультет бд 
def create_faculty(faculty_name, dean_name, faculty_capacity):
    endpoint = f"{BASE_URL}/add_faculty"
    payload = {
        "name_": faculty_name,
        "decan_": dean_name,
        "capacity_": faculty_capacity
    }
    response = requests.post(endpoint, params=payload)
    try:
        result = response.json()
        if response.status_code == 200:
            print("Faculty successfully added.")
        else:
            print(f"Error adding faculty: {response.status_code}")
            print(f"Response details: {result}")
    except ValueError:
        print(f"Error parsing response. HTTP status: {response.status_code}")
        print(f"Response text: {response.text}")

if name == "main":
    fake_gen = Faker()

    for _ in range(1):
        create_faculty(
            faculty_name=fake_gen.job(),
            dean_name=fake_gen.name(),
            faculty_capacity=randint(100, 1000)
        )
