import connexion,xlwt,time
from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.models.inline_response2006 import InlineResponse2006
from swagger_server.models.inline_response2007 import InlineResponse2007
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from swagger_server.db import FVisitorsLog
from swagger_server.tool import getTment,transpositionTime,getpeopleStatus,getpurpose
from swagger_server.tool import timeTransposition



def visitors_export_get(team=None, keyword=None, starttime=None, endtime=None):
    """
    Visitors Export
    Visitors Export
    :param team: team
    :type team: str
    :param keyword: keyword
    :type keyword: str
    :param starttime: start time
    :type starttime: str
    :param endtime: end time
    :type endtime: str

    :rtype: InlineResponse2006
    """
    try:

        result = FVisitorsLog.select()
        if keyword != None and keyword != '':
            like = '%' + keyword + '%'
            try:
                result = result.where(FVisitorsLog.username % like | FVisitorsLog.interviewed % like)
            except:
                pass

        if team != None and team != '':
            result = result.where(FVisitorsLog.team == team)
        if starttime != None and starttime != '':
            try:
                print(int(timeTransposition(starttime)) / 1000)
                result = result.where(FVisitorsLog.starttime > int(timeTransposition(starttime)) / 1000)
            except:
                pass
        if endtime != None and endtime != '':
            try:
                result = result.where(FVisitorsLog.starttime < int(timeTransposition(endtime)) / 1000)
            except:
                pass
        total = result.count()
        workbook_m = xlwt.Workbook(encoding='utf-8')
        xlsheet = workbook_m.add_sheet('访客导出日志', cell_overwrite_ok=True)
        #xlsheet.write(0, 0, 'id')
        xlsheet.write(0, 0, '姓名')
        xlsheet.write(0, 1, '被访人')
        xlsheet.write(0, 2, '被访人部门')
        xlsheet.write(0, 3, '访客人数')
        xlsheet.write(0, 4, '访客状态')
        xlsheet.write(0, 5, '来访时间')
        xlsheet.write(0, 6, '离开时间')
        i = 1
        for item in result:
            #xlsheet.write(i, 0, item.id)
            xlsheet.write(i, 0, item.username)
            xlsheet.write(i, 1, item.interviewed)
            xlsheet.write(i, 2, getTment(int(item.team)))
            xlsheet.write(i, 3, item.total)
            xlsheet.write(i, 4, getpeopleStatus(int(item.status)))
            xlsheet.write(i, 5, transpositionTime(item.starttime))
            xlsheet.write(i, 6, transpositionTime(item.end))
            i = i + 1

        timemsg = '访客导出日志' + str(int(time.time()))
        workbook_m.save('/home/face/faceRec1/pic_data/{}.xls'.format(timemsg))
        # os.chmod('/home/face/faceRec1/pic_data/{}.xls'.format(timemsg),stat.S_IRWXO)
        msg = {"code": 0, "msg": '{}.xls'.format(timemsg), "total": total, "result": [{'id': item.id, 'name': item.username, 'interviewed': item.interviewed, 'team': getTment(int(item.team)), 'total': item.total, 'visiting': transpositionTime(item.end), 'status': getpeopleStatus(int(item.status))} for item in result]}
    except:
        msg = {"code": -1, "msg": "system error"}
    return msg


def visitors_info_id_get(id):
    """
    Visitors info
    Visitors info
    :param id: Each page shows the number
    :type id: str

    :rtype: InlineResponse2007
    """
    try:
        data = FVisitorsLog.get(FVisitorsLog.id==id)
        basic = {
            "username": data.username,
            "visiting": transpositionTime(data.starttime),
            "leave": transpositionTime(data.end),
            "purpose": getpurpose(int(data.purpose)),
            "phone": data.phone,
            "interviewed": data.interviewed,
            "team": getTment(int(data.team)),
            "total": data.total
        }
        pic_list=data.pic
        pic =[]
        for i in pic_list.split(','):
            try:
               pic.append({"url":i.split('/')[-1]})
            except:
                pass
        msg = {"code": 0, "msg": "success", "basic": basic, "topic": pic}
    except:
        msg = {"code": -1, "msg": "system error"}
    return msg


def visitors_list_get(size=None, page=None, team=None, keyword=None, starttime=None, endtime=None):
    """
    Visitors list
    Visitors list
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

    :rtype: InlineResponse2006
    """
    result = FVisitorsLog.select()
    if keyword != None and keyword != '':
        like = '%' + keyword + '%'
        try:
            result = result.where(FVisitorsLog.username % like | FVisitorsLog.interviewed % like)
        except:
            pass
    if team != None and team != '':
        result = result.where(FVisitorsLog.team == team)
    if starttime != None and starttime != '':
        try:
            print(int(timeTransposition(starttime)) / 1000)
            result = result.where(FVisitorsLog.starttime > int(timeTransposition(starttime)) / 1000)
        except:
            pass
    if endtime != None and endtime != '':
        result = result.where(FVisitorsLog.starttime < int(timeTransposition(endtime)) / 1000)
    result = result.order_by(FVisitorsLog.id.desc())
    result = result.paginate(int(page), 20)
    total = result.count()

    # if keyword != None or team != None or starttime != None or endtime != None:
    #     result = FVisitorsLog.select().where((FVisitorsLog.username ** '%'+ keyword +'%') | (FVisitorsLog.team == team) | ((FVisitorsLog.starttime > starttime) & (FVisitorsLog.starttime > endtime))).paginate(int(page), int(size))
    #     total = FVisitorsLog.select().where((FVisitorsLog.username ** '%'+ keyword +'%') | (FVisitorsLog.team == team) | ((FVisitorsLog.starttime > starttime) & (FVisitorsLog.starttime > endtime))).count()
    # else:
    #     result = FVisitorsLog.select().paginate(int(page), int(size))
    #     total = FVisitorsLog.select().count()

    result = [{'id': item.id, 'name': item.username, 'interviewed': item.interviewed, 'team': getTment(item.team),
               'total': item.total, 'visiting': transpositionTime(item.starttime), 'leave': transpositionTime(item.end),
               'status': getpeopleStatus(item.status)} for item in result]

    msg = {"code": 0, "msg": "success", "total": total, "result": result}
    #try:

    # except:
    #     msg = {"code": -1, "msg": "system error"}
    return msg
