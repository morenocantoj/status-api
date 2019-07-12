from celery import Celery
from app.config import REDIS_BROKER

app = Celery("tasks")
app.conf.broker_url = REDIS_BROKER


@app.task
def hello_world():
    return "Hello world!"
