# from django.shortcuts import render

from django.shortcuts import render, redirect, HttpResponse
# import os

def tables(req):
    return render(req, "tables.html")
