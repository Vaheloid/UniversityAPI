from typing import List

from fastapi import FastAPI, Depends

from app.students.models import Student
from utils import json_to_dict_list
import os

# # Получаем путь к директории текущего скрипта
# script_dir = os.path.dirname(os.path.abspath(__file__))
#
# # Переходим на уровень выше
# parent_dir = os.path.dirname(script_dir)
#
# # Получаем путь к JSON
# path_to_json = os.path.join(parent_dir, 'students.json')

path_to_json = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "students.json"
)

app = FastAPI()


class RBStudent:
    def __init__(
        self, course: int, major: str | None = None, enrollment_year: int | None = 2018
    ):
        self.course = course
        self.major: str | None = major
        self.enrollment_year: int | None = enrollment_year


@app.get("")
def get_all_students(course: int | None = None):
    students = json_to_dict_list(path_to_json)
    if course is None:
        return students
    else:
        return_list = []
        for student in students:
            if student["course"] == course:
                return_list.append(student)
        return return_list


@app.get("/students/{course}")
def get_all_students_course(request_body: RBStudent = Depends()) -> List[SStudent]:
    students = json_to_dict_list(path_to_json)
    filtered_students = []
    for student in students:
        if student["course"] == request_body.course:
            filtered_students.append(student)

    if request_body.major:
        filtered_students = [
            student
            for student in filtered_students
            if student["major"].lower() == request_body.major.lower()
        ]
    if request_body.enrollment_year:
        filtered_students = [
            student
            for student in filtered_students
            if student["enrollment_year"] == request_body.enrollment_year
        ]
    return filtered_students


@app.get("/student", response_model=SStudent)
def get_student_from_param_id(student_id: int):
    students = json_to_dict_list(path_to_json)
    for student in students:
        if student["student_id"] == student_id:
            return student
    return None
