from datetime import timedelta
import datetime, time


# 自定义方法


# 将自定义查询结果 转换为 dict
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

# 获取时间戳 时间格式为 2008-12-12 23:59:59
def geTtimeStamp(datatime):
    return int(time.mktime(time.strptime(datatime, '%Y-%m-%d %H:%M:%S')))

# 获取昨天的开始时间和结束时间
def getYesterday():
    today=datetime.date.today()
    yesterday= (today - timedelta(days=1)).strftime('%Y-%m-%d')
    return {
        'start': yesterday + ' 00:00:00',
        'end': yesterday + ' 23:59:59'
    }

# 获取本周的开始时间和结束时间
def getThisWeek():
    now = datetime.datetime.now()
    this_week_start = now - timedelta(days=now.weekday())
    this_week_end = now + timedelta(days=6 - now.weekday())
    return {
        'start': this_week_start.strftime('%Y-%m-%d')+ ' 00:00:00',
        'end': this_week_end.strftime('%Y-%m-%d') + ' 23:59:59'
    }