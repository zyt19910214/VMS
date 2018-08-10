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


# 会员增删改查
def list_vip_person(req):
    """
    会员列表查询
    :param req:
    :return:
    """
    data = req.GET.copy()
    sql = 'SELECT a.id, a.`name` AS vip_name, a.phone AS vip_phone, a.note AS vip_notes, a.sex AS vip_sex,' \
          ' b.point AS vip_person_point FROM person a LEFT JOIN point_detail b ON a.id = b.person_id  ORDER BY a.id desc'

    if 'phone' in  data:
        phone = data['phone']
        sex = data['sex']
        if phone != '' and sex == '2':
            sql = "SELECT a.id, a.`name` AS vip_name, a.phone AS vip_phone, a.note AS vip_notes, a.sex AS vip_sex, b.point AS vip_person_point from (select * FROM person   WHERE `phone`='%s') a LEFT JOIN point_detail b ON a.id = b.person_id  ORDER BY a.id desc" % (
            phone)
        elif phone == '' and sex != '2':
            sql = "SELECT a.id, a.`name` AS vip_name, a.phone AS vip_phone, a.note AS vip_notes, a.sex AS vip_sex, b.point AS vip_person_point from (select * FROM person   WHERE `sex` ='%s') a LEFT JOIN point_detail b ON a.id = b.person_id  ORDER BY a.id desc" % (
                sex)
        elif phone != '' and sex != '2':
            sql = "SELECT a.id, a.`name` AS vip_name, a.phone AS vip_phone, a.note AS vip_notes, a.sex AS vip_sex, b.point AS vip_person_point from (select * FROM person   WHERE `phone`='%s' AND `sex` ='%s') a LEFT JOIN point_detail b ON a.id = b.person_id  ORDER BY a.id desc" % (
                phone,sex)
        else:
            pass

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
    # print (id_list)
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


# 商品增删改查
def list_good(req):
    """
    商品查询
    :param req:
    :return:
    """
    data = req.GET.copy()
    sql = 'select a.*,b.name as type from good a INNER JOIN good_category b ON a.good_category_id = b.id ORDER BY uploadtime desc'
    if 'title' in data:
        good_name = data['title']
        good_type = data['label']
        if good_name != '' and good_type == '':
            sql = "select a.*,b.`name` as type from(select * from good where `name`='%s')a INNER JOIN good_category b ON a.good_category_id = b.id ORDER BY a.uploadtime desc"%(good_name)
        elif good_name == '' and good_type != '':
            sql = "select a.*,b.`name` as type from(select * from good )a INNER  JOIN (select * from good_category where `id`='%s')  b ON a.good_category_id = b.id ORDER BY a.uploadtime desc"%(good_type)
        elif good_name != '' and good_type != '':
            sql ="select a.*,b.`name` as type from(select * from good where `name`='%s' )a INNER  JOIN (select * from good_category where `id`='%s')  b ON a.good_category_id = b.id ORDER BY a.uploadtime desc"%(good_name,good_type)
        else:
            pass
    db = Mysql()

    g_list = []
    resp = ''
    query_result = db.getAll(sql)
    db.dispose()

    if  len(query_result)!=0:
        good_list = list(query_result)

        for x in good_list:
           if x['uploadtime'] != '':
               x['uploadtime'] = str(x['uploadtime'])
           g_list.append(x)
        limit = int(req.GET['limit'])
        page = int(req.GET['page'])
        resp = {
            "code": 0,
            "msg": "",
            "count": len(g_list),
            "data": g_list[(page - 1) * limit:page * limit]
        }
    else:

        resp = {
            "code": 0,
            "msg": "",
            "count": 0,
            "data": g_list
        }


    logger.debug('【商品接口数据】：' + json.dumps(resp))

    return HttpResponse(json.dumps(resp), content_type="application/json")


def add_good(req):
    """
    添加商品
    :param req:
    :return:
    """
    logger.debug('添加商品传入参数：' + str(req.POST))
    data = req.POST.copy()

    db = Mysql()
    is_exist = db.getAll('SELECT * from good where `name` =\'%s\'' % (data['title']))

    if (is_exist):
        # 已存在该商品无法添加
        resp = {
            "code": 2,
            "msg": "good_is_exist"
        }
        logger.debug('添加失败,商品已存在')
    else:
        count = str(int(data['add_count'])+int(data['count']))
        sql = "INSERT INTO `good` (`name`, `good_category_id`, `price`, `uploadtime`, `status`) VALUES ('%s', '%s', '%s', now(), '%s');"%(data['title'],data['type'],data['price'],count)
        logger.debug(sql)
        dd = db.insertOne(sql)
        db.dispose()
        if dd != 0:
            # 会员添加成功
            resp = {
                "code": 0,
                "msg": "success"
            }
            logger.debug('商品添加成功')
        else:
            # 会员添加失败
            resp = {
                "code": 1,
                "msg": "internal_exceptions"
            }
            logger.debug('服务异常,商品添加失败')
    return HttpResponse(json.dumps(resp), content_type="application/json")


