from django.shortcuts import render,get_object_or_404,redirect
from django.forms import modelform_factory
from .models import Haberler
from django.contrib.auth.models import User

def habersayfasi(request,id):
    haber=get_object_or_404(Haberler,pk=id)
    return render(request,"detay/haber_sayfasi.html",{"haber": haber})

def gorsellistesi(request):
    return render(request,'detay/gorsel.html')


HaberFormu=modelform_factory(Haberler,exclude=[])

def haberOlustur(request):
    if request.method =="POST": #kullanıcı formu doldurmuş anlamına geliyor
        form=HaberFormu(request.POST or None,request.FILES or None)  #veri tabanına kaydediyor
        if form.is_valid():
            form.save()
           # haber= form.save(commit=False) #formu kaydet
            #haber.user=request.user
            #haber.save()
            return redirect("anasayfa") #kaydettikten sonra ana sayfaya gönderiyor
    else:
        haberForm= HaberFormu()
    return render (request,"detay/haber_olustur.html",{"form":haberForm})



# Create your views here.
