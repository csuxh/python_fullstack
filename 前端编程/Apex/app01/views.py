from django.shortcuts import render, redirect, HttpResponse
import os
from django.http import JsonResponse
from . import models
# Create your views here.
# 专门用来放函数


# 登录的函数
def login(request):
    error_msg = ""
    if request.method == "POST":  # 这里必须是大写的
        # 如果你是POST请求,我就取出提交的数据,做登录判断
        print(request.POST["email"])
        email = request.POST.get("email", None)
        pwd = request.POST.get("pwd", None)
        print(email, pwd)
        # 做是否登陆成功的判断
        if email == "jack@qq.com" and pwd == "123456":
            # 登录成功
            # 回复一个特殊的响应,这个响应会让用户的浏览器请求指定的URL
            # return redirect("http://www.luffycity.com")
            ret = models.UserInfo.objects.all()
            return render(request, "app01/user_list.html", {"user_list": ret})
        else:
            # 登录失败
            error_msg = "邮箱或密码错误"
    # 不是POST请求就走下面这一句
    return render(request, "app01/login.html", {"error": error_msg})


# 展示所有的用户的函数
def user_list(request):
    # 去数据库中查询所有的用户
    # 利用ORM这个工具去查询数据库,不用自己去查询
    page_num = request.GET.get("page")
    total_count = models.UserInfo.objects.all().count()
    from utils.mypage import Page
    page_obj = Page(page_num, total_count, per_page=10, url_prefix="/app01/user_list/", max_page=11, )
    ret = models.UserInfo.objects.all()[page_obj.start:page_obj.end]
    print(ret)
    page_html = page_obj.page_html()
    return render(request, "app01/user_list2.html", {"user_list": ret, "page_html": page_html})

    # ret = models.UserInfo.objects.all()  # [UserInfo Object, UserInfo Object]
    # print(ret[0].id, ret[0].name)
    # 打开user_list.html文件,
    # return render(request, "app01/user_list2.html", {"user_list": ret})



# 添加用户的函数
def add_user(request):
    if request.method == "POST":
        # 用户填写了新的用户名,并发送了POST请求过来
        new_name = request.POST.get("username", None)
        # 去数据库中新创建一条用户记录
        models.UserInfo.objects.create(name=new_name)
        # return HttpResponse("添加成功!")
        # 添加成功后直接跳转到用户列表页
        return redirect("/app01/user_list/")

    # 第一个请求页面的时候,就返回一个页面,页面上有两个框让用户填写
    return render(request, "add_user.html")


def publisher_list(request):
    ret = models.Publisher.objects.all().order_by("id")
    return render(request, 'app01/publisher_list2.html', {"publisher_list": ret})

def add_publisher(request):
    err_msg = ""
    if request.method == "POST":
        new_name = request.POST.get("publisher_name")
        if new_name:
            models.Publisher.objects.create(name=new_name)
            return redirect("/app01/publisher_list/")
        else:
            err_msg = "名字不能为空"
    return render(request, 'add_publisher.html', {"err_msg": err_msg})


def delete_publisher(request):
    del_id = request.GET.get("id", None)
    if del_id:
        del_obj = models.Publisher.objects.get(id=del_id)
        del_obj.delete()
        return redirect('/app01/publisher_list/')
    else:
        return HttpResponse("数据不存在")

def edit_publisher(request):
    if request.method == "POST":
        #获取修改后的名字
        err_msg = ""
        edit_id = request.POST.get("publisher_id")
        new_name = request.POST.get("publisher_name")
        edit_obj = models.Publisher.objects.get(id=edit_id)
        if new_name:
            edit_obj.name = new_name
            edit_obj.save()
            return redirect("/app01/publisher_list/")
        else:
            err_msg = "不能为空"
            return render(request, 'edit_publisher.html', {'publisher': edit_obj ,'err_msg': err_msg})
    edit_id = request.GET.get("id", None)
    if edit_id:
        edit_obj = models.Publisher.objects.get(id=edit_id)
        return render(request, "edit_publisher.html", {'publisher': edit_obj})
    else:
        return HttpResponse("出版社不存在")

