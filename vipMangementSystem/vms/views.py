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

db = Mysql()
def list_vip_person(req):
    person_list =  list(db.getAll('select a.id,a.`name` as vip_name,a.phone as vip_phone,a.note as vip_notes,a.sex as vip_sex,b.point as vip_person_point from person a,point_detail b WHERE a.id = b.person_id and a.name=\'温娜\'')
    )
    db.dispose()
    print person_list
    limit = 10
    page = 1
    # person_list =  list(vip_person.objects.filter().values())

    resp ={
        "code": 0
        , "msg": ""
        , "count": "100"
        , "data":person_list[(page-1)*limit:page*limit]
    }
    print json.dumps(resp)
    return HttpResponse(json.dumps(resp), content_type="application/json")

def sss():
    db.getAll()