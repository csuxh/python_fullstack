#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:csuxh
# datetime:2019/3/5 09:54
import web
from web import form

render = web.template.render('templates/')

urls = ('/', 'index')
app = web.application(urls, globals())

myform = form.Form(
    form.Textbox("CN_name"),
    form.Textbox("Accounts id",
                 form.notnull,
                 form.regexp('\d+', 'Must be a digit'),
                 form.Validator('Must be more than 5', lambda x: int(x) > 5)),
    form.Textarea('Accounts Code'),
    form.Checkbox('customer'),
    form.Dropdown('COMPANY', ['XQW-SHANGHAI', 'APEX-WUHAN', 'APEX-SHANGHAI']))


class index:
    def GET(self):
        form = myform()
        # make sure you create a copy of the form by calling it (line above)
        # Otherwise changes will appear globally
        print(form.render())
        return render.form_test(form)

    def POST(self):
        form = myform()
        if not form.validates():
            print(form.render())
            return render.form_test(form)
        else:
            # form.d.boe and form['boe'].value are equivalent ways of
            # extracting the validated arguments from the form.
            return "Grrreat success! CN_name: %s, Accounts id: %s" % (form.d.CN_name, form['Accounts id'].value)


if __name__ == "__main__":
    web.internalerror = web.debugerror
    app.run()