def book_list(request):
    ret = models.Book.objects.all().order_by("id")
    return render(request, 'app01/book_list2.html', {"book_list": ret})


def add_books(request):
    if request.method == "POST":
        new_book = request.POST.get("book_name")
        publisher_id = request.POST.get("publisher")
        print(new_book)
        print(publisher_id)
        if new_book:
            models.Book.objects.create(title=new_book, pub_id=publisher_id)
            return redirect("/book_list/")
    else:
        ret = models.Publisher.objects.all().order_by("id")
        # models.Publisher.objects.all().order_by("id")
        print(ret)
        return render(request, "app01/add_books.html", {'publisher_list': ret})

def delete_book(request):
    del_id = request.GET.get("id", None)
    if del_id:
        del_obj = models.Book.objects.get(id=del_id)
        del_obj.delete()
        return redirect('/app01/book_list/')
    else:
        return HttpResponse("数据不存在")

def edit_books(request):
    if request.method == "POST":
        #获取修改后的名字
        err_msg = ""
        edit_id = request.POST.get("book_id")
        edit_name = request.POST.get("book_name")
        pub_id = request.POST.get("publisher")
        print(edit_id, edit_name, pub_id)
        edit_obj = models.Book.objects.get(id=edit_id)
        if edit_id:
            edit_obj.title = edit_name
            edit_obj.pub_id = pub_id
            edit_obj.save()
            return redirect("/app01/book_list/")
        else:
            err_msg = "不能为空"
            return render(request, 'app01/edit_publisher.html', {'publisher': edit_obj ,'err_msg': err_msg})

    edit_id = request.GET.get("id", None)
    if edit_id:
        book_obj = models.Book.objects.get(id=edit_id)
        pub_obj = models.Publisher.objects.all()
        return render(request, "app01/edit_books.html", {"publisher_list": pub_obj,"book_obj": book_obj})
    else:
        return HttpResponse("出版社不存在")


#django 模板语言测试
# def template_test(request):
#     name = "jackxia"
#     age = 25
#     return render(request, "template_test.html", {"name": name, "age": age})
def template_test(request):
    l = [11, 22, 33]
    d = {"name": "alex"}
    from datetime import datetime
    now = datetime.now()
    class Person(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def dream(self):
            return "{} is dream...".format(self.name)

    Alex = Person(name="Alex", age=34)
    Egon = Person(name="Egon", age=9000)
    Eva_J = Person(name="Eva_J", age=18)

    person_list = [Alex, Egon, Eva_J]
    return render(request, "app01/template_test.html", {"ss": "hello , how are you", "now": now, "person_list": person_list,"size":123567})

def test(request):
    book_obj = models.Book.objects.all()
    for i in book_obj:
        print(i.id)
    return HttpResponse("OK")


def upload(request):
    # 文件上传
    if request.method == "POST":
        file_name = request.FILES.get("upload_file")
        # print(type(file_name))
        with open(os.path.join("upload/",str(file_name)), "wb") as f:
            for i in request.FILES["upload_file"].chunks():
                f.write(i)
        return HttpResponse("上传成功")
    return render(request, "app01/file_upload.html")


def json_test(request):
    data = {"id": 1101, "name": "john ",
            }
    # import json
    # return HttpResponse(json.dumps(data))
    return JsonResponse(data)
    # return JsonResponse(data, safe=False) 校验是否是字典

#分页版本
# def depts(request):
#     # 从URL取参数
#     page_num = request.GET.get("page")
#     print(page_num, type(page_num))
#     # 总数据是多少
#     total_count = models.Dept.objects.all().count()
#     from utils.mypage import Page
#     page_obj = Page(page_num, total_count, per_page=10, url_prefix="/depts/", max_page=11, )
#
#     ret = models.Dept.objects.all()[page_obj.start:page_obj.end]
#     print(ret)
#
#     page_html = page_obj.page_html()
#     return render(request, "dept.html", {"depts": ret, "page_html": page_html})