import requests,time, datetime
from bs4 import BeautifulSoup


def grabArctile():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}

    url = 'https://www.jianshu.com/users/4de1477a2c7a/timeline?_pjax=%23list-container'

    user_id = '4de1477a2c7a'

    resp = requests.get(url, headers=headers)


    soup = BeautifulSoup(resp.content, 'lxml')

    ul = soup.select('.note-list > li > .content')

    arctile = []

    list = []

    for li in ul:
        span = li.select('.author > .info > span')
        # print()
        if span[0]['data-type'] == 'share_note':
            arctile.append(li)
            appendArctile(list,li,user_id,span)

    # print(arctile)

def appendArctile(list,li,user_id,span):
    dt = span[0]['data-datetime'][0:10] + " " + span[0]['data-datetime'][11:19]
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    timeInt = int(time.mktime(timeArray))
    tag = li.select('.title')
    d = {'user_id':user_id}
    d['title'] = tag[0].string
    d['url'] = 'https://www.jianshu.com'+ tag[0]['href']
    d['time'] = timeInt

    list.append(d)
    print(list)



grabArctile()