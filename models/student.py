from pydantic import BaseModel


class Student(BaseModel):
    name: str
    age: int
    address: dict
    class Address(BaseModel):
        city: str
        country: str