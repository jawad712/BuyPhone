from contextlib import nullcontext
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from manage import main
from .models import Mobile , Review ,Specs

# Create your views here.


def homepage(request):
    return render(request,'index.html')

def all_phones(request):
    try:
        mobiles = 0
        if(request.GET['search_keyword']):
            search_keyword = request.GET['search_keyword']
            mobiles = Mobile.objects.filter(mobile_name__contains=search_keyword)
        else:
            mobiles = Mobile.objects.all()
        
        return render(request,'shop.html',{'mobiles':mobiles})
    except:
        print('Something Went Wrong')
