"""vipMangementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from vms.views import list_vip_person as views_list_vip_person
from vms.views import add_vip_person as views_add_vip_person
from vms.views import del_vip_person as views_del_vip_person
from vms.views import edit_vip_person as views_edit_vip_person
from vms.views import list_good as views_list_good
urlpatterns = [
    url(r'^listVipPerson/$',views_list_vip_person),
    url(r'^addVipPerson/$', views_add_vip_person),
    url(r'^delVipPerson/$', views_del_vip_person),
    url(r'^editVipPerson/$', views_edit_vip_person),
    url(r'^listGood/$', views_list_good),


]
