import connexion,time
from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.models.inline_response2004 import InlineResponse2004
from swagger_server.models.inline_response2005 import InlineResponse2005
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from swagger_server.tool import getTment, getAtttStatus, transpositionTime,getID
from swagger_server.db import FMonth, FDay, FSysEmployee,FSysTment
from swagger_server.tool import timeTransposition,fortmentgetman,getid,getname,transpositionTime

def attendance_day_export_get(team=None, keyword=None, starttime=None, username=None):  # noqa: E501
    """attendance export

    attendance export # noqa: E501

    :param team: team
    :type team: str
    :param keyword: keyword
    :type keyword: str
    :param starttime: start time
    :type starttime: str
    :param username: the username choosed
    :type username: str

    :rtype: InlineResponse2004
    """
    return 'do some magic!'


def attendance_day_get(team=None, keyword=None, username=None, starttime=None):  # noqa: E501
    """attendance day list

    attendance day list # noqa: E501

    :param team: team
    :type team: str
    :param keyword: keyword
    :type keyword: str
    :param username: the username for user choose
    :type username: str
    :param starttime: start time
    :type starttime: str

    :rtype: InlineResponse2004
    """
    try:
        result = []
        if starttime == '':
            starttime = transpositionTime(int(time.time()) - 3600)
            starttime = str(starttime[0:4]) + str(starttime[5:7]) + str(starttime[8:10])

        data = FDay.select()
        if starttime != '':
            starttime = str(starttime[0:4]) + str(starttime[5:7]) + str(starttime[8:10])
            print(starttime)
            data = data.where(FDay.times == int(starttime))
        if username != '':
            id = getid(username)
            data = data.where(FDay.uid == id[0])
        for item in data:
            username = getname(item.uid)[0]
            result.append({
                'id': item.uid,
                "username": username,
                "tment": getTment(FSysEmployee.get(FSysEmployee.id == item.uid).tment),
                "passtime": transpositionTime(item.posttime),
                "status": getAtttStatus(item.type)
            })

        if team != '':
            result = [x for x in result if x['tment'] == '{}'.format(team)]
        msg = {"code": 0, "msg": 'success', 'result': result}
    except:
        msg = {"code": -1, "msg": 'error'}
    return msg


def attendance_day_info_get(id):  # noqa: E501
    """attendance export

    attendance export # noqa: E501

    :param id: login user id
    :type id: str

    :rtype: InlineResponse2004
    """
    result=[]
    data = FDay.select().where(FDay.uid==id).order_by(FDay.posttime.desc())
    username=getname(id)
    for item in data:
        msg_list={"username":username[0],
         "passtime":transpositionTime(item.posttime),
        'tment':'研发部',
         "status":getAtttStatus(item.type)}
        result.append(msg_list)
    msg={"code":0,"msg":"success","result":result}
    return msg


def attendance_export_get(team=None, keyword=None, starttime=None, endtime=None):
    """
    attendance export
    attendance export
    :param team: team
    :type team: str
    :param keyword: keyword
    :type keyword: str
    :param starttime: start time
    :type starttime: str
    :param endtime: end time
    :type endtime: str

    :rtype: InlineResponse2004
    """
    try:
        result = FMonth.select()
        if keyword != None and keyword != '':
            like = '%' + keyword + '%'
            result = result.where(FMonth.username % like)
        if team != None and team != '':
            print(team)
            result = result.where(FMonth.tid == team)
        if starttime != None and starttime != '':
            try:
                print(int(timeTransposition(starttime)) / 1000)
                result = result.where(FMonth.posttime > int(timeTransposition(starttime)) / 1000)
            except:
                pass
        if endtime != None and endtime != '':
            try:
                result = result.where(FMonth.posttime < int(timeTransposition(endtime)) / 1000)
            except:
                pass
        total = result.count()



        # if (keyword!=None) or (team!=None) or (starttime!=None) or (endtime!=None):
        #     like = '%' + keyword + '%'
        #     result = FMonth.select().where((FMonth.tid == team) | (FMonth.username % like) | (FMonth.posttime > starttime) | (FMonth.posttime < endtime)).paginate(int(page), int(size))
        #     total = FMonth.select().where(FMonth.tid == team).count()
        # else:
        #     result = FMonth.select().paginate(int(page), int(size))
        #     total = FMonth.select().count()
        msg = {"code": 0, "msg": "success", "total": total, "result": [{'id': item.id, 'name': item.username, 'tment': getTment(item.tid), 'normal': item.normal, 'off': item.off, 'late': item.late, 'quit': item.early, 'absence': item.absence} for item in result]}
    except:
        msg = {"code": -1, "msg": "system error"}
    return msg


