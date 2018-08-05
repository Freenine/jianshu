from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from .function import dictfetchall, getThisWeek, geTtimeStamp
import MySQLdb, time

# from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'pyjianshu/index.html')

# 文章统计
def articleCount(request):
    this_week = getThisWeek()
    time_start = (request.GET.get('time_start', geTtimeStamp(this_week['start'])))
    time_end = (request.GET.get('time_end', geTtimeStamp(this_week['end'])))

    with connection.cursor() as cursor:
        cursor.execute("select u.name, u.home_page,count(a2.id) as article_count "
                       "from PyJianShu_user as u "
                       "left join (select a.user_id, a.id from PyJianShu_article as a where a.newstime >= %s and a.newstime <= %s) "
                       "as a2 on u.id=a2.user_id group by u.id order by article_count desc, u.name",[time_start, time_end])

        data = dictfetchall(cursor)

    return JsonResponse(data, safe=False)

# 评论统计
def commentCount(request):
    this_week = getThisWeek()
    time_start = (request.GET.get('time_start', geTtimeStamp(this_week['start'])))
    time_end = (request.GET.get('time_end', geTtimeStamp(this_week['end'])))

    with connection.cursor() as cursor:
        cursor.execute("select u.name, u.home_page,count(a2.id) as comment_count "
                       "from PyJianShu_user as u "
                       "left join (select a.user_id, a.id from PyJianShu_comment as a where a.newstime >= %s and a.newstime <= %s) "
                       "as a2 on u.id=a2.user_id group by u.id order by comment_count desc, u.name", [time_start, time_end])

        data = dictfetchall(cursor)

    return JsonResponse(data, safe=False)

# 赞统计
def likeCount(request):
    this_week = getThisWeek()
    time_start = (request.GET.get('time_start', geTtimeStamp(this_week['start'])))
    time_end = (request.GET.get('time_end', geTtimeStamp(this_week['end'])))

    with connection.cursor() as cursor:
        cursor.execute("select u.name, u.home_page,count(a2.id) as like_count "
                       "from PyJianShu_user as u "
                       "left join (select a.user_id, a.id from PyJianShu_like as a where a.newstime >= %s and a.newstime <= %s) "
                       "as a2 on u.id=a2.user_id group by u.id order by like_count desc, u.name", [time_start, time_end])

        data = dictfetchall(cursor)

    return JsonResponse(data, safe=False)


