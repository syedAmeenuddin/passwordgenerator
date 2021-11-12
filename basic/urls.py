"""basic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
ye url mech puch location of files ku locate karna so
like index.html ye folder ke under hy
java file ye folder ke under hy like that :)
"""


from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from polls import views
urlpatterns = [
    # empty path ako main page ku refer kariga so
    path('admin/', admin.site.urls, name='admin'),
    path('', views.home, name='home'),
    path('secondscreen', views.ss, name='ss',),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
