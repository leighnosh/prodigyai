from fastapi import APIRouter
from app.tasks.sample_tasks import add_numbers
from app.celery_app import celery_app

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/add")
def run_add_numbers(x: int, y: int):
    task = add_numbers.delay(x, y)
    return {"task_id": task.id}

@router.get("/{task_id}")
def get_task_result(task_id: str):
    result = celery_app.AsyncResult(task_id)
    return {
        "task_id": task_id,
        "status": result.status,
        "result": result.result if result.successful() else None
    }