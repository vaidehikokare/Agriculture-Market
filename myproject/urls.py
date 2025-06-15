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
from app.views import buy_signup , buy_register_view ,buy_login1 , crop_display ,view_details_crop , crop_delete , buy_product , confirm_order ,orders ,order_action ,accept_order,reject_order
from app.views import home ,sell,insert ,seeds ,insert1 ,fer, insert2 , buy , seeds_buy , fer_buy ,crop_buy ,search ,crop_detail,sell_login,sell_signup,sell_register_view,sell_login1,buy_login
from app.views import search_seeds , agri_weather_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('sell_register_view/',sell_register_view,name='sell_register_view'),
    path("sell/",sell,name='sell'),
    path("sell_login/",sell_login,name='sell_login'),
    path("sell_signup/",sell_signup,name='sell_signup'),
    path('buy/',buy,name='buy'),
     # path('', buy),
    # path("sell/",sell,name='sell'),
    # path('crop/',crop,name='crop'),
    path('crop_buy/',crop_buy,name='crop_buy'),
    path('seeds_buy/',seeds_buy,name='seeds_buy'),
    path('fer_buy/',fer_buy,name='fer_buy'),
    path('seeds/',seeds,name='seeds'),
    path('fer/',fer,name='fer'),
    path('insert/<int:user_id>/', insert, name='insert'), 
    path('insert2/', insert2, name='insert2'),
    # path('sell/sell/', sell, name='sell'),
    path('insert1/', insert1, name='insert1'),
    path('crop_detail/<int:crop_id>/', crop_detail, name='crop_detail'),
    path('search',search,name='search'),
    path('sell_login1/',sell_login1,name='sell_login1'),
    path('buy_login/',buy_login,name='buy_login'),
    path('buy_signup/',buy_signup,name='buy_signup'),
    path('buy_register_view/',buy_register_view,name='buy_register_view'),
    path('buy_login1/',buy_login1,name='buy_login1'),
    path('crop_display/',crop_display,name='crop_display'),
    path('view_details_crop/<int:crop_id>/',view_details_crop,name='view_details_crop'),
    path('crop_delete/<int:crop_id>/',crop_delete,name='crop_delete'),
    path('buy_product/<int:crop_id>/',buy_product,name='buy_product'),
    path('confirm_order/<int:crop_id>/',confirm_order,name='confirm_order'),
    path('orders/',orders,name='orders'),
    path('order_action/<int:order_id>/',order_action,name='order_action'),
    path('accept_order/<int:order_id>/',accept_order,name='accept_order'),
    path('reject_order/<int:order_id>/',reject_order,name='reject_order'),
    path('search_seeds/',search_seeds,name='search_seeds'),
    path('agri_weather_view/', agri_weather_view, name='agri_weather_view'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)