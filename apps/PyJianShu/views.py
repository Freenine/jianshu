from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from .function import dictfetchall, getThisWeek, geTtimeStamp
import MySQLdb, time

# from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {}
    context['index'] = 'This is index!'
    return render(request,'pyjianshu/index.html',context)

# 文章统计
def articleCount(request):
    this_week = getThisWeek()
    time_start = geTtimeStamp(request.GET.get('time_start', this_week['start']))
    time_end = geTtimeStamp(request.GET.get('time_end', this_week['end']))

    with connection.cursor() as cursor:
        cursor.execute("select u.name, u.home_page,count(a2.id) as article_count "
                       "from PyJianShu_user as u "
                       "left join (select a.user_id, a.id from PyJianShu_article as a where a.newstime >= %s and a.newstime <= %s) "
                       "as a2 on u.id=a2.user_id group by u.id order by article_count desc",[time_start, time_end])

        data = dictfetchall(cursor)

    return JsonResponse(data, safe=False)

# 评论统计
def commentCount(request):
    this_week = getThisWeek()
    time_start = geTtimeStamp(request.GET.get('time_start', this_week['start']))
    time_end = geTtimeStamp(request.GET.get('time_end', this_week['end']))

    with connection.cursor() as cursor:
        cursor.execute("select u.name, u.home_page,count(a2.id) as comment_count "
                       "from PyJianShu_user as u "
                       "left join (select a.user_id, a.id from PyJianShu_comment as a where a.newstime >= %s and a.newstime <= %s) "
                       "as a2 on u.id=a2.user_id group by u.id order by comment_count desc", [time_start, time_end])

        data = dictfetchall(cursor)

    return JsonResponse(data, safe=False)

# 赞统计
def zanCount(request):
    this_week = getThisWeek()
    time_start = geTtimeStamp(request.GET.get('time_start', this_week['start']))
    time_end = geTtimeStamp(request.GET.get('time_end', this_week['end']))

    with connection.cursor() as cursor:
        cursor.execute("select u.name, u.home_page,count(a2.id) as zan_count "
                       "from PyJianShu_user as u "
                       "left join (select a.user_id, a.id from PyJianShu_zan as a where a.newstime >= %s and a.newstime <= %s) "
                       "as a2 on u.id=a2.user_id group by u.id order by zan_count desc", [time_start, time_end])

        data = dictfetchall(cursor)

    return JsonResponse(data, safe=False)


















































def grabdata():
    context = {}
    # listDict = {'0':[],'1':[],'2':[],'3':[]}
    list = User.objects.all()

    # for li in list:
    #     listDict[str(li.id % 4)].append(li.js_id)

    # list
    # print(list)
    data = getData(list)
    #


    # print(len(data['arctile_list']))
    context['article_list'] = data['article_list']
    context['comment_list'] = data['comment_list']
    context['like_list'] = data['like_list']
    # print(len(context['article_list']),len(context['comment_list']),len(context['like_list']))

    # addArticle(data['article_list'])
    # addComment(data['comment_list'])
    # addLike(data['like_list'])

    # return render(request, 'pyjianshu/index.html', context)
    # pass
#
# def addArticle(article_list):
#     querysetlist = []
#     for i in article_list:
#         # print(i['js_article_id'])
#         querysetlist.append(Article(title=MySQLdb.escape_string(i['title']),js_id=i['js_article_id'],article_page=i['url'],newstime=i['time'],user_id=i['user_id']))
#     Article.objects.bulk_create(querysetlist)
#
# def addComment(comment_list):
#     querysetlist = []
#     for i in comment_list:
#         querysetlist.append(Comment(content=MySQLdb.escape_string(i['content']),js_article_id=i['js_article_id'],js_article_user_id=i['js_article_user'],newstime=i['time'],js_user_id=i['user_js_id'],user_id=i['user_id']))
#     Comment.objects.bulk_create(querysetlist)
#
# def addLike(like_list):
#     querysetlist = []
#     for i in like_list:
#         querysetlist.append(Like(js_article_id=i['js_article_id'],js_like_user_id=i['js_like_user_id'],js_user_id=i['user_js_id'],newstime=i['time'],user_id=i['user_id']))
#     Like.objects.bulk_create(querysetlist)


