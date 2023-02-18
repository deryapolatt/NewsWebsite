from django.urls import path
from .views import habersayfasi,haberOlustur

urlpatterns=[
    path("<int:id>",habersayfasi,name='haberlerigoster'),
    path("haber-olustur",haberOlustur,name='haberOlustur'),


]