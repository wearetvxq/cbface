import connexion, time, json,xlwt
from swagger_server.models.body1 import Body1
from swagger_server.models.body10 import Body10
from swagger_server.models.body11 import Body11
from swagger_server.models.body12 import Body12
from swagger_server.models.body13 import Body13
from swagger_server.models.body14 import Body14
from swagger_server.models.body2 import Body2
from swagger_server.models.body3 import Body3
from swagger_server.models.body4 import Body4
from swagger_server.models.body5 import Body5
from swagger_server.models.body6 import Body6
from swagger_server.models.body7 import Body7
from swagger_server.models.body8 import Body8
from swagger_server.models.body9 import Body9
from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.models.inline_response20010 import InlineResponse20010
from swagger_server.models.inline_response20011 import InlineResponse20011
from swagger_server.models.inline_response20012 import InlineResponse20012
from swagger_server.models.inline_response20013 import InlineResponse20013
from swagger_server.models.inline_response20014 import InlineResponse20014
from swagger_server.models.inline_response20015 import InlineResponse20015
from swagger_server.models.inline_response20016 import InlineResponse20016
from swagger_server.models.inline_response20017 import InlineResponse20017
from swagger_server.models.inline_response2008 import InlineResponse2008
from swagger_server.models.inline_response2009 import InlineResponse2009
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from swagger_server.db import FSysEmployee,FSysUser,FSysAttendance,FSysRouter,FSysTment
from swagger_server.tool import *
from flask import request
import os

def system_access_delete(body):
    """
    System Tment Del
    System Tment Del
    :param body: data
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Body12.from_dict(connexion.request.get_json())
        try:
            if FSysRouter.delete().where(FSysRouter.id == body.id).execute():
                msg = {"code": 0, "msg": "success"}
            else:
                msg = {"code": 10003, "msg": "Record does not exist"}
        except:
            msg = {"code": -1, "msg": "system error"}
    return msg


def system_access_get(size=None, page=None, keyword=None, status=None):
    """
    System tment get
    System tment get
    :param size: Each page shows the number
    :type size: str
    :param _from: which page
    :type _from: str
    :param keyword: keyword
    :type keyword: str
    :param status: access status
    :type status: str

    :rtype: InlineResponse20014
    """
    try:
        # if keyword!=None and status!=None:
        #     result = FSysRouter.select().where(FSysRouter.status == status) & (FSysRouter.name ** '%'+ keyword +'%').paginate(int(page), int(size))
        #     total = FSysRouter.select().where(FSysRouter.status == status) & (FSysRouter.name ** '%'+ keyword +'%').count()
        # else:
        #     result = FSysRouter.select().paginate(int(page), int(size))
        #     total = FSysRouter.select().count()
        result = FSysRouter.select()
        if keyword!=None and keyword!='':
            like='%'+keyword+'%'
            try:
               result=FSysRouter.select().where(FSysRouter.name % like)
            except:
                pass
        if status!=None and status!='':
            try:
               result=result.where(FSysRouter.status==status)
            except:
                pass
        result=result.paginate(int(page),20)
        total=result.count()
        msg = {"code": 0, "msg": "success", "total": total, "result": [{'id': item.id, 'name': item.name, 'level': item.level, 'type': item.type, 'status': item.status} for item in result]}
    except:
        msg = {"code": -1, "msg": "system error"}
    return msg


def system_access_post(body):
    """
    System Tment Add
    System Tment Add
    :param body: data
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Body11.from_dict(connexion.request.get_json())
        try:
            FSysRouter.insert(name=body.name,status=body.status,level=body.level,path=body.router,desc=body.desc,type=body.type,).execute()
            msg = {"code": 0, "msg": "success"}
        except:
            msg = {"code": -1, "msg": "system error"}
    return msg


