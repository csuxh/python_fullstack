#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2018/9/11 11:06
from django import forms
from d73_forms import models


# class BookForm(forms.ModelForm):
#     class Meta:
#         model = models.BookType
#         fields = "__all__"
#         labels = {
#             "id", "编号",
#             "caption", "类型"
#         }

class cForm2(forms.Form):
    user = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={'class': 'c1'}),
        error_messages={'required': '用户名不能为空'}, )
    pwd = forms.CharField(max_length=4, min_length=2, required=True)
    email = forms.EmailField(error_messages={'required': '邮箱不能为空', 'invalid': '邮箱格式错误'})

    memo = forms.CharField(
        widget=forms.Textarea()
    )

    book_type = forms.ChoiceField(
        widget=forms.widgets.Select
    )

    # 直接写数据
    # user_type_choice = (
    #     (0, '普通用户'),
    #     (1, '高级用户'),
    # )
    # 通过BookType表查询信息，values_list拿到的是元组。id作为value显示，caption作为text在页面显示
    # user_type_choice = models.BookType.objects.values_list('id', 'caption')
    # book_type = forms.CharField(
    #     widget=forms.widgets.Select(choices=user_type_choice, attrs={'class': "form-control"}))

    # 写上以下代码就不用担心数据库添加了数据而不能及时获取了
    def __init__(self, *args, **kwargs):
        # 每次创建Form1对象时执行init方法
        super(cForm2, self).__init__(*args, **kwargs)

        self.fields['book_type'].widget.choices =models.BookType.objects.all().using('mysql_db').values_list('id', 'caption')

        # print(self.fields)
        # print(models.BookType.objects.all().values_list('id', 'caption'))