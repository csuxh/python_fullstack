from django.shortcuts import render,HttpResponse, redirect
from functools import wraps
# Create your views here.


def login_decrator(f):
    @wraps(f)
    def inner(*args, **kwargs):
        print("call login")
        if args[0].COOKIES.get("is_login", False):
            return f(*args, **kwargs)
        else:
            print("pls login")
            return redirect("/app03/login")
    return inner


def login(request):
    if request.method == "POST":
        usr_name = request.POST.get("name")
        pwd = request.POST.get('pwd')
        if usr_name == "jack" and pwd == "xiahang":
            ret = redirect("/app03/home/")
            ret.set_cookie("is_login", True, max_age=10)
            return ret
    return render(request, "login.html")


@login_decrator
def home(request):
    # if request.COOKIES.get("is_login", False):
    #     return render(request, "publisher_list2.html")
    # else:
    #     return redirect("/app03/login")
    return redirect("/app03/login")