def system_access_put(body):
    """
    System Tment Edit
    System Tment Edit
    :param body: data
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Body10.from_dict(connexion.request.get_json())
        try:
            FSysRouter.update(name=body.name,status=body.status,level=body.level,path=body.router,desc=body.desc,type=body.type).where(FSysRouter.id==body.id).execute()
            msg = {"code": 0, "msg": "success"}
        except:
            msg = {"code": -1, "msg": "system error"}
    return msg


def system_access_query_id_get(id):
    """
    System access get
    System access get
    :param id: user id
    :type id: str

    :rtype: InlineResponse20015
    """
    try:
        result = FSysRouter.get(FSysRouter.id==id)
        data = {
                "id": result.id,
                "name": result.name,
                "status": result.status,
                "level": result.level,
                "type": result.type,
                "router": result.path,
                "desc": result.desc
        }
        msg = {"code": 0, "msg": "success", "result": data}
    except:
        msg = {"code": -1, "msg": "system error"}
    return msg


def system_attendance_get():
    """
    System attendance set
    System attendance set

    :rtype: InlineResponse20016
    """
    try:
        result = FSysAttendance.select()
        morning = ''
        afternoon = ''
        for item in result:
            if item.type == 1:
                morning = json.loads(item.content)
            elif item.type == 2:
                afternoon = json.loads(item.content)
        msg = {"code": 0, "msg": "success", "morning": morning, "afternoon":afternoon}
    except:
        msg = {"code": -1, "msg": "system error"}
    return msg


def system_attendance_post(body):
    """
    System attendance set
    System attendance set
    :param body: data
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Body13.from_dict(connexion.request.get_json())
        try:
            if body.morning!=[]:
                morning = json.dumps({
                    'endwork': body.morning[0].endwork,
                    'endwork_late': body.morning[0].endwork_late,
                    'startwork': body.morning[0].startwork,
                    'startwork_late': body.morning[0].startwork_late
                })
                if FSysAttendance.select().where(FSysAttendance.type == 1).count():
                    FSysAttendance.update(content=morning).where(FSysAttendance.type == 1).execute()
                else:
                    FSysAttendance.insert(type=1, content=morning).execute()
            if body.afternoon!=[]:
                afternoon = json.dumps({
                    'endwork': body.afternoon[0].endwork,
                    'endwork_late': body.afternoon[0].endwork_late,
                    'startwork': body.afternoon[0].startwork,
                    'startwork_late': body.afternoon[0].startwork_late
                })
                if FSysAttendance.select().where(FSysAttendance.type == 2).count():
                    FSysAttendance.update(content=afternoon).where(FSysAttendance.type == 2).execute()
                else:
                    FSysAttendance.insert(type=2, content=afternoon).execute()

            msg = {"code": 0, "msg": "success"}
        except:
            msg = {"code": -1, "msg": "system error"}
    return msg


