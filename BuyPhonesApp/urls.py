from xml.dom.minidom import Document
from django.conf import settings
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#URLConf
urlpatterns = [
    path("",views.homepage),
    path('phones/',views.all_phones),
    path('addNewPhone',views.addNewPhone),
    path('editPhone',views.editPhone),
    path('updatePhone',views.updatePhone),
    path('addPhone',views.addPhone),
    
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)