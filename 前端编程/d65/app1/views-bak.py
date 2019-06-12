from django.shortcuts import render, redirect, HttpResponse
from app1 import models

# 展示出版社列表
def publisher_list(request):
    # 去数据库查出所有的出版社,填充到HTML中,给用户返回
    ret = models.Publisher.objects.all().order_by("id")
    return render(request, "publisher_list2.html", {"publisher_list": ret})

# 删除出版社的函数
def delete_publisher(request):
    print(request.GET)
    print("=" * 120)
    # 删除指定的数据
    # 1. 从URL的参数里面拿到将要删除的数据的ID值
    del_id = request.GET.get("id", None)  # 字典取值,娶不到默认为None
    # 如果能取到id值
    if del_id:
        # 去数据库删除当前id值的数据
        # 根据id值查找到数据
        del_obj = models.Publisher.objects.get(id=del_id)
        # 删除
        del_obj.delete()
        # 返回删除后的页面,跳转到出版社的列表页,查看删除是否成功
        return redirect("/publisher_list/")
    else:
        return HttpResponse("要删除的数据不存在!")


# URL分组匹配传参形式，删除出版社的函数
def delete_publisher2(request, del_id):
    # 删除指定的数据
    # 如果能取到id值
    if del_id:
        # 去数据库删除当前id值的数据
        # 根据id值查找到数据
        del_obj = models.Publisher.objects.get(id=del_id)
        # 删除
        del_obj.delete()
        # 返回删除后的页面,跳转到出版社的列表页,查看删除是否成功
        return redirect("/publisher_list/")
    else:
        return HttpResponse("要删除的数据不存在!")


from django.views import View
# CBV版 添加新的出版社
class AddPublisher(View):
    def get(self, request):
        print(request.path_info)
        print(request.body)
        print("=" * 120)
        return render(request, "add_publisher.html")

    def post(self, request):
        print(request.body)
        print("=" * 120)
        new_name = request.POST.get("publisher_name", None)
        if new_name:
            # 通过ORM去数据库里新建一条记录
            models.Publisher.objects.create(name=new_name)
            # 引导用户访问出版社列表页,查看是否添加成功  --> 跳转
            return redirect("/publisher_list/")
        else:
            error_msg = "出版社名字不能为空!"
            return render(request, "add_publisher.html", {"error": error_msg})


