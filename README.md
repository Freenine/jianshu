# jianshu
Django and python

## 克隆项目
> git clone git@github.com:Freenine/jianshu.git
## 配置数据库
> 将 `database.py` 放入根目录
>
> pip install -r requirement.txt

## 启动 redis
> redis-server
## 启动任务调度
> celery -A apps.PyJianShu.task worker -l info -P eventlet
>
> celery -A apps.PyJianShu.task beat -l info
