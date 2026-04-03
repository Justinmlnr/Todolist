from fastapi import FastAPI, HTTPException
from Todo import Todo

app = FastAPI() #crée l'application

todos: list[Todo] = []

@app.get("/todos")
def get_todos() -> list[Todo]:
    return todos

@app.post("/todos")
def create_todo(todo: Todo) -> Todo:
    todo.id = len(todos) + 1
    todos.append(todo)
    return todo

@app.get("/todos/{id}")
def get_todo(id: int) -> Todo:
    for todo in todos:
        if todo.id == id:
            return todo
    raise HTTPException(status_code=404, detail="Tâche non trouvée")

@app.put("/todos/{id}")
def update_todo(id: int, new_todo: Todo) -> Todo:
    for i in range(len(todos)):
        if todos[i].id == id:
            new_todo.id = id
            todos[i] = new_todo
            return new_todo
    raise HTTPException(status_code=404, detail="Tâche non trouvée")


@app.delete("/todos/{id}")
def delete_todo(id: int) -> dict[str, str]:
    for i in range(len(todos)):
        if todos[i].id == id:
            del todos[i]
            return {"message": "Tâche supprimée"}
    raise HTTPException(status_code=404, detail="Tâche non trouvée")