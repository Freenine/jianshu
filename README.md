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
> celery worker -A JianShu -l info
>
> celery beat -A JianShu -l info
