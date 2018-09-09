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
import time
import random
from functools import wraps

logger = logging.getLogger('django')
from JWT import JWT
jwt = JWT()

# 会员增删改查


@jwt.verify_bearer_token()
def list_vip_person(req):
    """
    会员列表查询
    :param req:
    :return:
    """

    data = req.GET.copy()
    sql = 'SELECT a.id, a.`name` AS vip_name, a.phone AS vip_phone, a.note AS vip_notes, a.sex AS vip_sex,' \
          ' sum(b.point) AS vip_person_point FROM person a LEFT JOIN point_detail b ON a.id = b.person_id and b.type =0 GROUP BY a.id ORDER BY a.id desc'

    if 'phone' in  data:
        phone = data['phone']
        sex = data['sex']
        if phone != '' and sex == '2':
            sql = "SELECT a.id, a.`name` AS vip_name, a.phone AS vip_phone, a.note AS vip_notes, a.sex AS vip_sex, sum(b.point) AS vip_person_point from (select * FROM person   WHERE `phone`='%s') a LEFT JOIN point_detail b ON a.id = b.person_id and b.type =0 GROUP BY a.id ORDER BY a.id desc" % (
            phone)
        elif phone == '' and sex != '2':
            sql = "SELECT a.id, a.`name` AS vip_name, a.phone AS vip_phone, a.note AS vip_notes, a.sex AS vip_sex, sum(b.point) AS vip_person_point from (select * FROM person   WHERE `sex` ='%s') a LEFT JOIN point_detail b ON a.id = b.person_id  and b.type =0 GROUP BY a.id ORDER BY a.id desc" % (
                sex)
        elif phone != '' and sex != '2':
            sql = "SELECT a.id, a.`name` AS vip_name, a.phone AS vip_phone, a.note AS vip_notes, a.sex AS vip_sex, sum(b.point) AS vip_person_point from (select * FROM person   WHERE `phone`='%s' AND `sex` ='%s') a LEFT JOIN point_detail b ON a.id = b.person_id and b.type =0 GROUP BY a.id ORDER BY a.id desc" % (
                phone,sex)
        else:
            pass

    db = Mysql()
    n_list = []
    query_result = db.getAll(sql)
    db.dispose()
    # print (len(query_result))
    if len(query_result)!=0:
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
    response = HttpResponse(json.dumps(resp), content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

@jwt.verify_bearer_token()
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


@jwt.verify_bearer_token()
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
    exist = db.getAll("select * from vip_order where person_id in (%s) and order_status = 0"%(id_list))
    if not exist:
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
    else:
        resp = {
            "code": 2,
            "msg": "person exist order"
        }

    return HttpResponse(json.dumps(resp), content_type="application/json")


@jwt.verify_bearer_token()
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
@jwt.verify_bearer_token()
def list_good(req):
    """
    商品查询
    :param req:
    :return:
    """
    data = req.GET.copy()
    sql = 'select a.*,b.name as type from good a INNER JOIN good_category b ON a.good_category_id = b.id ORDER BY uploadtime desc'
    if 'title' in data or 'label' in data:
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
    query_result = db.getAll(sql)
    db.dispose()

    if len(query_result) != 0:
        good_list = list(query_result)

        for x in good_list:
           if x['uploadtime'] != '':
               x['uploadtime'] = str(x['uploadtime'])
           g_list.append(x)
        if 'limit' in req.GET:
            limit = int(req.GET['limit'])
            page = int(req.GET['page'])
            resp = {
                "code": 0,
                "msg": "",
                "count": len(g_list),
                "data": g_list[(page - 1) * limit:page * limit]
            }
            logger.debug(g_list[(page - 1) * limit:page * limit])
        else:
            resp = {
                "code": 0,
                "msg": "",
                "count": len(g_list),
                "data": g_list
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


@jwt.verify_bearer_token()
def add_good(req):
    """
    添加商品
    :param req:
    :return:
    """
    logger.debug('添加商品传入参数：' + str(req.POST))
    data = req.POST.copy()
    if float(data['origin_price'])> float(data['price']):
        resp = {
            "code": 3,
            "msg": "price_incorrect"
        }
        logger.debug('原价低于售价,请重新添加')
    else:
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
            sql = "INSERT INTO `good` (`name`, `good_category_id`, `price`, `uploadtime`, `status`,`origin_price`) VALUES ('%s', '%s', '%s', now(), '%s','%s');"%(data['title'],data['type'],data['price'],count,data['origin_price'])
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


@jwt.verify_bearer_token()
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

    if float(data['origin_price']) > float(data['price']):
        resp = {
            "code": 3,
            "msg": "price_incorrect"
        }
        logger.debug('原价低于售价,请重新更新')
    else:
        db = Mysql()
        is_exist = db.getAll(sql2)

        if(is_exist):
            # 无法更新为已存在商品
            resp = {
                "code": 2,
                "msg": "good_is_exist"
            }
            logger.debug('更新失败,商品已存在')
        else:
            count = str(int(data['count'])+int(data['add_count']))
            sql = "UPDATE good SET  `name` = '%s',good_category_id= '%s',price='%s',status='%s',uploadtime = now(),origin_price='%s' WHERE id=%s" % (
            data['title'], data['type'], data['price'], count, data['origin_price'],data['id'])
            logger.debug(sql)
            dd = db.update(sql)
            db.dispose()
            if dd != 0:
                # 商品更新成功
                resp = {
                    "code": 0,
                    "msg": "success"
                }
                logger.debug('商品更新成功')
            else:
                # 商品更新失败
                resp = {
                    "code": 1,
                    "msg": "internal_exceptions"
                }
                logger.debug('服务异常,商品更新失败')

    return HttpResponse(json.dumps(resp), content_type="application/json")


@jwt.verify_bearer_token()
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
@jwt.verify_bearer_token()
def list_server(req):
    """
    服务查询
    :param req:
    :return:
    """
    data = req.GET.copy()
    sql = 'select a.*,b.name as type from server a INNER JOIN server_category b ON a.server_category_id = b.id order by id'
    if 'servername' in data or 'type' in data:
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
    if 'limit' in req.GET:
        limit = int(req.GET['limit'])
        page = int(req.GET['page'])
        resp = {
            "code": 0,
            "msg": "",
            "count": len(server_list),
            "data": server_list[(page - 1) * limit:page * limit]
        }
    else:
        resp = {
            "code": 0,
            "msg": "",
            "count": len(server_list),
            "data": server_list
        }

    logger.debug('【服务接口数据】：' + json.dumps(resp))

    return HttpResponse(json.dumps(resp), content_type="application/json")


@jwt.verify_bearer_token()
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
            # 服务添加成功
            resp = {
                "code": 0,
                "msg": "success"
            }
            logger.debug('商品添加成功')
        else:
            # 服务添加失败
            resp = {
                "code": 1,
                "msg": "internal_exceptions"
            }
            logger.debug('服务异常,商品添加失败')
    return HttpResponse(json.dumps(resp), content_type="application/json")


@jwt.verify_bearer_token()
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
        # 无法更新为已存在服务
        resp = {
            "code": 2,
            "msg": "server_is_exist"
        }
        logger.debug('更新失败,商品已存在')
    else:
        result = db.getOne("SELECT * from server where id = '%s'" % data['id'])
        # print(result)
        if result['name']== data['name'] and float(result['price']) == float(data['price']) and int(result['server_category_id']) == int(data['type']) :
            # 服务未更改无需更新
            resp = {
                "code": 2,
                "msg": "nothing is changed"
            }
            logger.debug('服务异常,服务更新失败')
        else:
            sql = "UPDATE server SET  `name` = '%s',server_category_id= '%s',price='%s' WHERE id='%s'" % (data['name'], data['type'], data['price'],data['id'])
            logger.debug(sql)
            dd = db.update(sql)
            # print(dd)
            db.dispose()
            if dd != 0:
                # 服务更新成功
                resp = {
                    "code": 0,
                    "msg": "success"
                }
                logger.debug('服务更新成功')
            else:
                # 服务更新失败
                resp = {
                    "code": 1,
                    "msg": "internal_exceptions"
                }
                logger.debug('服务异常,服务更新失败')

    return HttpResponse(json.dumps(resp), content_type="application/json")


@jwt.verify_bearer_token()
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


# 订单系统处理
@jwt.verify_bearer_token()
def list_order(req):
    data = req.GET.copy()
    sql = "select c.order_serial_number,d.name,c.person_id,d.phone,c.type,c.order_status as state,all_value,c.lay_value,c.free_value,c.notes from( select a.*,b.name as type from vip_order a INNER JOIN order_category b ON a.order_category_id = b.id order by id) c INNER JOIN person d on c.person_id = d.id  ORDER BY c.order_serial_number desc"
    db = Mysql()


    n_list = []
    query_result = db.getAll(sql)
    db.dispose()
    if len(query_result) != 0:
        order_list = list(query_result)

        # print(len(person_list))
        # print req.GET
        limit = int(req.GET['limit'])
        page = int(req.GET['page'])

        for x in order_list:
            if x['state'] == 0:
                x['progress'] = '50%'
            elif x['state'] == 1 or x['state'] ==2:
                x['progress'] = '100%'
            else:
                x['progress'] = '0%'
            n_list.append(x)
            # print(len(n_list))
        # print(n_list[(page - 1) * limit:page * limit])
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
    logger.debug('【订单接口数据】：' + json.dumps(resp))

    return HttpResponse(json.dumps(resp), content_type="application/json")


@jwt.verify_bearer_token()
def add_order(req):
    """
    订单添加
    :param req:
    :return:
    """
    logger.debug('订单生成传入参数：' + str(req.POST))
    data = req.POST.copy()
    db = Mysql()
    resp = ''
    good_list = []
    server_list = []
    sql_list = []
    for x in data:
        if 'good' in x and data[x] != '0':
            if x[4:] != '':
                good_list.append(x[4:] + '-' + data[x])
            else:
                logger.debug("未选取任何商品")
        elif 'server' in x and data[x] != '0':
            if x[6:] != '':
                server_list.append(x[6:7])
            else:
                logger.info("未选取任何服务")
        else:
            pass
    logger.info('本次商品清单：'.join(good_list))
    logger.info('本次服务清单：'.join(server_list))
    if 'new_dd' not in data:
        num = 1
        is_exist = db.getAll("SELECT * from vip_order where `person_id` ='%s'  and order_status = 0  " % (data['id']))
        if (is_exist):
            # 该会员已存在订单无法继续添加
            resp = {
                "code": 2,
                "msg": "main_order_is_exist"
            }
            logger.debug('订单生成失败,该会员主订单已存在')
            db.dispose()
        else:
            serial_num = time.strftime("%Y%m%d%H%M%S", time.localtime())
            #  price = db.getAll("SELECT price FROM order_category WHERE id ='%s'"%data['type'])
            #if price:
            sql = "INSERT INTO vip_order(`person_id`,`order_serial_number`, `order_status`, `order_category_id`, `create_time`, `notes`,`lay_value`, `free_value`) VALUES ('%s','%s','0', '%s', now(), '%s' ,'0','0');" % (
            data['id'],serial_num,data['type'], data['vip_notes'])
            dd = db.insertOne(sql)
            # print (dd)
            if dd != 0:
                # print (good_list)
                #print (server_list)
                for good in good_list:
                    sql_list.append("INSERT INTO `order_good_item`( `order_id`, `good_id`, `good_count`) VALUES ( '%s', '%s', '%s');"%(dd,good.split('-')[0],good.split('-')[1]))
                    now_count = db.getAll("select status from good WHERE id = '%s'"%(good.split('-')[0]))
                    # print(now_count)
                    if now_count:
                        # print (int(now_count[0]['status']))
                        # print (int(good.split('-')[1]))
                        left_count = (int(now_count[0]['status'])-int(good.split('-')[1]))
                        # print("UPDATE good SET status = '%s' WHERE id = '%s'"%(str(left_count),good.split('-')[0]))
                        sql_list.append("UPDATE good SET status = '%s' WHERE id = '%s'"%(str(left_count),good.split('-')[0]))
                    else:
                        return
                for server in server_list:
                    sql_list.append("INSERT INTO `vms`.`order_server_item` ( `order_id`, `server_id`, `server_count`) VALUES ('%s', '%s', '1');"%(dd,server))



                # print (sql_list)
                # print (len(sql_list))
                dd2 = db.inserGoodServer(num,dd,sql_list)
                logger.info('插入影响行数：'+str(dd2))
                db.dispose()

                if dd2 == len(sql_list):
                    resp = {
                        "code": 0,
                        "msg": "success"
                    }
                    logger.debug('订单生成成功')
                else:
                    resp = {
                        "code": 1,
                        "msg": "internal_exceptions"
                    }
                    logger.debug('订单生成失败')

    else:
        num = 2
        # 查询出主订单的id
        dd = db.getOne("SELECT id,free_value,lay_value FROM vip_order WHERE person_id ='%s' and order_status = 0"%data['id'])

        if dd:

            # 新增商品的sql语句插入sql_list以及商品消费
            for good in good_list:
                sql_list.append("INSERT INTO `order_good_item`( `order_id`, `good_id`, `good_count`) VALUES ( '%s', '%s', '%s');" % (
                    dd['id'], good.split('-')[0], good.split('-')[1]))
                now_count = db.getAll("select status from good WHERE id = '%s'" % (good.split('-')[0]))
                #  print(now_count)
                if now_count:
                    left_count = (int(now_count[0]['status']) - int(good.split('-')[1]))
                    # print("UPDATE good SET status = '%s' WHERE id = '%s'"%(str(left_count),good.split('-')[0]))
                    sql_list.append(
                        "UPDATE good SET status = '%s' WHERE id = '%s'" % (str(left_count), good.split('-')[0]))
                else:
                    return

            # 新增服务的sql语句插入sql_list
            for server in server_list:
                sql_list.append("INSERT INTO `vms`.`order_server_item` ( `order_id`, `server_id`, `server_count`) VALUES ('%s', '%s', '1');" % (
                    dd['id'], server))

            # # 延时费用和优惠费用的sql语句插入sql_list
            # if data['free_value'] == '' and data['lay_value'] == '':
            #     pass
            # else:
            #     if data['free_value'] == '':
            #         data['free_value'] = 0
            #     if data['lay_value'] == '':
            #         data['lay_value'] = 0
            #     free = float(dd['free_value']) + float(data['free_value'])
            #     lay = float(dd['lay_value']) + float(data['lay_value'])
            #     sql_list.append("UPDATE vip_order SET free_value ='%s' ,lay_value ='%s' WHERE id ='%s'"%(free,lay,dd['id']))

            # print(sql_list)
            # print(len(sql_list))
            # 执行新增消费的记录插入，包括延时费用和优惠费用的更新
            if len(sql_list) != 0:
                dd2 = db.inserGoodServer(num,dd,sql_list)
                logger.info('插入影响行数：' + str(dd2))
                if dd2 == len(sql_list):
                    resp = {
                        "code": 0,
                        "msg": "success"
                    }
                    logger.debug('新增消费成功')
                else:
                    resp = {
                        "code": 1,
                        "msg": "internal_exceptions"
                    }
                    logger.debug('新增消费失败')
            else:
                resp = {
                    "code": 3,
                    "msg": "nothing_is_changed"
                }
                logger.debug('新增消费失败')
            db.dispose()

    return HttpResponse(json.dumps(resp), content_type="application/json")


@jwt.verify_bearer_token()
def order_detail(req):
    logger.debug('订单详情传入参数：' + str(req.GET))
    data = req.GET.copy()
    resp = ''
    db = Mysql()
    result = db.getOne("SELECT c.*,d.name as type,d.price FROM ((SELECT a.*,b.name,b.phone FROM( SELECT * FROM vip_order WHERE `order_serial_number` = '%s') a INNER JOIN person b ON a.person_id = b.id)) c INNER JOIN order_category d ON c.order_category_id = d.id " % (data['order_serial_number']))
    logger.debug(result)
    if result:
        valid_point = db.getOne("select sum(point) as valid_point from point_detail where person_id = '%s'"%result['person_id'])['valid_point']
        if not valid_point:
            valid_point = 0
        logger.debug(valid_point)
        good_value_list = db.getAll(
            "select SUM(a.good_count) as good_count,b.name,b.price from (select good_id,good_count from order_good_item WHERE order_id = '%s'  ) a INNER JOIN good b on a.good_id = b.id GROUP BY a.good_id" %
            result['id'])
        server_value_list = db.getAll(
            "select SUM(server_count) as server_count,b.name,b.price from (select server_id,server_count from order_server_item where order_id = '%s' ) a INNER JOIN server b on a.server_id = b.id GROUP BY a.server_id" %
            result['id'])
        # print(good_value_list)
        good_value = 0
        server_value = 0

        for x in good_value_list:
            good_value = good_value + (x['price'] * int(x['good_count']))
            x['good_count'] = str(x['good_count'])

        logger.debug('商品消费为：' + str(good_value) + '元')

        for y in server_value_list:
            # print(y)
            server_value = server_value +(y['price'] * int(y['server_count']) )
            y['server_count'] = str(y['server_count'])
        logger.debug('服务消费为：' + str(server_value) + '元')

        # 目前除去优惠和延时费用的总消费价格
        now_value = good_value+server_value
        resp = {
            "code": 0
            , "msg": ""
            , "name": result['name']
            , "valid_point":valid_point
            , "site_money": float(result['price'])
            , "money":str(now_value)
            , "lay_value": result['lay_value']
            , "free_value": result['free_value']
            , "order_serial_number":result['order_serial_number']
            , "type":result['type']
            , "state": result['order_status']
            , "start_time": str(result['create_time'])
            , "end_time": str(result['end_time'])
            , "server":list(server_value_list)
            , "good": list(good_value_list)

        }
        db.dispose()
    return HttpResponse(json.dumps(resp), content_type="application/json")


@jwt.verify_bearer_token()
def end_order(req):
    logger.debug('结账传入参数：' + str(req.POST))
    data = req.POST.copy()
    resp = ''
    db = Mysql()
    result = db.getOne(
        "SELECT c.*,d.name as type,d.price FROM ((SELECT a.*,b.name,b.phone FROM( SELECT * FROM vip_order WHERE `order_serial_number` = '%s' ) a INNER JOIN person b ON a.person_id = b.id)) c INNER JOIN order_category d ON c.order_category_id = d.id " % (
        data['orderid']))
    point = db.getOne("select SUM(point) as valid_point from point_detail where person_id ='%s'"%result['person_id'])
    # print(point)
    logger.debug(result)
    if result:
        if data['free_value'] == '':
            data['free_value'] = 0
        if data['lay_value'] == '':
            data['lay_value'] = 0
        all_money = float(data['site_money'])+ float(data['money'])+float(data['lay_value'])-float(data['free_value'])
        sql_list = []
        offset_point = 0

        if data['type'] == '1':

            if point['valid_point']:
                sql2 = "INSERT INTO `vms`.`point_detail`( `person_id`, `order_id`, `type`, `point`, `create_time`) VALUES ('%s', '%s', 1,'%s', now());"%(result['person_id'],result['id'],str(0-int(float(point['valid_point']))/10*10))
                sql_list.append(sql2)
                offset_point = int(float(point['valid_point'])) / 10
            else:
                point = 0


        elif data['type'] == '2':
            pass
        elif data['type'] == '3' :
            if float(data['my_point']) <= float(point['valid_point']):
                offset_point = int(float(data['my_point']))/10
                sql2 = "INSERT INTO `vms`.`point_detail`( `person_id`, `order_id`, `type`, `point`, `create_time`) VALUES ('%s', '%s', 1,'%s', now());" % (
                result['person_id'], result['id'], str(0 - int(float(data['my_point']))/10*10))
                sql_list.append(sql2)
            else:
                resp = {
                    "code": 2,
                    "msg": "failed"
                }
                logger.debug('输入积分值大于可用积分值')
                return HttpResponse(json.dumps(resp), content_type="application/json")
        else:
            resp = {
                "code": 1,
                "msg": "failed"
            }
            logger.debug('结算失败')
            return HttpResponse(json.dumps(resp), content_type="application/json")
        sql = "UPDATE vip_order SET all_value = '%s',lay_value ='%s',free_value='%s', point_offset='%s',order_status=1,end_time=now() where order_serial_number = '%s'" % (
            all_money - offset_point, data['lay_value'], data['free_value'], offset_point, data['orderid'])
        sql3 = "INSERT INTO `vms`.`point_detail`( `person_id`, `order_id`, `type`, `point`, `create_time`) VALUES ('%s', '%s', 0,'%s', now());" % (
            result['person_id'], result['id'], all_money - offset_point)
        sql_list.append(sql)
        sql_list.append(sql3)
        # print(sql_list)
        count = db.excuteManysql(sql_list)
        # print(sql)
        # count = db.update(sql)
        # print(count)
        if count == len(sql_list):
            resp = {
                "code": 0,
                "msg": "success"
            }
            logger.debug('结算成功')
        else:
            resp = {
                "code": 1,
                "msg": "failed"
            }
            logger.debug('结算失败')
        db.dispose()
    else:
        resp = {
            "code": 1,
            "msg": "failed"
        }
        logger.debug('结算失败')
    return HttpResponse(json.dumps(resp), content_type="application/json")


@jwt.verify_bearer_token()
def del_order(req):
    """
    废弃订单，将订单状态修改为2，此单消费货物返还。
    :param req:
    :return:
    """
    logger.debug('订单废弃传入参数：' + str(req.GET))
    data = req.GET.copy()
    sql_list = []
    sql = "UPDATE vip_order SET order_status = 2,all_value = '0',end_time=now() WHERE order_serial_number = '%s'"%data['order_serial_number']
    sql2 = "select a.good_id,a.good_count from order_good_item a  INNER JOIN vip_order b ON a.order_id = b.id and b. order_serial_number = '%s'" %data['order_serial_number']
    db = Mysql()
    result = db.getAll(sql2)
    # print(result)
    if result:
        for x in result:
            good_id = x['good_id']
            good_count = int(x['good_count'])
            sql_list.append("UPDATE good SET status = status+'%d' WHERE id = '%s'"%(good_count,good_id))
        sql_list.append(sql)
        count = db.excuteManysql(sql_list)
        # print(count)
        if count == 1+len(result):
            resp = {
                "code": 0,
                "msg": "success"
            }
            logger.debug('订单废弃成功')
        else:
            resp = {
                "code": 1,
                "msg": "internal_exceptions"
            }
    else:
        count = db.update(sql)
        if count == 1:
            resp = {
                "code": 0,
                "msg": "success"
            }
            logger.debug('订单废弃成功')
        else:
            resp = {
                "code": 1,
                "msg": "internal_exceptions"
            }
    db.dispose()
    return HttpResponse(json.dumps(resp), content_type="application/json")


def manager_login(req):
    """
    管理者账号登录
    :param req:
    :return:
    """
    resp = ''
    username = req.POST.get('username')
    password = req.POST.get('password')
    sql = "SELECT * from manager where username ='%s' and password='%s'"%(username,password)
    db = Mysql()
    result = db.getOne(sql)
    if result:
        access_token = jwt.create_token(username)

        in_result = db.insertOne(
            "INSERT INTO `vms`.`t_token`(`user_id`,`token`, `time`) VALUES ('%s','%s', now());" %(result['id'],access_token) )

        if in_result:
            # print(access_token)
            resp = {
                "code": 0
                , "msg": "登入成功"
                , "data": {
                    "access_token": access_token
                }
            }
            return HttpResponse(json.dumps(resp), content_type="application/json")
    resp = {
        "code": 1
        , "msg": "登入失败"
        , "data": {
        }
    }

    return HttpResponse(json.dumps(resp), content_type="application/json")


def manager_logout(req):
    """
    管理者账号退出登录
    :param req:
    :return:
    """
    token = req.GET.get('access_token')
    db = Mysql()
    result = db.getAll("select * from t_token where token = '%s'"%token)
    if result:
        if db.delete("DELETE FROM t_token where token = '%s'"%token):
            resp = {
                "code": 0
                , "msg": "退出成功"
                , "data": {
                }
            }
        else:
            resp = {
                "code": 1
                , "msg": "数据库异常，退出失败"
                , "data": {
                }
            }
    else:
        resp = {
            "code": 1
            , "msg": "退出失败"
            , "data": {
            }
        }
    return HttpResponse(json.dumps(resp), content_type="application/json")


@jwt.verify_bearer_token()
def get_now_login_name(req):
    resp ={
      "code": 0
      ,"msg": ""
      ,"data": {
        "username": "张运通"
        ,"sex": "男"
        ,"role": 1
      }
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")

@jwt.verify_bearer_token()
def change_assword(req):
    resp = ''
    token = req.POST.get('access_token')
    db =Mysql()
    result = db.getOne("select * from t_token  a INNER JOIN manager b  ON a.user_id = b.id  and b.`password` ='%s' and a.token = '%s'"%(req.POST.get('oldPassword'),token))

    if result:
        sql2 = "UPDATE manager SET `password` ='%s' WHERE id = '%s'"%(req.POST.get('password'),result['user_id'])
        if db.update(sql2):
            resp ={
              "code": 0
              ,"msg": "success"
              ,"data": {

              }
            }
        else:
            resp = {
                "code": 1
                , "msg": "failed"
                , "data": {

                }
            }
    else:
        resp = {
            "code": 2
            , "msg": "failed"
            , "data": {

            }
        }
    return HttpResponse(json.dumps(resp), content_type="application/json")