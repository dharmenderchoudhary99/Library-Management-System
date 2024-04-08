from fastapi import APIRouter
from models.student import Student
from config.db import conn
from bson.objectid import ObjectId
from schemas.students import serializeDict, serializeList
student = APIRouter()

@student.post('/students', response_model=Student)
async def create_student(student: Student):
    result = conn.local.students.insert_one(student.dict(by_alias=True))
    new_student = conn.local.students.find_one({"_id": result.inserted_id})
    new_student["id"] = str(new_student.pop("_id"))
    return new_student

@student.get('/students', response_model=list[Student])
async def list_students(country: str = None, age: int = None):
    query = {}
    if country:
        query["address.country"] = country
    if age:
        query["age"] = {"$gte": age}
    students = conn.local.students.find(query)
    return [serializeDict(student) for student in students]

@student.get('/students/{id}', response_model=Student)
async def get_student(id: str):
    student = conn.local.students.find_one({"_id": ObjectId(id)})
    if student:
        student["id"] = str(student.pop("_id"))
        return student
    return None

@student.patch('/students/{id}')
async def update_student(id: str, student: Student):
    result = conn.local.students.find_one_and_update({"_id": ObjectId(id)}, {"$set": student.dict(by_alias=True)})
    if result:
        result["id"] = str(result.pop("_id"))
        return result
    return None

@student.delete('/students/{id}')
async def delete_student(id: str):
    result = conn.local.students.find_one_and_delete({"_id": ObjectId(id)})
    if result:
        result["id"] = str(result.pop("_id"))
        return result
    return None