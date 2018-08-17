from django.shortcuts import render

from . import models
from .forms import User_input
from .models import Data
from django.http import HttpResponseRedirect
from django import http 
def home(request):

    my_data = Data.objects.all()
    #(request.POST or None)
    contect ={

        'my_data': my_data
    }
    return render(request, 'home.html', contect)


def my_form(request):
    msg=''
    my_user_input = User_input (request.POST or None)
    if my_user_input.is_valid():
       save_data = models.Data()
       save_data.name = my_user_input.cleaned_data['name']
       save_data.date = my_user_input.cleaned_data['date']
       save_data.description = my_user_input.cleaned_data['description']
       save_data.save()
       msg='Data is saved'
       #my_user_input = EmployeeForm()
       return http.HttpResponseRedirect('/user_input/')
    #    if my_user_input.is_valid():
    #       my_user_input.full_clean()


       #my_user_input.name = my_user_input.name.clean(self).strip()

    contect ={

        'msg': msg,
        'my_user_input': my_user_input,
    }
    return render(request, 'user_input.html', contect)
