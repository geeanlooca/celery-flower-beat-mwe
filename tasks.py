import os

from celery import Celery

from os import environ
from core_processing import make_psd_detection

broker_url = environ['CELERY_BROKER_URL']
result_backend = environ['CELERY_RESULT_BACKEND']

print(f'{broker_url=} {result_backend=}')


app = Celery('app', broker=broker_url, backend=result_backend)
from celery.schedules import crontab


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('hello') every 30 seconds.
    # It uses the same signature of previous task, an explicit name is
    # defined to avoid this task replacing the previous one defined.
    sender.add_periodic_task(30.0, test.s('hello'), name='add every 30')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=16, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )

    sender.add_periodic_task(
        crontab(hour=16, minute=31),
        gather_stats.s(),
    )

@app.task
def add(x, y):
    return x + y

@app.task
def test(msg):
    print(msg)

@app.task
def gather_stats():
    x = make_psd_detection()
    print(f'Detection stats: {x=}')