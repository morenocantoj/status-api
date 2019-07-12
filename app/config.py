import os

REDIS = {
    'url': os.getenv('REDIS_URL', default='localhost'),
    'port': os.getenv('REDIS_PORT', default='6379'),
    'password': os.getenv('REDIS_PASSWORD', default='')
}

REDIS_BROKER = "redis://:{password}@{url}:{port}/0".format(**REDIS)
