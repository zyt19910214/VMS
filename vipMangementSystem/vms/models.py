# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class vip_person(models.Model):
    vip_name = models.CharField(max_length=20)
    vip_sex = models.IntegerField()
    vip_phone = models.CharField(max_length=20)
    vip_level = models.IntegerField()
    vip_notes = models.CharField(max_length=100,null=True,blank=True)
    vip_reserve1 = models.CharField(max_length=30,null=True,blank=True)
    vip_reserve2 = models.CharField(max_length=30,null=True,blank=True)

    def __unicode__(self):
        return self.vip_phone

class vip_server(models.Model):
    server_name = models.CharField(max_length=30)
    server_price = models.FloatField(max_length=8)
    server_notes = models.CharField(max_length=100,null=True,blank=True)
    server_reserve1 = models.CharField(max_length=30,null=True,blank=True)
    server_reserve2 = models.CharField(max_length=30,null=True,blank=True)

    def __unicode__(self):
        return self.server_name

class vip_good(models.Model):
    good_name = models.CharField(max_length=30)
    good_price = models.FloatField(max_length=8)
    good_notes = models.CharField(max_length=100,null=True,blank=True)
    good_reserve1 = models.CharField(max_length=30,null=True,blank=True)
    good_reserve2 = models.CharField(max_length=30,null=True,blank=True)

    def __unicode__(self):
        return self.good_name

class vip_order(models.Model):
    vip_person_id = models.IntegerField(default=0)
    order_name = models.CharField(max_length=50)
    order_good = models.ManyToManyField('vip_good')
    order_server = models.ManyToManyField('vip_server')
    def __unicode__(self):
        return self.order_name


class vip_point(models.Model):
    vip_person_id = models.IntegerField(default=0)
    point_value = models.FloatField(max_length=8)
    point_last_value = models.FloatField(max_length=8)
    point_last_time = models.DateTimeField('最后修改日期', auto_now = True)
    point_reserve1 = models.CharField(max_length=30,null=True,blank=True)

    def __unicode__(self):
        return str(self.point_value)
