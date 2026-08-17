from models import Student


# In-memory database
students = {}


def create(student: Student):
    if student.id in students:
        return None

    students[student.id] = student
    return student


def get(student_id: int):
    return students.get(student_id)


def get_all():
    return list(students.values())


def update(student_id: int, student: Student):
    if student_id not in students:
        return None

    students[student_id] = student
    return student


def delete(student_id: int):
    if student_id not in students:
        return False

    del students[student_id]
    return True