from django.db import models

# Create your models here.
# ORM相关的只能写在这个文件里,写到别的文件里Django找不到


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)  # 创建一个自增的主键字段
    name = models.CharField(null=False, max_length=32)   # 创建一个varchar(20)类型的不能为空的字段

    def __str__(self):
        return self.name

    class Meta:
        # db_table = 'mytable' #自定义表名
        # verbose_name = '自定义名称' #指定admin管理页面名称
        ordering = ['name']


#图书管理系统
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, unique=True, max_length=64)
    addr = models.CharField(max_length=128,null=False,default="west zhongshan road")
    def __str__(self):
        return self.name

    class Meta:
        # db_table = 'mytable' #自定义表名
        # verbose_name = '自定义名称' #指定admin管理页面名称
        ordering = ['name']

# Book表
class Book(models.Model):
    id = models.AutoField(primary_key=True)  # 自增的ID主键
    # 创建一个varchar(64)的唯一的不为空的字段
    title = models.CharField(max_length=64, null=False, unique=True)
    # 和出版社关联的外键字段
    pub = models.ForeignKey(to="Publisher", on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    class Meta:
        # db_table = 'mytable' #自定义表名
        # verbose_name = '自定义名称' #指定admin管理页面名称
        ordering = ['title']

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, unique=True)
    book = models.ManyToManyField(to="Book")
    def __str__(self):
        return self.name

    class Meta:
        # db_table = 'mytable' #自定义表名
        # verbose_name = '自定义名称' #指定admin管理页面名称
        ordering = ['name']


class db_config(models.Model):
    id = models.AutoField(primary_key=True)
    db_name = models.CharField(max_length=10,null=False, unique=True)
    host = models.CharField(max_length=20)
    port = models.CharField(max_length=10)
    database = models.CharField(max_length=10)
    user = models.CharField(max_length=10)
    passwd = models.CharField(max_length=10)



