# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from models import vip_person
from models import vip_point

# Create your views here.
import json

def list_vip_person(req):
    limit = int(req.GET['limit'])
    page = int(req.GET['page'])
    person_list =  list(vip_person.objects.filter().values())
    resp ={
        "code": 0
        , "msg": ""
        , "count": "100"
        , "data":person_list[(page-1)*limit:page*limit]
    }
    print json.dumps(resp)
    return HttpResponse(json.dumps(resp), content_type="application/json")