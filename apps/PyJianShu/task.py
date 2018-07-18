from celery import Celery
from celery.schedules import crontab

from .grab import execute
app = Celery(broker='redis://127.0.0.1:6379')
app.conf.timezone = 'Asia/Shanghai'
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    # sender.add_periodic_task(1.0, test.s(), name='add every 10')

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=23, minute=3),
        test.s(),
    )

@app.task
def test():

    print('我要开始了')
    execute()
    print('我要结束了')