from django.contrib import admin
from django.urls import path, include #include enables us to get the template from another app
from . import views #this enables us to interact with views.py
from django.contrib.staticfiles.urls import staticfiles_urlpatterns #this is for static assets folder where we put css
from django.conf.urls.static import static #this is for media purposes
from django.conf import settings #this is also for media purposes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="home"),
    path('weather/', include('station.urls'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)