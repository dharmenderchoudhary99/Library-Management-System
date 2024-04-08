
from routes.student import student

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")

app.include_router(student)