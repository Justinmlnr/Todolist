from fastapi import FastAPI, HTTPException
from Todo import Todo
from User import User

app = FastAPI() #crée l'application

todos: list[Todo] = []
users: list[User] = []

# --------------Users --------------------
@app.get("/users")
def get_users() -> list[User]:
    return users

@app.post("/users")
def create_user(user: User) -> User:
    user.id = len(users) + 1
    users.append(user)
    return user

#================== Todos ======================
@app.get("/todos")
def get_todos() -> list[Todo]:
    return todos

@app.post("/todos")
def create_todo(todo: Todo) -> Todo:
    for user in users:
        if user.id == todo.user_id:
            todo.id = len(todos) + 1
            todos.append(todo)
            return todo

    raise HTTPException(status_code=404, detail="Users pas trouvé")

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