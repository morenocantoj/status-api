# status-api
Worker to check servers status with Python 3.7

# How to set up
For the moment, you can set up your working environment with these steps:
- Start your Redis database service, in my case with `docker run -d -p 6379:6379 redis`
- Start Celery main worker: `celery -A app.celery.main worker --loglevel=info`
- Start Flower monitoring tool for Celery: `celery flower -A app.celery.main worker --loglevel=info`
