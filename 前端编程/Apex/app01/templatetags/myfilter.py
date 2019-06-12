from django import template
from datetime import datetime

#这里名字必须是register，不然识别不了
register = template.Library()

#自定义filter
@register.filter(name="addDate")
def add_date(arg):
    now = datetime.now()
    return "{} {}".format(arg, now)

#最多传两个参数
@register.filter(name="addStr")
def add_date(arg, arg2):
    """
    第一个参数永远是管道符前面那个变量
    :param arg: 道符前面那个变量
    :param arg2: 冒号后面的变量
    :return:
    """
    return "{} {}".format(arg, arg2)

#自定义tags   可以传多个参数
@register.simple_tag(name="myTag")
def plus(arg1, arg2, arg3):
    return "{}+ {}+ {}".format(arg1, arg2, arg3)

#自定义inclusion_tag
@register.inclusion_tag("template.html")
def ge_list(n):
    n=1 if n<1 else int(n)
    data = ["第{}章".format(i) for i in range(n)]
    return {"result": data}