# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import vip_good
from models import vip_order
from models import vip_person
from models import vip_point
from models import vip_server

# Register your models here.


class GoodAdmin(admin.ModelAdmin):
    list_display = ('good_name','good_price','good_notes')

class ServerAdmin(admin.ModelAdmin):
    list_display = ('server_name','server_price','server_notes')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_name',)

class PointAdmin(admin.ModelAdmin):
    list_display = ('point_value','point_last_value','point_last_time')

class PersonAdmin(admin.ModelAdmin):
    list_display = ('vip_name','vip_sex','vip_phone','vip_level','vip_notes')

admin.site.register(vip_good, GoodAdmin)
admin.site.register(vip_server, ServerAdmin)
admin.site.register(vip_order, OrderAdmin)
admin.site.register(vip_point, PointAdmin)
admin.site.register(vip_person, PersonAdmin)