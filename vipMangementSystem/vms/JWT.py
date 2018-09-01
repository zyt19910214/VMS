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

class JWT(object):

    def __init__(self):
        pass

    def create_token(self,username):
        payload = {
            "iss": "gusibi.com",
            "iat": int(time.time()),
            #"exp": int(time.time()) + 10,
            "username": username,
            "scopes": ['open']
        }
        token = jwt.encode(payload, 'mothanty', algorithm='HS256')
        return token

    def verify_bearer_token(self,token):
        payload = jwt.decode(token, 'mothanty',  algorithms=['HS256'])
        db = Mysql()
        result = db.getAll("select * from t_token where token = '%s' and DATE_SUB(now(), INTERVAL 1 HOUR)<time"%token)
        if payload :
            if result:
                db.update("UPDATE t_token c set time = now()  WHERE token ='%s'"%token)
                return True
        db.delete("DELETE FROM t_token WHERE token='%s'"%token)
        return False