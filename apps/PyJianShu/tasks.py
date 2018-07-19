from __future__ import absolute_import, unicode_literals
from celery import shared_task

from apps.PyJianShu.grab import execute

@shared_task
def add():
    print('我要开始了')
    execute()
    print('我要结束了')
    return 0

