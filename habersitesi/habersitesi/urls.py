from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from habergir.views import habersayfasi
from websitesi.views import hosgeldiniz

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',hosgeldiniz,name="anasayfa"),
    path("haber/",include("habergir.urls")),
    path("accounts/",include("accounts.urls")),




]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