def system_employee_delete(body):
    """
    System employee Del
    System employee Del
    :param body: data
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Body6.from_dict(connexion.request.get_json())
        try:
            if FSysEmployee.delete().where(FSysEmployee.id==body.id).execute():
                msg = {"code": 0, "msg": "success"}
            else:
                msg = {"code": 10003, "msg": "Record does not exist"}
        except:
            msg = {"code": -1, "msg": "system error"}
    return msg


def system_employee_export_get(page=None,size=None,team=None, keyword=None, status=None):
    """
    System employee export
    System employee export
    :param team: team
    :type team: str
    :param keyword: keyword
    :type keyword: str
    :param status: account status
    :type status: str

    :rtype: InlineResponse20010
    """
    try:
        result=FSysEmployee.select()
        if team!=None and team!='':
            result=FSysEmployee.select().where(FSysEmployee.tment == team)
        if keyword!=None and keyword!='':
            like='%'+keyword+'%'
            result=result.where(FSysEmployee.username % like)
        if status!=None and status!='':
            result=result.where(FSysEmployee.status==status)
        result=result.order_by(FSysEmployee.posttime)
        #result = FSysEmployee.select().where((FSysEmployee.tment==team) | (FSysEmployee.status==status | (FSysEmployee.username ** '%'+ keyword +'%'))).order_by(FSysEmployee.posttime)
        total = result.count()
        workbook_m = xlwt.Workbook(encoding='utf-8')
        xlsheet = workbook_m.add_sheet('员工导出日志', cell_overwrite_ok=True)
        xlsheet.write(0, 0, '姓名')
        xlsheet.write(0, 1, '性别')
        xlsheet.write(0, 2, '部门')
        xlsheet.write(0, 3, '状态')
        xlsheet.write(0, 4, '创建时间')
        #xlsheet.write(0, 5, 'id')
        i = 1
        for item in result:
            xlsheet.write(i, 0, item.username)
            xlsheet.write(i, 1, getsex(item.sex))
            xlsheet.write(i, 2, getTment(item.tment))
            xlsheet.write(i, 3, getidstatus(item.status))
            xlsheet.write(i, 4, transpositionTime(item.posttime))
            #xlsheet.write(i, 5, item.id)


            i = i + 1

        timemsg = '员工导出日志' + str(int(time.time()))
        workbook_m.save('/home/face/faceRec1/pic_data/{}.xls'.format(timemsg))
        msg = {"code": 0, "msg": '{}.xls'.format(timemsg), "total": total, "result": [{'id': item.id, 'name': item.username, 'sex':getsex(item.sex), 'team': getTment(item.tment), 'status': getidstatus(item.status), 'posttime': transpositionTime(item.posttime)} for item in result]}
    except:
        msg = {"code": -1, "msg": "system error"}
    return msg


def system_employee_list_get(size=None, page=None, team=None, keyword=None, status=None):
    """
    System employee list
    System employee list
    :param size: Each page shows the number
    :type size: str
    :param _from: which page
    :type _from: str
    :param team: team
    :type team: str
    :param keyword: keyword
    :type keyword: str
    :param status: account status
    :type status: str

    :rtype: InlineResponse20010
    """
    result = FSysEmployee.select()
    if team != None and team != '':
        result = FSysEmployee.select().where(FSysEmployee.tment == team)
    if keyword != None and keyword != '':
        like = '%' + keyword + '%'
        result = result.where(FSysEmployee.username % like)
    if status != None and status != '':
        result = result.where(FSysEmployee.status == status)
    result = result.order_by(FSysEmployee.posttime)

    # result = FSysEmployee.select().where((FSysEmployee.tment==team) | (FSysEmployee.status==status | (FSysEmployee.username ** '%'+ keyword +'%'))).order_by(FSysEmployee.posttime).paginate(page, size)
    # total = FSysEmployee.select().where((FSysEmployee.tment==team) | (FSysEmployee.status==status | (FSysEmployee.username ** '%'+ keyword +'%'))).count()
    total = result.count()
    msg = {"code": 0, "msg": "success", "total": total, "result": [
        {'id': item.id, 'name': item.username, 'sex': getsex(item.sex), 'team': getTment(int(item.tment)),
         'status': getidstatus(item.status), 'posttime': transpositionTime(item.posttime)} for item in result]}


    # try:

    # except:
    #     msg = {"code": -1, "msg": "system error"}
    return msg


def system_employee_post(body):
    """
    System employee Add
    System employee Add
    :param body: data
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Body5.from_dict(connexion.request.get_json())
        try:
            FSysEmployee.insert(username=body.username, tment=getID((body.team)), sex=body.sex, status=body.status,pic=body.topic,desc=body.remarks, posttime=int(time.time())).execute()
            msg = {"code": 0, "msg": "success"}
        except:
            msg = {"code": -1, "msg": "system error"}
    return msg


def system_employee_put(body):
    """
    System employee Edit
    System employee Edit
    :param body: data
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Body4.from_dict(connexion.request.get_json())
        try:
            FSysEmployee.update(username=body.username, tment=getID(body.team), sex=body.sex, status=body.status, pic=body.topic, desc=body.remarks).where(FSysEmployee.id==body.id).execute()
            msg = {"code": 0, "msg": "success"}
        except:
            msg = {"code": -1, "msg": "system error"}
    return msg


def system_employee_query_id_get(id):
    """
    System employee get
    System employee get
    :param id: user id
    :type id: str

    :rtype: InlineResponse20011
    """
    data = FSysEmployee.get(FSysEmployee.id == id)
    picaddress=(data.pic).split('/')[-1]
    try:
       result = {
           "id": data.id,
           "topic": picaddress,
           "username": data.username,
           "team": getTment(int(data.tment)),
           "sex": getsex(data.sex),
           "status": getidstatus(data.status),
           "remarks": data.desc
       }
       msg = {"code": 0, "msg": "success", "result": result}
    except:
        msg = {"code": -1, "msg": "system error"}
    return msg


def system_password_post(body):
    """
    System User Edit Password
    System User Edit Password
    :param body: data
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Body14.from_dict(connexion.request.get_json())
        data = FSysUser.get(FSysUser.id == body.id)
        try:
            encrypStr = data.mail + body.old
            passwd = encryption(encrypStr)
            if data.passwd == passwd:
                new_encrypStr = data.mail + body.new
                new_passwd = encryption(new_encrypStr)
                FSysUser.update(passwd=new_passwd).where(FSysUser.id == body.id).execute()
                msg = {"code": 0, "msg": "success"}
            else:
                msg = {"code": 10002, "msg": "wrong password"}
        except:
            msg = {"code": -1, "msg": "system error"}
    return msg


