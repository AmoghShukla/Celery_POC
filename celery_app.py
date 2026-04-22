from celery import Celery

app = Celery(
    'workers',
    broker="amqp://guest:guest@localhost:5672//",
    backend="redis://localhost:6379/0"
)

app.conf.update(
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
    timezone='UTC',
    task_track_started=True,
)