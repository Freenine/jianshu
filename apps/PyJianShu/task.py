from celery import Celery
from celery.schedules import crontab

app = Celery(broker='redis://127.0.0.1:6379')
app.conf.timezone = 'Asia/Shanghai'
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    # sender.add_periodic_task(1.0, test.s(), name='add every 10')

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=9, minute=51),
        test.s(),
    )

@app.task
def test():
    print('hello')