from celery import Celery

app = Celery("tasks")
app.config_from_object('app.celery.celeryconfig')


@app.task
def hello_world():
    return "Hello world!"