def attendance_info_id_get(id):
    """
    attendance info
    attendance info
    :param id: login user id
    :type id: str

    :rtype: InlineResponse2005
    """
    data = FDay.select().where(FDay.uid==id)
    normal = data.where(FDay.type==0).count()
    late = data.where(FDay.type==1).count()
    early = data.where(FDay.type==3).count()
    off = data.where(FDay.type==2).count()
    absence = data.where(FDay.type==4).count()
    userinfo = FSysEmployee.get(FSysEmployee.id == id)
    userinfo = {
        'username': userinfo.username,
        'normal': normal,
        'late': late,
        'retreat': early,
        'absence': absence,
        'off': off
    }
    result=[{'day': str(item.times)[0:4]+'-'+str(item.times)[4:6]+'-'+str(item.times)[6:8]+' 00:00:00', 'status': (int(item.type))} for item in data]
    seen = set()
    new_dict_list = []
    for dict in result:
        t_dict = {'day': dict['day'], 'status': dict['status']}
        t_tup = tuple(t_dict.items())
        if t_tup not in seen:
            seen.add(t_tup)
            new_dict_list.append(dict)

    msg = {"code": 0, "msg": "success", "result": new_dict_list, "userinfo":userinfo}
    return msg


def attendance_list_get(size=None, page=None, team=None, keyword=None, starttime=None, endtime=None):
    """
    attendance list
    attendance list
    :param size: Each page shows the number
    :type size: str
    :param page: which page
    :type page: str
    :param team: team
    :type team: str
    :param keyword: keyword
    :type keyword: str
    :param starttime: start time
    :type starttime: str
    :param endtime: end time
    :type endtime: str

    :rtype: InlineResponse2004
    """
    # try:
    #
    # except:
    #     msg = {"code": -1, "msg": "system error"}
    result = FMonth.select()
    if keyword != None and keyword != '':
        like = '%' + keyword + '%'
        result = result.where(FMonth.username % like)
    if team != None and team != '':
        result = result.where(FMonth.tid == team)
    if starttime != None and starttime != '':
        try:
            print(int(timeTransposition(starttime)) / 1000)
            result = result.where(FMonth.posttime > int(timeTransposition(starttime)) / 1000)
        except:
            pass
    if endtime != None and endtime != '':
        try:
            result = result.where(FMonth.posttime < int(timeTransposition(endtime)) / 1000)
        except:
            pass

    #result = result.paginate(1, int(size))
    total = result.count()

    # if (keyword!=None) or (team!=None) or (starttime!=None) or (endtime!=None):
    #     like = '%' + keyword + '%'
    #     result = FMonth.select().where((FMonth.tid == team) | (FMonth.username % like) | (FMonth.posttime > starttime) | (FMonth.posttime < endtime)).paginate(int(page), int(size))
    #     total = FMonth.select().where(FMonth.tid == team).count()
    # else:
    #     result = FMonth.select().paginate(int(page), int(size))
    #     total = FMonth.select().count()
    msg = {"code": 0, "msg": "success", "total": total, "result": [
        {'id': item.id, 'name': item.username, 'tment': getTment(item.tid), 'normal': item.normal, 'off': item.off,
         'late': item.late, 'quit': item.early, 'absence': item.absence} for item in result]}
    return msg
