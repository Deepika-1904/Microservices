# Microservices
A REST-based **Student Marks Microservice** developed using **Python, FastAPI, and Uvicorn**. The application demonstrates basic **Create, Read, Update, and Delete (CRUD)** operations on student marks data using REST APIs.

The project uses a **Python dictionary as an in-memory database** and **Pydantic** for data validation.

### Technologies Used

* Python
* FastAPI
* Uvicorn
* Pydantic
* REST API
* In-memory Dictionary Database

### CRUD Endpoints

* `POST /students` – Create a student
* `GET /students` – Retrieve all students
* `GET /students/{id}` – Retrieve a specific student
* `PUT /students/{id}` – Update student details
* `DELETE /students/{id}` – Delete a student

The APIs can be tested through FastAPI's automatically generated **Swagger UI** at `/docs`.

### Running the Project

```bash
pip install -r requirements.txt
python -m uvicorn app:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

to test the CRUD operations using Swagger UI.
