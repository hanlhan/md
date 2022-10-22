# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone

class Article(models.Model):
    # id
    id = models.AutoField(primary_key=True)
    # 文章用户 id
    userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(0))
    # 文章标题
    title = models.CharField(max_length=100)
    # 文章内容
    content = models.CharField(max_length=10000, blank=True, null=True)
    # 文章创建时间
    createtime = models.DateTimeField(auto_now=timezone.now)
    # 文章最后修改时间
    altertime = models.DateTimeField()
    # 文章是否删除
    isdel = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'article'



class User(AbstractUser):
    # 手机号
    phone = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = "user"


class WXUserInfo(models.Model):
    """

    """
    # id
    id = models.AutoField(primary_key=True)
    # 所属用户 id
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(0))
    # openid
    openID = models.CharField(max_length=100)
    # nickname
    nickname = models.CharField(max_length=50)
    # sex
    sex = models.IntegerField(null=True)
    # province
    province = models.CharField(max_length=50, null=True)
    # city
    city = models.CharField(max_length=50, null=True)
    # country
    country = models.CharField(max_length=50, null=True)
    # headimgurl
    headimgurl = models.CharField(max_length=100, null=True)
    # privilege
    privilege = models.CharField(max_length=50, null=True)
    # unionid
    unionid = models.CharField(max_length=100)

    class  Meta:
        db_table = "wx_user_info"



