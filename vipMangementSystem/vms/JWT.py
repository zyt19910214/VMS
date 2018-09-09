# -*- coding: utf-8 -*-

"""
@version: python2.7
@author: 'zyt'
@software: PyCharm
@time: 2018/9/1 13:36
"""
# -*- coding: utf-8 -*-

import jwt
import time
from DB import Mysql
from functools import wraps
from django.http import HttpResponse
import json

class JWT(object):

    def __init__(self):
        pass

    def create_token(self,username):
        payload = {
            "iss": "mothanty.com",
            "iat": int(time.time()),
            #"exp": int(time.time()) + 10,
            "username": username,
            "scopes": ['open']
        }
        token = jwt.encode(payload, 'mothanty', algorithm='HS256')
        return token


    # def verify_bearer_token(self,token):
    #     payload = jwt.decode(token, 'mothanty',  algorithms=['HS256'])
    #     db = Mysql()
    #     result = db.getAll("select * from t_token where token = '%s' and DATE_SUB(now(), INTERVAL 1 HOUR)<time"%token)
    #     if payload :
    #         if result:
    #             db.update("UPDATE t_token c set time = now()  WHERE token ='%s'"%token)
    #             return True
    #     db.delete("DELETE FROM t_token WHERE token='%s'"%token)
    #     return False

    def verify_bearer_token(self):
        def _deco(func):
            @wraps(func)
            def __deco(request, *para, **kw):
                token = ''
                db = Mysql()
                if request.method == 'GET':
                    token = request.GET.get('access_token')
                elif request.method == 'POST':
                    token = request.POST.get('access_token')
                else:
                    print('尚未处理的请求类型')
                if token is not None:
                    try:
                        payload = jwt.decode(token, 'mothanty', algorithms=['HS256'])
                    except Exception as e:
                        db.delete("DELETE FROM t_token WHERE token='%s'" % token)
                        print(e)
                        resp = {
                            "code": 1001,
                            "msg": "",
                            "count": 0,
                            "data": []
                        }
                        return HttpResponse(json.dumps(resp), content_type="application/json")
                    result = db.getAll(
                        "select * from t_token where token = '%s' and DATE_SUB(now(), INTERVAL 1 HOUR)<time" % token)
                    if payload:
                        if result:
                            db.update("UPDATE t_token set time = now()  WHERE token ='%s'" % token)
                            print (func.__name__ + '方法token校验--成功')
                            return func(request, *para, **kw)

                print (func.__name__ + '方法token校验--失败')
                db.delete("DELETE FROM t_token WHERE token='%s'" % token)
                resp = {
                    "code": 1001,
                    "msg": "",
                    "count": 0,
                    "data": []
                }
                return HttpResponse(json.dumps(resp), content_type="application/json")

            return __deco

        return _deco