web: gunicorn time_tasks.wsgi

worker: celery -A time_tasks --beat -S django --l info