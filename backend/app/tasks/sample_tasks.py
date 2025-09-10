from app.celery_app import celery_app


@celery_app.task
def add_numbers(x: int, y: int):
    """Simple addition task for testing."""
    return x + y