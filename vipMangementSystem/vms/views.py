# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from models import vip_person
from models import vip_point
from DB import Mysql

# Create your views here.
import json
import time

def list_vip_person(req):
    # print req.GET
    db = Mysql()
    sql = 'SELECT a.id, a.`name` AS vip_name, a.phone AS vip_phone, a.note AS vip_notes, a.sex AS vip_sex, b.point AS vip_person_point' \
          ' FROM person a LEFT JOIN point_detail b ON a.id = b.person_id  ORDER BY a.id'
    person_list = list(db.getAll(sql))
    print person_list
    print len(person_list)
    db.dispose()

    limit = int(req.GET['limit'])
    page = int(req.GET['page'])

    # person_list =  list(vip_person.objects.filter().values())
    n_list = []
    for x in person_list:
        if x['vip_person_point'] is None:
            x['vip_person_point'] = 0
        if x['vip_sex'] == 0:
            x['vip_sex'] = '女'
        elif x['vip_sex'] == 1:
            x['vip_sex'] = '男'
        else:
            x['vip_sex'] = '未知'
        n_list.append(x)
    print len(n_list)
    print len(n_list[(page-1)*limit:page*limit])
    resp ={
        "code": 0
        , "msg": ""
        , "count": len(n_list)
        , "data":n_list[(page-1)*limit:page*limit]
    }
    print '【VIP人员接口数据】：'+json.dumps(resp)

    return HttpResponse(json.dumps(resp), content_type="application/json")

def add_vip_person(req):
    print req
    print req.POST
    data = req.POST.copy()
    if data['sex'] == '男':
        data['sex'] = '1'
    else:
        data['sex'] = '0'

    db = Mysql()
    sql = "INSERT INTO person (`name`, `sex`, `phone`, `note`, `create_time`, `resrver1`)" \
          " VALUES('%s','%s','%s','%s',now(),NULL)"%(data['username'],data['sex'],data['phone'],data['desc'])
    print sql
    dd = db.insertOne(sql)
    db.dispose()
    if dd == 0:
        resp = {
            "code": 1
            , "msg": "success"
        }
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        resp = {
            "code": 0
            , "msg": "success"
        }
        return HttpResponse(json.dumps(resp), content_type="application/json")





