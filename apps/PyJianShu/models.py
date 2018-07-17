from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')
    js_id = models.CharField(max_length=40, verbose_name='简书id', unique=True)
    home_page = models.CharField(max_length=50, verbose_name='个人主页')

class Article(models.Model):
    title = models.CharField(max_length=40, verbose_name='文章标题')
    js_id = models.CharField(max_length=40, verbose_name='简书文章id', unique=True)
    article_page = models.CharField(max_length=40, verbose_name='简书文章页面')
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='用户id')
    newstime = models.DateTimeField(verbose_name='发布时间')

class Comment(models.Model):
    content = models.CharField(max_length=40, verbose_name='评论内容')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户id')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章id')
    js_article_id = models.CharField(max_length=40, verbose_name='简书文章id')
    js_article_user = models.CharField(max_length=40, verbose_name='文章所属用户简书id')
    newstime = models.DateTimeField(verbose_name='评论时间')

class Like(models.Model):
    js_user_id = models.CharField(max_length=40, verbose_name='简书用户id')
    js_like_user_id = models.CharField(max_length=40, verbose_name='简书获赞人id')
    js_article_id = models.CharField(max_length=40, verbose_name='简书文章id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户id')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章id')
    newstime = models.DateTimeField(verbose_name='点赞时间')

