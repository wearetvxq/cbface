import connexion, json
from swagger_server.models.body17 import Body17
from swagger_server.models.body18 import Body18
from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.models.inline_response20020 import InlineResponse20020
from swagger_server.models.inline_response20021 import InlineResponse20021
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from swagger_server.db import FVisitorsLog, FLog
from swagger_server.tool import *
from swagger_server.IO import IO

def monitor_get(status):
    """
    Get access to people information
    Get access to people information
    :param status: Demand Processing Status
    :type status: str

    :rtype: InlineResponse20020
    """
    return 'do some magic!'


def monitor_open_post(body):
    """
    Open
    Open
    :param body: data
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Body18.from_dict(connexion.request.get_json())
        try:
            status = body.status
            a=IO()
            a.open(int(status))
            msg = {"code": 0, "msg": "success"}
        except:
            msg={"code": -1, "msg": "Error"}

    return msg


def monitor_post(body):
    """    Update visitor log
    Update visitor log
    :param body: data
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Body17.from_dict(connexion.request.get_json())
        #try:

        #except:
            #msg = {"code": -1, "msg": "system error"}
        # 取消
        if body.username == '':
            if body.visit_id== '1' or body.visit_id== '2' or body.visit_id== '3':
                FLog.update(status=2).where(FLog.id == int(body.id)).execute()
                FVisitorsLog.update(end=int(time.time())).where(FVisitorsLog.id == int(body.id)).execute()
            else:
                FLog.update(status=2).where(FLog.id == int(body.id)).execute()
            msg = {"code": 0, "msg": "success"}
        # 确定
        print(body.username)
        if body.username != '':
            if body.visit_id== 'a' or body.visit_id== 'b' or body.visit_id== 'c':
                print('hahahahah')
                FVisitorsLog.insert(visitid=body.visit_id, username=body.username, interviewed=body.interviewed,
                                    team=body.team, total=body.total, status=0,
                                    starttime=body.posttime.replace('000', ''), end=1, purpose=body.purpose,
                                    phone=body.phone, pic='/home/face/faceRec1/pic_data/' + body.pic[0].img).execute()
                FLog.update(status=1).where(FLog.id == int(body.id)).execute()
            else:
                FLog.update(status=1).where(FLog.id == int(body.id)).execute()
                FVisitorsLog.update(end=int(time.time())).where(
                    (FVisitorsLog.username == body.username) & (FVisitorsLog.end == 1)).execute()
            msg = {"code": 0, "msg": "success"}
    return msg

def monitor_polling_get():
    """
    polling log
    polling log

    :rtype: InlineResponse20021
    """
    import time
    try:
        try:
            data = FLog.select().where(FLog.status==0,FLog.type==2).order_by(FLog.posttime).get()
            camera = json.loads(data.content)
            print(camera['CamID'])
            pic_list = []
            if data.pic != 'null':
                for i in data.pic.split(','):
                    if i != '' and i.find('1.jpg') != -1:
                        pic_list.append({'img': i.split('/')[-1]})
                posttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data.posttime))
                msg_result = {'id': data.id, 'camid': str(camera['CamID']), 'pic': pic_list, 'posttime': posttime}
                msg = {"code": 0, "msg": "success", "result": msg_result}
        except:
            msg = {"code": 0, "msg": "success", "result": 0}
    except:
        msg = {"code": -1, "msg": "system error"}
    return msg
