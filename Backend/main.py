from fastapi import FastAPI
from pydantic import BaseModel
from concept_engine import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Answer(BaseModel):
    concept: str
    correct: bool

@app.get("/question/{concept}")
def question(concept):
    return get_question(concept)

@app.post("/answer")
def answer(data: Answer):
    update_mastery(data.concept, data.correct)

    breakpoint = get_breakpoint(data.concept)

    if breakpoint:
        return {
            "breakpoint": breakpoint
        }

    return {"status":"continue"}

@app.get("/lesson/{concept}")
def lesson(concept):
    return {"lesson": get_lesson(concept)}

