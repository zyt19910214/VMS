# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import print_function
from __future__ import print_function
from __future__ import print_function
from __future__ import unicode_literals

from django.http import HttpResponse
from DB import Mysql
import json


def list_vip_person(req):
    """
    会员列表查询
    :param req:
    :return:
    """
    db = Mysql()
    sql = 'SELECT a.id, a.`name` AS vip_name, a.phone AS vip_phone, a.note AS vip_notes, a.sex AS vip_sex,' \
          ' b.point AS vip_person_point FROM person a LEFT JOIN point_detail b ON a.id = b.person_id  ORDER BY a.id'
    person_list = list(db.getAll(sql))
    db.dispose()
    # print(person_list)
    # print(len(person_list))
    # print req.GET
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
    # print(len(n_list))
    # print(len(n_list[(page - 1) * limit:page * limit]))

    resp = {
        "code": 0,
        "msg": "",
        "count": len(n_list),
        "data": n_list[(page-1)*limit:page*limit]
    }
    print ('【VIP人员接口数据】：' + json.dumps(resp))

    return HttpResponse(json.dumps(resp), content_type="application/json")


def add_vip_person(req):
    """
    会员添加
    :param req:
    :return:
    """
    # print (req)
    print ('添加会员传入参数：'+str(req.POST))
    data = req.POST.copy()
    if data['sex'] == '男':
        data['sex'] = '1'
    else:
        data['sex'] = '0'

    db = Mysql()
    is_exist = db.getAll('SELECT * from person where phone =\'%s\''%(data['phone']))
    if (is_exist):
        # 已存在手机号无法注册会员
        resp = {
            "code": 2,
            "msg": "phone_is_exist"
        }
        print('添加失败,手机号已存在')
    else:
        sql = "INSERT INTO person (`name`, `sex`, `phone`, `note`, `create_time`, `resrver1`)" \
              " VALUES('%s','%s','%s','%s',now(),NULL)" %(data['username'],data['sex'],data['phone'],data['desc'])
        print (sql)
        dd = db.insertOne(sql)
        db.dispose()
        if dd != 0:
            # 会员添加成功
            resp = {
                "code": 0,
                "msg": "success"
            }
            print('会员添加成功')
        else:
            # 会员添加失败
            resp = {
                "code": 1,
                "msg": "internal_exceptions"
            }
            print('服务异常,会员添加失败')
    return HttpResponse(json.dumps(resp), content_type="application/json")

def del_vip_person(req):
    print(req.POST)

    resp = {
        "code": 1,
        "msg": "internal_exceptions"
    }


    return HttpResponse(json.dumps(resp), content_type="application/json")






