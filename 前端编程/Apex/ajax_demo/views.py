from django.shortcuts import render,redirect, HttpResponse
from app01 import models

# Create your views here.

# login装饰器
def chk_login(f):
    def inner(request, *args, **kwargs):
        if request.session.get("is_login", False):
            return f(request, *args, **kwargs)
        else:
            next_page = request.get_full_path()
            print(next_page)
            return redirect("/login/?next={}".format(next_page))
    return inner


def login_page(request):
    error_msg = ""
    if request.method == "POST":  # 这里必须是大写的
        # 如果你是POST请求,我就取出提交的数据,做登录判断
        print(request.POST["email"])
        email = request.POST.get("email", None)
        pwd = request.POST.get("pwd", None)
        #print(email, pwd)
        # 做是否登陆成功的判断
        if email == "jack@qq.com" and pwd == "123456":
            # 登录成功
            # 回复一个特殊的响应,这个响应会让用户的浏览器请求指定的URL
            # return redirect("http://www.luffycity.com")
            request.session["is_login"] = True
            request.session["usr"] = "Jack"
            next_page = request.GET.get("next", False)
            print(next_page)
            if next_page:
                return redirect(next_page)
            else:
                ret = models.UserInfo.objects.all()
                return render(request, "index.html", {"user_list": ret})
        else:
            # 登录失败
            error_msg = "邮箱或密码错误"
    # 不是POST请求就走下面这一句
    return render(request, "login.html", {"error": error_msg})


@chk_login
def index(request):
    ss = request.session.session_key
    print(ss)
    request.session.set_expiry(7*24*60*60)
    return render(request, "index.html")

@chk_login
def user_list(request):
    # 去数据库中查询所有的用户
    # 利用ORM这个工具去查询数据库,不用自己去查询
    ret = models.UserInfo.objects.all()  # [UserInfo Object, UserInfo Object]
    print(ret[0].id, ret[0].name)
    # 打开user_list.html文件,


    return render(request, "ajax_demo/user_list.html", {"user_list": ret})

def page_list(request):
    ret = models.UserInfo.objects.all()
    max_page = 11    #页面显示多少个分页

    total_row = ret.count()
    print(total_row)
    per_row=12      #每一页显示多少行

    total_page, end_page = divmod(total_row, per_row)
    if end_page:
        total_page += 1
    print(total_page, end_page)

    try:
        page_num = int(request.GET.get("page", 1))
        print(page_num)
        if page_num > total_page:
            page_num = total_page
    except Exception as e:
        page_num = 1

    if total_page < max_page:
        max_page = total_page
    half_max_page = max_page//2

    #当前展示的数据
    data_start = (page_num-1)*per_row
    data_end = page_num*per_row

    #当前页面展示的页码
    page_start = page_num - half_max_page
    page_end = page_num + half_max_page
    if page_start <=1:
        page_start = 1
        page_end = max_page
    if page_end >= total_page:
        page_end = total_page
        page_start = total_page - max_page + 1

    #当前页面展示的数据
    page_data = ret[data_start:data_end]

    html_page_list = []
    #首页
    html_page_list.append('<li><a href="/ajax_demo/list/?page=1">首页</a></li>')

    #上一页
    if page_num <= 1:
        html_page_list.append('<li class="disabled"><a href="#"><span aria-hidden="true">&laquo;</span></a></li>')
    else:
        html_page_list.append('<li><a href="/ajax_demo/list/?page={}"><span aria-hidden="true">&laquo;</span></a></li>'.format((page_num-1)))

    #当前页
    for i in range(page_start, page_end + 1):
        if i == page_num:
            tmp = '<li class="active"><a href="/ajax_demo/list/?page={0}">{0}</a></li>'.format(i)
        else:
            tmp = '<li><a href="/ajax_demo/list/?page={0}">{0}</a></li>'.format(i)
        html_page_list.append(tmp)


    #下一页
    if page_num >= total_page:
        html_page_list.append('<li class="disabled"><a href="#"><span aria-hidden="true">&raquo;</span></a></li>')
    else:
        html_page_list.append('<li><a href="/ajax_demo/list/?page={}"><span aria-hidden="true">&raquo;</span></a></li>'.format(page_num + 1))

    #尾页
    html_page_list.append('<li><a href="/ajax_demo/list/?page={}">尾页</a></li>'.format(total_page))

    page_html = "".join(html_page_list)
    return render(request, "ajax_demo/翻页测试.html", {"user_list": page_data, "html_page_list":page_html})

@chk_login
def ajax_test(request):
    return render(request, "ajax_demo/ajax_test.html")

def ajax_add(request):
    print(request.GET.get("i1"))
    print(request.GET.get("i2"))
    a = int(request.GET.get("i1"))
    b = int(request.GET.get("i2"))
    return HttpResponse(a+b)


if __name__ == '__main__':
    for i in range(1000):
        name = "jack" + str(i)
        ret = models.UserInfo.objects.create(name="{}").format()




