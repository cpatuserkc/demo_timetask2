# time_tasks/celery/__init__.py
from __future__ import absolute_import, unicode_literals
import os



from celery import Celery
from celery.schedules import crontab

print(__name__, "package initiated")
# You can use rabbitmq instead here.
BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'time_tasks.settings')

'''
THIS IS IMPORTED INTO DJANGO via __init__ of the time_tasks app
'''
app = Celery('time_tasks')


# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.broker_url = BASE_REDIS_URL

# this allows you to schedule items in the Django admin.
try:
    app.conf.beat_scheduler = 'django_celery_beat.schedulers:DatabaseScheduler'
except:
    print("beat scheduler doesnt need : trying without")
    pass
    
    try:
        app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'
    except:
        pass


from celery.schedules import crontab


#https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html?highlight=app.conf.beat_schedule#crontab-schedules
# app.conf.beat_schedule = {
#     # Executes every Monday morning at 7:30 a.m.
#     'add-every-monday-morning': {
#         'task': 'tasks.add',
#         'schedule': crontab(hour=7, minute=30, day_of_week=1),
#         'args': (16, 16),
#     },
# }


print(f"Celery app name {app} \nbase redis url {BASE_REDIS_URL} \n")