def system_tment_delete(body):
    """
    System Tment Del
    System Tment Del
    :param body: data
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Body9.from_dict(connexion.request.get_json())
        try:
            if FSysTment.delete().where(FSysTment.id==body.id).execute():
                msg = {"code": 0, "msg": "success"}
            else:
                msg = {"code": 10003, "msg": "Record does not exist"}
        except:
            msg = {"code": -1, "msg": "system error"}
    return msg


def system_tment_export_get(keyword=None, status=None):
    """
    System tment export
    System tment export
    :param keyword: keyword
    :type keyword: str
    :param status: account status
    :type status: str

    :rtype: InlineResponse20012
    """
    try:
        result = FSysTment.select()
        if keyword!=None and keyword!='':
            try:
               like='%' +keyword+'%'
               result=result.where(FSysTment.name % like)
            except:
                pass
        if status!=None and status!='':
            try:
               result=result.where(FSysTment.status == status)
            except:
                pass

        total=result.count()

        workbook_m = xlwt.Workbook(encoding='utf-8')
        xlsheet = workbook_m.add_sheet('部门导出日志', cell_overwrite_ok=True)
        #xlsheet.write(0, , 'id')
        xlsheet.write(0, 0, '部门名称')
        xlsheet.write(0, 1, '人数')
        xlsheet.write(0, 2, '状态')
        xlsheet.write(0, 3, '创建时间')

        i = 1
        for item in result:
            #xlsheet.write(i, 0, item.id)
            xlsheet.write(i, 0, item.name)
            xlsheet.write(i, 1, item.total)
            xlsheet.write(i, 2, getidstatus(item.status))
            xlsheet.write(i, 3, transpositionTime(item.posttime))

            i = i + 1

        timemsg = '部门导出日志' + str(int(time.time()))
        workbook_m.save('/home/face/faceRec1/pic_data/{}.xls'.format(timemsg))

        # if keyword!=None and status!=None:
        #     result = FSysTment.select().where((FSysTment.status == status | (FSysTment.name ** '%'+ keyword +'%')))
        #     total = FSysTment.select().where((FSysTment.status == status | (FSysTment.name ** '%'+ keyword +'%'))).count()
        # else:
        #     result = FSysTment.select()
        #     total = FSysTment.select().count()
        msg = {"code": 0, "msg": '{}.xls'.format(timemsg), "total": total, "result": [{'id': item.id, 'name': item.name, 'total': item.total, 'posttime': transpositionTime(item.posttime), 'status': item.status} for item in result]}
    except:
        msg = {"code": -1, "msg": "system error"}
    return msg


def system_tment_list_get(size, page, keyword=None, status=None):
    """
    System tment list
    System tment list
    :param size: Each page shows the number
    :type size: str
    :param page: which page
    :type page: str
    :param keyword: keyword
    :type keyword: str
    :param status: account status
    :type status: str

    :rtype: InlineResponse20012
    """
    try:

        result = FSysTment.select()
        print(keyword,status)
        if keyword != None and keyword!='':
            try:
                like = '%' + keyword + '%'
                result = result.where(FSysTment.name % like)
            except:
                pass
        if status != None and status!='':
            try:
                result = result.where(FSysTment.status == status)
            except:
                pass
        result = result.paginate(int(page), 20)
        total = result.count()
        # if keyword!=None and status!=None:
        #     result = FSysTment.select().where((FSysTment.status == status | (FSysTment.name ** '%'+ keyword +'%'))).paginate(int(page), int(size))
        #     total = FSysTment.select().where((FSysTment.status == status | (FSysTment.name ** '%'+ keyword +'%'))).count()
        # else:
        #     result = FSysTment.select().paginate(int(page), int(size))
        #     total = FSysTment.select().count()
        msg = {"code": 0, "msg": "success", "total": total, "result": [{'id': item.id, 'name': item.name, 'total': item.total, 'posttime': transpositionTime(item.posttime), 'status': getidstatus(item.status)} for item in result]}
    except:
        msg = {"code": -1, "msg": "system error"}
    return msg


def system_tment_post(body):
    """
    System Tment Add
    System Tment Add
    :param body: data
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Body8.from_dict(connexion.request.get_json())
        try:
            tmenttotal=FSysTment.select().where(FSysTment.name==body.name).count()
            print(tmenttotal)
            if tmenttotal==0:
                try:
                    FSysTment.insert(name=body.name, status=body.status, desc=body.remarks, total=1,
                                     posttime=time.time()).execute()
                    msg = {"code": 0, "msg": "success"}
                except:
                    msg = {"code": -1, "msg": "system error"}
            else:
                msg = {"code": 10001, "msg": "部门已存在"}
        except:
            msg = {"code": -1, "msg": "system error"}
    return msg


