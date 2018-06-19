import connexion, time
from swagger_server.models.body import Body
from swagger_server.models.inline_response200 import InlineResponse200
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from swagger_server.db import FSysUser
from swagger_server.tool import *

def login_post(body):
    """
    User Login
    System User Login
    :param b\]'\]\]\ody: data
    :type body: dict
    | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        print('-----------------')
        body = Body.from_dict(connexion.request.get_json())
        try:
            print(body.username, body.passwd)
            data = FSysUser.get((FSysUser.mail == body.username) & (FSysUser.status==1))
            try:
                encrypStr = body.username + body.passwd
                print(encrypStr)
                passwd = encryption(encrypStr)
                print(passwd, data.passwd)
                if data.passwd == passwd:
                    msg = {"code": 0, "msg": "success"}
                else:
                    msg = {"code": 10002, "msg": "wrong password"}
            except:
                msg = {"code": 10001, "msg": "User does not exist"}
        except:
            msg = {"code": 10003, "msg": "没有启用该用户"}

    return msg
