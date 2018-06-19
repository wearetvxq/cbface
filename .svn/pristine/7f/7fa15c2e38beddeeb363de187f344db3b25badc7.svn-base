import connexion,json
from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.models.inline_response2001 import InlineResponse2001
from swagger_server.models.inline_response2002 import InlineResponse2002
from swagger_server.models.inline_response2003 import InlineResponse2003
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from swagger_server.db import *
from swagger_server.tool import *

def index_by_get():
    """
    Index Pie Chart
    Index Pie Chart

    :rtype: InlineResponse2002
    """
    try:
        result_list=[]
        result = FEmployeeLog.select().order_by(FEmployeeLog.posttime.desc()).paginate(1,3)
        for item in result:
            msg_list={
                "name": getname(item.uid)[0],
                "team": getTment(getname(item.uid)[1]),
                "desc": '内部员工',
                 "posttime": transpositionTime(item.posttime)}
            result_list.append(msg_list)

        result1 = FVisitorsLog.select().order_by(FVisitorsLog.starttime.desc()).paginate(1,3)
        for item in result1:
            msg_lis={
                "name": item.username,
                "team": "其他",
                "desc": "陌生人来访",
                "posttime": transpositionTime(item.starttime)
            }
            result_list.append(msg_lis)
        msg = {"code": 0, "status": "success", "result":result_list}

    except:
        msg={"code":-1,"status":"Error"} 
    return msg

def index_log_get():
    """
    Index Chart Log
    Index Chart Log

    :rtype: InlineResponse2003
    """
    viptotal=FVisitorsLog.select().where(FVisitorsLog.team==6).count
    msrtotal=FVisitorsLog.select().where(FVisitorsLog.team==5).count
    ygtotal=FVisitorsLog.select().where(FVisitorsLog.team!=5 & FVisitorsLog.team!=6).count

def index_pie_get():
    """
    Index Pie Chart
    Index Pie Chart

    :rtype: InlineResponse2001
    """

    try:
        print('--------')
        #上午积极统计（写成时间戳格式，下面判断）
        data1=FSysAttendance.select().where(FSysAttendance.type==1)
        m_start_time=int(timeTransposition((transpositionTime(int(time.time())-24*3600))[0:10]+' '+str(json.loads(data1[0].content)["startwork"]))/1000)
        # 上午结束统计（写成时间戳格式，下面判断）
        data1 = FSysAttendance.select().where(FSysAttendance.type == 1)
        m_end_time = int(timeTransposition(
            (transpositionTime(int(time.time())-24*3600))[0:10] + ' ' + str(json.loads(data1[0].content)["endwork"])) / 1000)




        #下午积极统计（写成时间戳格式，下面判断）
        data2 = FSysAttendance.select().where(FSysAttendance.type == 2)
        a_start_time=int(timeTransposition((transpositionTime(int(time.time())-24*3600))[0:10]+' '+str(json.loads(data2[0].content)["startwork"]))/1000)
        # 下午积极统计（写成时间戳格式，下面判断）
        data2 = FSysAttendance.select().where(FSysAttendance.type == 2)
        a_end_time = int(timeTransposition(
            (transpositionTime(int(time.time())-24*3600))[0:10] + ' ' + str(json.loads(data2[0].content)["endwork"])) / 1000)
        print(m_start_time,a_start_time,m_end_time,a_end_time)

        data=FDay.select()
        #全天
        normal = data.where(FDay.type == 0).count()
        late=data.where(FDay.type == 1).count()
        m_jj = data.where(FDay.times < m_start_time).count()
        a_jj =data.where((FDay.times < a_start_time) & (FDay.times > m_end_time)).count()
        early = data.where(FDay.type == 3).count()
        #上午
        m_normal = data.where((FDay.type == 0 )& (FDay.times < m_end_time)).count()
        m_late=data.where((FDay.type == 1 )& (FDay.times < m_end_time) & ((FDay.times > m_start_time))).count()
        m_early=data.where((FDay.type ==3 )&( FDay.times > m_start_time) & (FDay.times < m_end_time)).count()

        #下午
        a_normal = data.where((FDay.type == 0) & (FDay.times > m_end_time) & (FDay.times < a_start_time)).count()
        a_late = data.where((FDay.type == 1) & (FDay.times > a_start_time) & (FDay.times < a_end_time)).count()
        a_early = data.where((FDay.type ==3)  &( FDay.times > a_start_time) & (FDay.times < a_end_time)).count()
        print(a_late)
        msg = {"code": 0, "msg": "success","day":[{"name":"迟到","value":late},{"name":"正常","value":normal},{"name":"积极","value":m_jj+a_jj},{"name":"早退","value":early}],
               "morning":[{"name":"迟到","value":m_late},{"name":"正常","value":m_normal},{"name":"积极","value":m_jj},{"name":"早退","value":m_early}],
               "afternoon":[{"name":"迟到","value":a_late},{"name":"正常","value":a_normal},{"name":"积极","value":a_jj},{"name":"早退","value":a_early}]
               }

    except:
        msg={"code":-1,"msg":"Error"}



    return msg
