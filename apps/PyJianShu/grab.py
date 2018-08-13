import requests,time, datetime,threading
from bs4 import BeautifulSoup
from .models import *
from .function import  *
user_all_list =[]
flag = 0
lock = threading.Lock()
article_list = []

comment_list = []

like_list = []

def getUser(test):

    for user in test:
        grabArticle(user)


def getData(userDict):

    time1 = time.time()
    for user in userDict:
        grabArticle(user)

    time2 = time.time()
    print(time2 - time1)
    return {'article_list': article_list, 'comment_list': comment_list, 'like_list': like_list}


def grabArticle(user):
    global user_all_list,like_list,comment_list,article_list
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }

    user_js_id = user.js_id
    user_id = user.id
    url = 'https://www.jianshu.com/users/' + user_js_id + '/timeline?_pjax=%23list-container'

    resp = requests.get(url, headers=headers)


    soup = BeautifulSoup(resp.content, 'lxml')
    ul = soup.select('.note-list > li > .content')
    data = soup.select('.note-list > li')
    feedList = []
    for feedLi in data:
        feedList.append(feedLi['id'][5:])

    page = 1
    feed = 999999999
    flog = True
    yesStart = geTtimeStamp(getYesterday()['start'])
    yesEnd = geTtimeStamp(getYesterday()['end'])
    while len(feedList) != 0:
        feed = feedList[-1]
        for li in ul:
            span = li.select('.author > .info > span')
            data_type = span[0]['data-type']
            # print()
            dt = span[0]['data-datetime'][0:10] + " " + span[0]['data-datetime'][11:19]
            timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
            timeInt = int(time.mktime(timeArray))
            if timeInt > yesStart and timeInt < yesEnd:
                # print(timeInt, yesStart, yesEnd)
                if data_type == 'share_note':
                    #文章
                    res = appendArticle(li,user_js_id,span,user_id)
                    article_list.append(res)
                elif data_type == 'comment_note':
                    #评论
                    res = appendComment(li, user_js_id, span,user_id)
                    # appendComment(li, user_id, span)
                    comment_list.append(res)
                    # print(li)
                    # pass
                elif data_type == 'like_note' and len(li.select('.title')) != 0:
                    res = appendLike(li, user_js_id, span,user_id)
                    like_list.append(res)
            elif timeInt < yesStart:
                feedList = []
                flog = False
                break
        if flog == False:
            break
        page = page+ 1
        feed = int(feed) - 1
        url = 'https://www.jianshu.com/users/' + user_js_id + '/timeline?max_id='+ str(feed) + '&page=' + str(page)
        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.content, 'lxml')
        ul = soup.select('.note-list > li > .content')
        data = soup.select('.note-list > li')
        feedList = []
        for feedLi in data:
            feedList.append(feedLi['id'][5:])
        # print(feedList)


    # print(article)

def appendArticle(li,user_js_id,span,user_id):
    dt = span[0]['data-datetime'][0:10] + " " + span[0]['data-datetime'][11:19]
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    timeInt = int(time.mktime(timeArray))
    tag = li.select('.title')
    d = {'user_js_id':user_js_id}
    str = tag[0].string
    # print(str is not None)
    if str is not None:
        d['title'] = str
    else:
        d['title'] = '无标题'
    d['js_article_id'] = tag[0]['href'][3:-1]
    d['url'] = 'https://www.jianshu.com'+ tag[0]['href']
    d['time'] = timeInt
    d['user_id'] = user_id

    return d

def appendComment(li,user_js_id,span,user_id):
    d = {'user_js_id': user_js_id}

    dt = span[0]['data-datetime'][0:10] + " " + span[0]['data-datetime'][11:19]
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    timeInt = int(time.mktime(timeArray))
    d['time'] = timeInt

    tag = li.select('.comment')
    str = tag[0].string
    if str is not None:
        d['content'] = str
    else:
        d['content'] = '无内容'


    tag = li.select('blockquote > .title')
    d['js_article_id'] = tag[0]['href'][3:-1]

    tag = li.select('blockquote > .meta > .origin-author > a')
    d['js_article_user'] = tag[0]['href'][7:-1]

    d['user_id'] = user_id

    return d

def appendLike(li,user_js_id,span,user_id):
    d = {'user_js_id': user_js_id}

    dt = span[0]['data-datetime'][0:10] + " " + span[0]['data-datetime'][11:19]
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    timeInt = int(time.mktime(timeArray))
    d['time'] = timeInt

    # tag = li.select('.comment')
    # d['content'] = tag[0].string

    tag = li.select('.title')
    d['js_article_id'] = tag[0]['href'][3:-1]

    tag = li.select('.meta > .origin-author > a')
    d['js_like_user_id'] = tag[0]['href'][7:-1]

    d['user_id'] = user_id

    return d

def execute():
    global like_list, comment_list, article_list
    list = User.objects.all()
    article_list = []
    comment_list = []
    like_list = []
    data = getData(list)
    Article.addArticles(data['article_list'])
    Comment.addComments(data['comment_list'])
    Like.addLikes(data['like_list'])

