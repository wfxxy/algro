#! /usr/bin/python
# encoding:utf-8

from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login, logout  #登入和登出

from django.contrib.auth.decorators import login_required  # 验证用户是否登录

def login_in(request):
    error_msg = ''
    if request.method == "POST":
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        user = authenticate(username=username,password=password)
#        return render(request, 'show_all.html')
        if user is not None and user.is_active:
            print("passed authencation",user)
            login(request,user)
            #return HttpResponseRedirect('show_all.html')
            return render(request,"show_all.html")
        else:
            error_msg = '登录失败'
            return render(request, "login.html", {'error_msg': error_msg})

    return render(request, "login.html", {'error_msg': error_msg})

def page_not_found(request):
   return render(request, '404.html')
# Create your views here.
