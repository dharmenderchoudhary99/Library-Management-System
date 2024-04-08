from pymongo import MongoClient

conn = MongoClient("mongodb://localhost:27017/")
db = conn["your_database_name"]
students = db["students"]