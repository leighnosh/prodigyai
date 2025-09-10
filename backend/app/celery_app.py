import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

# Redis configuration
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", "6380")
REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"

# Create Celery instance
celery_app = Celery(
    "prodigyai",
    broker=REDIS_URL,
    backend=REDIS_URL,
    include=["app.tasks.sample_tasks"]
)

# Celery configuration
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    task_result_expires=3600,  # Results expire after 1 hour
)

# Auto-discover tasks
celery_app.autodiscover_tasks()