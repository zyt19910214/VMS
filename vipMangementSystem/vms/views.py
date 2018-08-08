# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import print_function
from __future__ import print_function
from __future__ import print_function
from __future__ import unicode_literals

from django.http import HttpResponse
from DB import Mysql
import json
import logging

logger = logging.getLogger('django')


def list_vip_person(req):
    """
    会员列表查询
    :param req:
    :return:
    """
    if req.method =='GET':
        sql = 'SELECT a.id, a.`name` AS vip_name, a.phone AS vip_phone, a.note AS vip_notes, a.sex AS vip_sex,' \
              ' b.point AS vip_person_point FROM person a LEFT JOIN point_detail b ON a.id = b.person_id  ORDER BY a.id desc'
    if req.method == 'POST':
        data = req.POST.copy()
        sql= "SELECT a.id, a.`name` AS vip_name, a.phone AS vip_phone, a.note AS vip_notes, a.sex AS vip_sex, b.point AS vip_person_point from (select * FROM person   WHERE `name`='%s') a LEFT JOIN point_detail b ON a.id = b.person_id  ORDER BY a.id desc" % (data['username'])

    db = Mysql()

    n_list = []
    resp = ''
    query_result = db.getAll(sql)
    db.dispose()
    # print (len(query_result))
    if  len(query_result)!=0:
        person_list = list(query_result)

        # print(len(person_list))
        # print req.GET
        limit = int(req.GET['limit'])
        page = int(req.GET['page'])

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
                "data": n_list[(page - 1) * limit:page * limit]
            }
    else:

        resp = {
            "code": 0,
            "msg": "",
            "count": 0,
            "data": n_list
        }
    logger.debug('【VIP人员接口数据】：' + json.dumps(resp))

    return HttpResponse(json.dumps(resp), content_type="application/json")


def add_vip_person(req):
    """
    会员添加
    :param req:
    :return:
    """
    # print (req)
    logger.debug('添加会员传入参数：'+str(req.POST))
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
        logger.debug('添加失败,手机号已存在')
    else:
        sql = "INSERT INTO person (`name`, `sex`, `phone`, `note`, `create_time`, `resrver1`)" \
              " VALUES('%s','%s','%s','%s',now(),NULL)" %(data['username'],data['sex'],data['phone'],data['desc'])
        logger.debug (sql)
        dd = db.insertOne(sql)
        db.dispose()
        if dd != 0:
            # 会员添加成功
            resp = {
                "code": 0,
                "msg": "success"
            }
            logger.debug('会员添加成功')
        else:
            # 会员添加失败
            resp = {
                "code": 1,
                "msg": "internal_exceptions"
            }
            logger.debug('服务异常,会员添加失败')
    return HttpResponse(json.dumps(resp), content_type="application/json")


def del_vip_person(req):
    """
    会员删除（单个/批量删除）
    :param req:
    :return:
    """

    id_list= req.POST.copy()['checkData']
    print (id_list)
    sql = 'DELETE FROM vms.person WHERE id IN (%s)'%(id_list)
    db = Mysql()
    count = (db.delete(sql))
    db.dispose()
    if count == len(id_list.split(",")):
        resp = {
            "code": 0,
            "msg": "success"
        }
    else:
        resp = {
            "code": 1,
            "msg": "internal_exceptions"
        }

    return HttpResponse(json.dumps(resp), content_type="application/json")


def edit_vip_person(req):
    """
    更新会员信息
    :param req:
    :return:
    """
    logger.debug('更新会员传入参数：' + str(req.POST))
    data = req.POST.copy()
    logger.debug(data)

    if data['sex'] == '男':
        data['sex'] = '1'

    else:
        data['sex'] = '0'
    db = Mysql()

    sql2 = "SELECT * from person where phone ='%s' and id != '%s'" %(data['phone'],data['id'])
    logger.debug(sql2)
    is_exist = db.getAll(sql2)

    if (is_exist):
        # 无法更新为已存在的手机号
        resp = {
            "code": 2,
            "msg": "phone_is_exist"
        }
        logger.debug('更新失败,手机号已存在')
    else:
        sql = "UPDATE person SET name = '%s',sex= '%s',phone='%s',note='%s',create_time = now() WHERE id=%s" % (data['username'], data['sex'], data['phone'], data['desc'],data['id'])
        logger.debug(sql)
        dd = db.update(sql)
        db.dispose()
        if dd != 0:
            # 会员更新成功
            resp = {
                "code": 0,
                "msg": "success"
            }
            logger.debug('更新成功')
        else:
            # 会员更新失败
            resp = {
                "code": 1,
                "msg": "internal_exceptions"
            }
            logger.debug('服务异常,更新失败')

    return HttpResponse(json.dumps(resp), content_type="application/json")




