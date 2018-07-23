from django.db import models
import MySQLdb

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')
    js_id = models.CharField(max_length=40, verbose_name='简书id', unique=True)
    home_page = models.CharField(max_length=50, verbose_name='个人主页')

class Article(models.Model):
    title = models.CharField(max_length=5000, verbose_name='文章标题')
    js_id = models.CharField(max_length=40, verbose_name='简书文章id', unique=True)
    article_page = models.CharField(max_length=40, verbose_name='简书文章页面')
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='用户id')
    newstime = models.IntegerField(verbose_name='发布时间')

    @staticmethod
    def addArticles(article_list):
        querysetlist = []
        for i in article_list:
            # print(i['js_article_id'])
            querysetlist.append(
                Article(title=MySQLdb.escape_string(i['title']), js_id=i['js_article_id'], article_page=i['url'],
                        newstime=i['time'], user_id=i['user_id']))
        Article.objects.bulk_create(querysetlist)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户id')
    content = models.CharField(max_length=5000, verbose_name='评论内容')
    js_user_id = models.CharField(max_length=40, verbose_name='简书用户id')
    js_article_id = models.CharField(max_length=40, verbose_name='简书文章id')
    js_article_user_id = models.CharField(max_length=40, verbose_name='文章所属用户简书id')
    newstime = models.IntegerField(verbose_name='评论时间')

    @staticmethod
    def addComments(comment_list):
        querysetlist = []
        for i in comment_list:
            # print(i['user_js_id'])
            querysetlist.append(Comment(content=MySQLdb.escape_string(i['content']), js_article_id=i['js_article_id'],
                                        js_article_user_id=i['js_article_user'], newstime=i['time'],
                                        js_user_id=i['user_js_id'], user_id=i['user_id']))
        Comment.objects.bulk_create(querysetlist)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户id')
    js_user_id = models.CharField(max_length=40, verbose_name='简书用户id')
    js_like_user_id = models.CharField(max_length=40, verbose_name='简书获赞人id')
    js_article_id = models.CharField(max_length=40, verbose_name='简书文章id')
    newstime = models.IntegerField(verbose_name='点赞时间')

    @staticmethod
    def addLikes(like_list):
        querysetlist = []
        for i in like_list:
            querysetlist.append(
                Like(js_article_id=i['js_article_id'], js_like_user_id=i['js_like_user_id'], js_user_id=i['user_js_id'],
                     newstime=i['time'], user_id=i['user_id']))
        Like.objects.bulk_create(querysetlist)

