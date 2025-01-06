# DB_PROJECT



This repository hosts a FastAPI application integrated with SQLAlchemy to manage a PostgreSQL database. The project supports CRUD (Create, Read, Update, Delete) operations for three main entities: Student, Study, and Faculty. Additionally, it offers endpoints to perform complex queries and aggregations.


Installation

Clone the repository:
git clone https://github.com/your_username/db_project.git
cd db_project

Install dependencies:
pip install -r requirements.txt

Set up the PostgreSQL database:
Open the db_creation.py file and update the database connection parameters (user, password, host, port) to match your configuration.

Run the script to create the database:
python db_creation.py

Start the FastAPI server:
uvicorn main:app --reload
Once the server is running, it will be available at http://127.0.0.1:8000.

API documentation can be accessed at:
http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc.

Usage
The API allows you to perform CRUD operations for Students, Studies, and Faculties, as well as execute advanced queries such as filtering, joining, updating with conditions, and aggregations.

Example API Endpoints

Add a student:
POST /add_student

Get all students:
GET /get_all_students

Update a student:
PUT /update_student/{student_id}

Delete a student:
DELETE /delete_student/{student_id}

Get average GPA by entry year:
GET /average_gpa_by_entry_year

Add a study:
POST /add_study

Get faculty by ID:
GET /get_faculty/{faculty_id}

Update faculty information:
PUT /update_faculty/{faculty_id}

Delete a faculty:
DELETE /delete_faculty/{faculty_id}
