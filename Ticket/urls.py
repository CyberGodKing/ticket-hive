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
from django.conf.urls.static import static


urlpatterns = [
    path('adminfupresocia2023/', admin.site.urls),
    path('', views.home, name='home'),
    path('previous_accesstoken', views.signin, name='sign_in'),
    path('ticket/accesstoken', views.signup, name='sign_up'),
    path('buyticket/paymethod',views.paymethod , name="method"),
    path('ErrorValidatingTransaction',views.errorvalidating, name="error"),
    path('mytickets',views.myticket , name="ticket"),
    path('pay/regular',views.initiate_payment , name="initiate-payment"),
    path('pay/vip',views.initiate_paymentvip , name="initiate-paymentvip"),
    path('pay/premium_vip',views.initiate_paymentpremium , name="initiate-paymentpremium"),
    path('verify',views.verify_payment , name="verify"),
    path('activate/<str:id>',views.activateticket , name="activate"),
    path('ticket-type',views.tickettype , name="tickettype"),

]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
