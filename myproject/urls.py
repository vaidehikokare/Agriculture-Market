"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
"""
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import path
from app.views import home ,sell,insert ,seeds ,insert1 ,fer, insert2 , buy , seeds_buy , fer_buy ,crop_buy ,search ,crop_detail
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path("sell/",sell,name='sell'),
    path('buy/',buy,name='buy'),
     # path('', buy),
    # path("sell/",sell,name='sell'),
    # path('crop/',crop,name='crop'),
    path('crop_buy/',crop_buy,name='crop_buy'),
    path('seeds_buy/',seeds_buy,name='seeds_buy'),
    path('fer_buy/',fer_buy,name='fer_buy'),
    path('seeds/',seeds,name='seeds'),
    path('fer/',fer,name='fer'),
    path('insert/', insert, name='insert'),
     path('insert2/', insert2, name='insert2'),
    # path('sell/sell/', sell, name='sell'),
    path('insert1/', insert1, name='insert1'),
    path('crop_detail/<int:crop_id>/', crop_detail, name='crop_detail'),
    path('search',search,name='search')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)