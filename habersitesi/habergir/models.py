from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

def get_setinel_user():
    return get_user_model().objects.get_or_create(username='deleted,')[0]

class Haberler(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='Kullanıcı',on_delete=models.SET(get_setinel_user))
    baslik = models.CharField(max_length=200)
    kullanici_adi = models.CharField(max_length=200)
    metin = models.TextField()
    gorsel =models.ImageField(null=True, blank=True)



    def __str__(self):
        return f"{self.baslik}"
# Create your models here.
