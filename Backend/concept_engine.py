import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data.json")

with open(DATA_PATH, "r") as f:
    DATA = json.load(f)

concepts = {c["id"]: c for c in DATA["concepts"]}

mastery = {}

THRESHOLD = 0.5

def get_question(concept):
    return concepts[concept]["questions"][0]

def get_lesson(concept):
    return concepts[concept]["lesson"]

def update_mastery(concept, correct):
    if concept not in mastery:
        mastery[concept] = 0.5

    if correct:
        mastery[concept] += 0.2
    else:
        mastery[concept] -= 0.2

    mastery[concept] = max(0, min(1, mastery[concept]))

def get_breakpoint(concept):
    if mastery.get(concept,0) < THRESHOLD:
        prereq = concepts[concept]["prerequisites"]
        if prereq:
            return prereq[0]
    return None