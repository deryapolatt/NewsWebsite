from django.shortcuts import render
from django.http import HttpResponse
from habergir.models import Haberler

def hosgeldiniz(request):
    return render(request,"websitesi/anasayfa.html",{"thaber": Haberler.objects.count(),
                                                     "haberler": Haberler.objects.all()})
