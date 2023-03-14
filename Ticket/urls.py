"""Ticket URL Configuration

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
"""
from django.contrib import admin
from django.urls import path
from buyticket import views
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('signIN', views.signin, name='sign_in'),
    path('signUP', views.signup, name='sign_up'),
    path('logOUT', views.log_out, name='log_out'),
    #path('payform', views.user_form, name='credential'),
    path('info',views.acc_info , name="info"),
    path('update-login/password',views.update_login,name="update_login"),
    path('buyticket/paymethod',views.paymethod , name="method"),
    path('ErrorValidatingTransaction',views.errorvalidating, name="error"),
    path('mytickets',views.myticket , name="ticket"),
    path('pay',views.initiate_payment , name="initiate-payment"),
    path('verify',views.verify_payment , name="verify"),

]