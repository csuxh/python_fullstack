from django.db import models

# Create your models here.
# Create your models here.
class Author(models.Model):
    """
    作者
    """
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        # db_table = 'mytable' #自定义表名
        # verbose_name = '自定义名称' #指定admin管理页面名称
        app_label = 'd73_forms'
        ordering = ['name']

class BookType(models.Model):
    """
    图书类型
    """
    caption = models.CharField(max_length=64)
    def __str__(self):
        return self.caption

    class Meta:
        # db_table = 'mytable' #自定义表名
        # verbose_name = '自定义名称' #指定admin管理页面名称
        app_label = 'd73_forms'
        ordering = ['caption']

class Book(models.Model):
    """
    图书
    """
    name = models.CharField(max_length=64)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    pubdate = models.DateField()

    authors = models.ManyToManyField(Author)
    book_type = models.ForeignKey(BookType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        # db_table = 'mytable' #自定义表名
        # verbose_name = '自定义名称' #指定admin管理页面名称
        app_label = 'd73_forms'
        ordering = ['name']