def system_tment_put(body):
    """
    System Tment Put
    System Tment Put
    :param body: data
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Body7.from_dict(connexion.request.get_json())
        try:
            FSysTment.update(name=body.name,status=body.status,desc=body.remarks).where(FSysTment.id==body.id).execute()
            msg = {"code": 0, "msg": "success"}
        except:
            msg = {"code": -1, "msg": "system error"}
    return msg


def system_tment_query_id_get(id):
    """
    System tment get
    System tment get
    :param id: user id
    :type id: str

    :rtype: InlineResponse20013
    """
    try:
        data = FSysTment.get(FSysTment.id==id)
        result = {
            "id": data.id,
            "name": data.name,
            "status": getidstatus(data.status),
            "remarks": data.desc
        }
        msg = {"code": 0, "msg": "success", "result": result}
    except:
        msg = {"code": -1, "msg": "system error"}
    return msg


def system_user_delete(body):
    """
    System User Del
    System User Del
    :param body: data
    :type body: dict | bytes

    :rtype: InlineResponse200
    """

    if connexion.request.is_json:
        body = Body3.from_dict(connexion.request.get_json())
        print(body.id)
        print(type(body.id))
        try:
            if FSysUser.delete().where(FSysUser.id==body.id).execute():
                msg = {"code": 0, "msg": "success"}
            else:
                msg = {"code": 10003, "msg": "Record does not exist"}
        except:
            msg = {"code": -1, "msg": "system error"}
    return msg


def system_user_export_get(team=None, keyword=None, status=None):
    """
    System User export
    System User export
    :param team: team
    :type team: str
    :param keyword: keyword
    :type keyword: str
    :param status: account status
    :type status: str

    :rtype: InlineResponse2008
    """
    try:

        result = FSysUser.select()
        if keyword != None and keyword!='':
            try:
                like = '%' + keyword + '%'
                result = result.where(FSysUser.mail % like)
            except:
                pass
        if status != None and status!='':
            try:
                result = result.where(FSysUser.status == status)
            except:
                pass
        if team!=None and team!='':
            try:
                result=result.where(FSysUser.tment==getTment(team))
            except:
                pass
        workbook_m = xlwt.Workbook(encoding='utf-8')
        xlsheet = workbook_m.add_sheet('用户导出日志', cell_overwrite_ok=True)
        xlsheet.write(0, 0, 'id')
        xlsheet.write(0, 1, '姓名')
        xlsheet.write(0, 2, '帐号邮箱')
        xlsheet.write(0, 3, '状态')
        xlsheet.write(0, 4, '创建时间')
        xlsheet.write(0, 5, '所属部门')

        i = 1
        for item in result:
            xlsheet.write(i, 0, item.id)
            xlsheet.write(i, 1, item.username)
            xlsheet.write(i, 2, item.mail)
            xlsheet.write(i, 3, getidstatus(item.status))
            xlsheet.write(i, 4, transpositionTime(item.posttime))
            xlsheet.write(i, 5, getTment(item.tment))

            i = i + 1

        timemsg = '用户导出日志' + str(int(time.time()))
        workbook_m.save('/home/face/faceRec1/pic_data/{}.xls'.format(timemsg))
        total = result.count()
        # if keyword!=None and status!=None:
        #     result = FSysUser.select().where((FSysUser.status == status | (FSysUser.mail ** '%'+ keyword +'%')))
        #     total = FSysUser.select().where((FSysUser.status == status | (FSysUser.mail ** '%'+ keyword +'%'))).count()
        # else:
        #     result = FSysUser.select()
        #     total = FSysUser.select().count()
        msg = {"code": 0, "msg": '{}.xls'.format(timemsg), "total": total, "result": [{'id': item.id, 'mail': item.mail, 'username': item.username, 'posttime': transpositionTime(item.posttime), 'status': item.status} for item in result]}
    except:
        msg = {"code": -1, "msg": "system error"}
    return msg


def system_user_list_get(size=None, page=None, team=None, keyword=None, status=None):
    """
    System User list
    System User list
    :param size: Each page shows the number
    :type size: str
    :param page: which page
    :type page: str
    :param team: team
    :type team: str
    :param keyword: keyword
    :type keyword: str
    :param status: account status
    :type status: str

    :rtype: InlineResponse2008
    """
    try:
        print(team)
        result = FSysUser.select()
        if keyword != None and keyword != '':
            try:
                like = '%' + keyword + '%'
                result = result.where(FSysUser.mail % like)
            except:
                pass
        if status != None and status != '':
            try:
                result = result.where(FSysUser.status == status)
            except:
                pass
        if team!=None and team!='':
            try:
                result=result.where(FSysUser.tment==getID(team))
            except:
                pass

        total = result.count()
        # if keyword!=None and status!=None:
        #     result = FSysUser.select().where((FSysUser.status == status | (FSysUser.mail ** '%'+ keyword +'%'))).paginate(int(page), int(size))
        #     total = FSysUser.select().where((FSysUser.status == status | (FSysUser.mail ** '%'+ keyword +'%'))).count()
        # else:
        #     result = FSysUser.select().paginate(int(page), int(size))
        #     total = FSysUser.select().count()
        msg = {"code": 0, "msg": 'success', "total": total, "result": [{'id': item.id, 'mail': item.mail, 'username': item.username, 'posttime': transpositionTime(item.posttime), 'status': getidstatus(item.status)} for item in result]}
    except:
        msg = {"code": -1, "msg": "system error"}
    return msg

def system_user_post(body):
    """
    System User Add
    System User Add
    :param body: data
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Body2.from_dict(connexion.request.get_json())
        try:
            encrypStr = body.mail + body.passwd
            passwd = encryption(encrypStr)
            if FSysUser.select().where(FSysUser.mail==body.mail).count() >= 1:
                msg = {"code": 10001, "msg": "Account already exists"}
            else:
                FSysUser.insert(mail=body.mail,passwd=passwd,tment=body.team,username=body.username,status=body.status,posttime=time.time()).execute()
                msg = {"code": 0, "msg": "success"}
        except:
            msg = {"code": -1, "msg": "system error"}


    return msg

