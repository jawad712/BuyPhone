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

def addPhone(request):
    try:
        mobile_name = request.GET.get('mobile_name',False)
        mobile_img = "restaurant_images/"+request.GET.get('mobile_img',False)
        mobile_desc = request.GET.get('mobile_desc',False)
        date = request.GET.get('date',False)
        mobile_ram = request.GET.get('mobile_ram',False)
        mobile_cpu = request.GET.get('mobile_cpu',False)
        mobile_storage = request.GET.get('mobile_storage',False)
        mobile_color = request.GET.get('mobile_color',False)
        mobile_other_features = request.GET.get('mobile_other_features',False)
        date = request.GET.get('date',False)
        specs = Specs.objects.create(mobile_ram=mobile_ram,mobile_cpu=mobile_cpu,mobile_storage=mobile_storage,mobile_color=mobile_color,mobile_other_features=mobile_other_features,date=date)
        Mobile.objects.create(mobile_name=mobile_name,mobile_img=mobile_img,mobile_desc=mobile_desc,date=date,id_id=specs.id)
        mobiles = Mobile.objects.all()
        return render(request,'managePhones.html',{'mobiles':mobiles})
    except:
        print("something went wrong while adding restaurant")    
def addNewPhone(request):
    return render(request,'addPhone.html')

def editPhone(request):
    mob_id = request.GET['mob_id']
    return render(request,'editPhone.html',{"mob_id":mob_id})

def updatePhone(request):
    mobile_name = request.GET.get('mobile_name',False)
    mob_id = request.GET.get('mob_id',False)
    Mobile.objects.filter(id_id=mob_id).update(mobile_name=mobile_name)
    mobiles = Mobile.objects.all()
    return render(request,'managePhones.html',{'mobiles':mobiles})

def managePhone(request):
    try:
        mobiles = Mobile.objects.all()
        return render(request,'managePhones.html',{'mobiles':mobiles})
    except:
        print("something Went Wrong in Manage restaurant")    
def deletePhone(request):
    try:
        Mobile.objects.get(id_id=request.GET['mob_id']).delete()
        mobiles = Mobile.objects.all()
        return render(request,'managePhones.html',{'mobiles':mobiles})
    except:
       print("something Went Wrong while deleting restaurant")

def show_PhoneDetails(request):
    try:
        mob_id = request.GET['mob_id']
        mobiles = Mobile.objects.get(id_id=mob_id)
        specs = Specs.objects.get(id = mob_id)
        return render(request,'phoneDetails.html',{"mobiles":mobiles , "specs":specs})    
    except:
        print('Something Went Wrong')


