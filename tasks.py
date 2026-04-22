import time
from celery_app import app


@app.task(bind=True)
def add(self, x, y):
    """
    Add two numbers together.
    bind=True gives us access to 'self' (the task instance)
    so we can log the task ID.
    """
    print(f"[Task ID: {self.request.id}] Adding {x} + {y} ...")
    time.sleep(2)          # simulate a tiny delay (like a DB call)
    result = x + y
    print(f"[Task ID: {self.request.id}] Result = {result}")
    return result


@app.task(bind=True)
def multiply(self, x, y):
    """Multiply two numbers."""
    print(f"[Task ID: {self.request.id}] Multiplying {x} * {y} ...")
    time.sleep(1)
    return x * y


@app.task(bind=True, max_retries=3)
def divide(self, x, y):
    """
    Divide x by y.
    If y == 0, retry up to 3 times (just to demonstrate retry).
    In real life you'd fix the input, but this shows the pattern.
    """
    try:
        print(f"[Task ID: {self.request.id}] Dividing {x} / {y} ...")
        time.sleep(1)
        return x / y
    except ZeroDivisionError as exc:
        print(f"[Task ID: {self.request.id}] ZeroDivisionError! Retrying...")
        raise self.retry(exc=exc, countdown=3)   # wait 3s then retry