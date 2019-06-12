from django.shortcuts import render

# Create your views here.

from django import forms
from django.forms import widgets
from . import cForm2
from app01 import models

class DjangoFrom(forms.Form):
    usr = forms.CharField(max_length=10, label="用户名")
    pwd = forms.CharField(
        min_length=6,
        label="密码",
        widget=widgets.PasswordInput(),
        error_messages={
            "min_length": "密码不能少于6位"
        }
    )
    email = forms.EmailField()


def django_form(request):
    form_obj = DjangoFrom(request.POST)
    if request.method == "POST":
        print(request.POST)
    return render(request, "d73/django_form.html", {"form_obj": form_obj})

def form2(request):
    form = cForm2.cForm2()
    # print(form.book_type)
    return render(request, "d73/form2.html", {"form":form})

from utils.db_pool import select_db
def select_test(request):
    # sql = '''
    #     select user_id, user_name from s_user limit 20
    # '''
    #
    # data =select_db(sql)
    # print(data)
    data = models.db_config.objects.all()
    print(data)
    return render(request, "d73/select_test.html", {"usr_list": data})