def system_user_put(body):
    """
    System User Edit
    System User Edit
    :param body: data
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Body1.from_dict(connexion.request.get_json())
        try:
            encrypStr = body.mail + body.passwd
            passwd = encryption(encrypStr)
            FSysUser.update(mail=body.mail,passwd=passwd,tment=body.team,username=body.username,status=body.status).where(FSysUser.id==body.id).execute()
            msg = {"code": 0, "msg": "success"}
        except:
            msg = {"code": -1, "msg": "system error"}
    return msg

def system_user_query_id_get(id):
    """
    System User get
    System User get
    :param id: user id
    :type id: str

    :rtype: InlineResponse2009
    """


    try:
        data = FSysUser.get(FSysUser.id == id)
        result = {
            "id": data.id,
            "team": getTment(int(data.tment)),
            "username": data.username,
            "mail": data.mail,
        }
        msg = {"code": 0, "msg": "success", "result": result}
    except:
        msg = {"code": -1, "msg": "system error"}
    return msg

def access_level_get(id=None):
    """
    Access Query Info
    Access Query Info
    :param id: access level
    :type id: str

    :rtype: InlineResponse20017
    """
    try:
        if id == None:
            result = FSysRouter.select().where(FSysRouter.level==0,FSysRouter.status==1)
        else:
            result = FSysRouter.select().where(FSysRouter.pid == id, FSysRouter.status == 1)
        msg = {"code": 0, "msg": "success", "result": [{'id': item.id, 'name': item.name, 'level': item.level} for item in result]}
    except:
        msg = {"code": -1, "msg": "system error"}
    return msg
def system_userpic_up(files):  
    """System userpic upfile

    System userpic up # noqa: E501

    :param files: the file of name
    :type files: werkzeug.datastructures.FileStorage

    :rtype: InlineResponse200
    """
    try:
        print('-------------')
        file = request.files['files']

        file.save(os.path.join('/home/face/faceRec1/pic_data', file.filename))
        new_filepath = file.filename
        msg = {'code': 0, 'msg': new_filepath}
    except:
        msg = {'code': -1, 'msg': 'Error'}
    return msg
