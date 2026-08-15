from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

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
    # buraya henüz bir şey yazma, bir sonraki adımda 404 ekleyeceğiz
    return JSONResponse(status_code=404, content={"error": f"Task {id} not found"})

@app.post("/tasks", status_code=201)
async def create_task(task: Task):
    if not task.title :
        return JSONResponse(status_code=400, content={"error": "Task title is required"})
    new_task = {"id": len(tasks) + 1, "title": task.title, "done": False}
    tasks.append(new_task)
    return new_task


