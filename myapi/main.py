# main.py
from fastapi import FastAPI

app = FastAPI()

fakeDatabase = {
    1: {"task": "clean house"},
    2: {"task": "blog"},
    3: {"task": "buy house"},
}


@app.get("/{id}")
def getItem(id: int):
    return fakeDatabase[id]


# Option # 1
@app.post("/")
def addItem(task: str):
    newId = len(fakeDatabase.keys()) + 1
    fakeDatabase[newId] = {"task": task}
    return fakeDatabase
