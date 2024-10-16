from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from pymongo import MongoClient



def __init__(self):
     client = MongoClient('localhost', 27017)
    # self.db = client['database_name']


def index(request):
    request.session.setdefault('visits',0)
    request.session['visits']+=1
    context = {
        'visits':request.session['visits']
    }
    template =loader.get_template('admin/index.html')
    return HttpResponse(template.render(context,request))
