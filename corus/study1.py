from fastapi import FastAPI

app = FastAPI()

@app.get("/tarefas")
def get():
    return {"keyMessage": "hello world"}