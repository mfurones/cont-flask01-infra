
from fastapi import FastAPI
from api.bll.cv import cv

app = FastAPI()
objCV = cv()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/cv")
def get_api_cv():
    
    return objCV.get_cvs