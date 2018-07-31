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


def list_vip_person(req):
    # print req.GET
    db = Mysql()
    person_list =  list(db.getAll('select a.id,a.`name` as vip_name,a.phone as vip_phone,a.note as vip_notes,a.sex as vip_sex,b.point as vip_person_point from person a,point_detail b WHERE a.id = b.person_id and a.name=\'温娜\'')
    )
    db.dispose()

    limit = int(req.GET['limit'])
    page = int(req.GET['page'])

    # person_list =  list(vip_person.objects.filter().values())

    resp ={
        "code": 0
        , "msg": ""
        , "count": len(person_list)
        , "data":person_list[(page-1)*limit:page*limit]
    }
    print '【VIP人员接口数据】：'+json.dumps(resp)

    return HttpResponse(json.dumps(resp), content_type="application/json")

