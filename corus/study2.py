from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()
class taskDefault(BaseModel):
    id: int
    name: str = Field(
        example="Limpar a casa",
        description="Nomeie a tarefa"
    )
    description: str=Field(
        example="Limpar corredores, garagem, banheiro e sala",
        description="Coloque detalhes da tarefa"
    )
    complete: bool=False

tasks: List[taskDefault]=[]

@app.get("/tasks")
def taskList():
    return {"Todas as tarefas": tasks}

@app.post("/tasks")
def createTask(task: taskDefault):
    tasks.append(task)
    return {"Tarefa criada": task}

@app.get("/tasks/{task_id}")
def taskListByID(task_id: int):
    for i in tasks: 
        if i.id==task_id:
            return i
    return {"ERRO": "ID não encontrado"}