def edit_good(req):
    """
    编辑商品
    :param req:
    :return:
    """
    logger.debug('更新商品传入参数：' + str(req.POST))
    data = req.POST.copy()
    logger.debug(data)

    sql2 = "SELECT * from good where `name` ='%s' and id != '%s'" % (data['title'], data['id'])
    logger.debug(sql2)

    db = Mysql()
    is_exist = db.getAll(sql2)

    if(is_exist):
        # 无法更新为已存在商品
        resp = {
            "code": 2,
            "msg": "phone_is_exist"
        }
        logger.debug('更新失败,商品已存在')
    else:
        count = str(int(data['count'])+int(data['add_count']))
        sql = "UPDATE good SET  `name` = '%s',good_category_id= '%s',price='%s',status='%s',uploadtime = now() WHERE id=%s" % (
        data['title'], data['type'], data['price'], count, data['id'])
        logger.debug(sql)
        dd = db.update(sql)
        db.dispose()
        if dd != 0:
            # 会员更新成功
            resp = {
                "code": 0,
                "msg": "success"
            }
            logger.debug('商品更新成功')
        else:
            # 会员更新失败
            resp = {
                "code": 1,
                "msg": "internal_exceptions"
            }
            logger.debug('服务异常,商品更新失败')

    return HttpResponse(json.dumps(resp), content_type="application/json")


def del_good(req):
    """
    商品 删除（单个/批量删除）
    :param req:
    :return:
    """
    id_list = req.POST.copy()['checkData']
    logger.debug("删除数据的ID："+str(id_list))
    sql = 'DELETE FROM good WHERE id IN (%s)' % (id_list)
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


# 服务增删改查
def list_server(req):
    """
    服务查询
    :param req:
    :return:
    """
    data = req.GET.copy()
    sql = 'select a.*,b.name as type from server a INNER JOIN server_category b ON a.server_category_id = b.id order by id'
    if 'servername' in data:
        server_name = data['servername']
        server_type = data['type']
        if server_name != '' and server_type == '':
            sql = "select a.*,b.`name` as type from(select * from server where `name`='%s')a INNER JOIN server_category b ON a.server_category_id = b.id ORDER BY id "%(server_name)
        elif server_name == '' and server_type != '':
            sql = "select a.*,b.`name` as type from(select * from server )a INNER  JOIN (select * from server_category where `id`='%s')  b ON a.server_category_id = b.id ORDER BY id "%(server_type)
        elif server_name != '' and server_type != '':
            sql ="select a.*,b.`name` as type from(select * from server where `name`='%s' )a INNER  JOIN (select * from server_category where `id`='%s')  b ON a.server_category_id = b.id ORDER BY id"%(server_name,server_type)
        else:
            pass
    db = Mysql()

    query_result = db.getAll(sql)
    db.dispose()

    server_list = list(query_result)

    limit = int(req.GET['limit'])
    page = int(req.GET['page'])
    resp = {
        "code": 0,
        "msg": "",
        "count": len(server_list),
        "data": server_list[(page - 1) * limit:page * limit]
    }

    logger.debug('【服务接口数据】：' + json.dumps(resp))

    return HttpResponse(json.dumps(resp), content_type="application/json")


def add_server(req):
    """
    添加服务
    :param req:
    :return:
    """
    logger.debug('添加服务传入参数：' + str(req.POST))
    data = req.POST.copy()

    db = Mysql()
    is_exist = db.getAll('SELECT * from server where `name` =\'%s\'' % (data['name']))

    if (is_exist):
        # 已存在该服务无法添加
        resp = {
            "code": 2,
            "msg": "server_is_exist"
        }
        logger.debug('添加失败,服务已存在')
    else:
        sql = "INSERT INTO `server` ( `name`, `server_category_id`, `price`) VALUES ('%s', '%s', '%s');"%(data['name'],data['type'],data['price'])
        logger.debug(sql)
        dd = db.insertOne(sql)
        db.dispose()
        if dd != 0:
            # 会员添加成功
            resp = {
                "code": 0,
                "msg": "success"
            }
            logger.debug('商品添加成功')
        else:
            # 会员添加失败
            resp = {
                "code": 1,
                "msg": "internal_exceptions"
            }
            logger.debug('服务异常,商品添加失败')
    return HttpResponse(json.dumps(resp), content_type="application/json")


def edit_server(req):
    """
    编辑服务
    :param req:
    :return:
    """
    logger.debug('更新服务传入参数：' + str(req.POST))
    data = req.POST.copy()
    logger.debug(data)

    sql2 = "SELECT * from server where `name` ='%s' and id != '%s'" % (data['name'], data['id'])
    logger.debug(sql2)

    db = Mysql()
    is_exist = db.getAll(sql2)

    if(is_exist):
        # 无法更新为已存在商品
        resp = {
            "code": 2,
            "msg": "phone_is_exist"
        }
        logger.debug('更新失败,商品已存在')
    else:
        count = str(int(data['count'])+int(data['add_count']))
        sql = "UPDATE good SET  `name` = '%s',good_category_id= '%s',price='%s',status='%s',uploadtime = now() WHERE id=%s" % (
        data['title'], data['type'], data['price'], count, data['id'])
        logger.debug(sql)
        dd = db.update(sql)
        db.dispose()
        if dd != 0:
            # 会员更新成功
            resp = {
                "code": 0,
                "msg": "success"
            }
            logger.debug('商品更新成功')
        else:
            # 会员更新失败
            resp = {
                "code": 1,
                "msg": "internal_exceptions"
            }
            logger.debug('服务异常,商品更新失败')

    return HttpResponse(json.dumps(resp), content_type="application/json")


def del_server(req):
    """
    服务删除（单个/批量删除）
    :param req:
    :return:
    """
    id_list = req.POST.copy()['checkData']
    logger.debug("删除数据的ID："+str(id_list))
    sql = 'DELETE FROM server WHERE id IN (%s)' % (id_list)
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
