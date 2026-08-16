from fastapi import FastAPI,Response 
from fastapi.responses import JSONResponse
from pydantic import BaseModel

class TaskUpdate(BaseModel):
    title: str = None
    done: bool = None

class Task(BaseModel):
    title: str = ""
  
app = FastAPI()
tasks =[{"id":1,"title": "Learn FastAPI","done": False},{"id":2,"title": "Build a CRUD API","done": False},{"id":3,"title": "Deploy the API","done": True}]

@app.get("/")
async def root():
    # return {"message": "Hello World"}
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }
@app.get("/health")
async def health():
    return {"status": "ok"}
@app.get("/tasks")
async def get_tasks():
    return tasks
@app.get("/tasks/{id}")
async def get_task(id: int):
    for task in tasks:
        if task["id"] == id:
            return task
    
    return JSONResponse(status_code=404, content={"error": f"Task {id} not found"})

@app.post("/tasks", status_code=201)
async def create_task(task: Task):
    if not task.title :
        return JSONResponse(status_code=400, content={"error": "Task title is required"})
    new_task = {"id":max ((t["id"] for t in tasks),default = 0)+1 ,"title": task.title, "done": False}
    tasks.append(new_task)
    return new_task
@app.put("/tasks/{id}")
async def update_task(id: int, task_update: TaskUpdate):
     if task_update.title is None and task_update.done is None:
        return JSONResponse(status_code=400, content={"error": "At least one field (title or done) must be provided for update"})
           

     for task in tasks:
        if task["id"] == id:
            if task_update.title is not None:
                task["title"] = task_update.title
            if task_update.done is not None:
                task["done"] = task_update.done
            return task
     return JSONResponse(status_code=404, content={"error": f"Task {id} not found"})
@app.delete("/tasks/{id}")
async def delete_task(id: int):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            return Response(status_code=204)
    return JSONResponse(status_code=404, content={"error": f"Task {id} not found"})

