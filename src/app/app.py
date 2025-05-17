from fastapi import FastAPI, HTTPException
from src.pred.image_classifier import *
from fastapi.middleware.cors import CORSMiddleware
from src.schemas.image_schema import Img
from fastapi.responses import JSONResponse

app = FastAPI(title="Image Classifier API")

origins = [
    "http://localhost:3000",
    "localhost:3000",
    "*",
    "http://127.0.0.1:8089/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def read_main():
    return {"msg": "Hello World !!!!"}


@app.post("/predict/internship/", status_code=200)
async def predict_internship(request: Img):
    prediction = internship_run_classifier(request.img_url)
    if not prediction:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail="Image could not be downloaded"

        )

    return JSONResponse(content=prediction)
