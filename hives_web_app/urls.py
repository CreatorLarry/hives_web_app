"""
URL configuration for hives_web_app project.

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
from django.contrib import admin
from django.urls import path

from main import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),

    path('booking/', views.booking, name='booking'),

    path('order/', views.order, name='order'),

    path('order/form/', views.order_detail_view, name='order_detail_view'),

    path('order-list/', views.order_list, name='order_list'),

    path('thank-you/', views.thank_you, name='thank_you'),

    path('thank-you-order/', views.thank_you_order, name='thank_you_order'),

    path('about/', views.about, name='about'),

    path('services/', views.services, name='services'),

    path('events/', views.events, name='events'),

    path('menu/', views.menu, name='menu'),

    path('contact/', views.contact_view, name='contact'),

    path('admin/', admin.site.urls),
]
