#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2019/3/4 09:44
import web

urls = (
    '/$', 'index'
    '/view/(/d+)', 'View'
)


app = web.application(urls, globals())


class index:
    def GET(self, name):
        #name = 'jack'
        # input = web.input(name=None)
        # return render.page1(input.name)

        #  *******方式一********
        # render = web.template.render('templates/')
        # return render.page1(name)

        #  *******方式二********
        render = web.template.frender('templates/page1.html')
        return render(name)


class View:
    def GET(self, id):
        # id = 1
        print('id')
        return  'asfasdf'
        # post = get_post(int(id))
        # print(post)
        # return render.view(post)
    # def GET(self, id):
    #     print('1111')
    #     post = get_post(int(id))
    #     print(post)
    #     return render.view(post)

if __name__ == '__main__':
    app.run()