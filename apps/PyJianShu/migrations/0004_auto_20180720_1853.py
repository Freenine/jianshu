# Generated by Django 2.0.7 on 2018-07-20 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PyJianShu', '0003_auto_20180718_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='newstime',
            field=models.IntegerField(verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='newstime',
            field=models.IntegerField(verbose_name='评论时间'),
        ),
        migrations.AlterField(
            model_name='like',
            name='newstime',
            field=models.IntegerField(verbose_name='点赞时间'),
        ),
    ]