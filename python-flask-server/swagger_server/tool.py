import hashlib, base64, calendar, time
from datetime import datetime
from swagger_server.db import *
#系统加密方法
def encryption(data):
    encodestr = base64.b64encode(data.encode(encoding="utf-8"))
    mstr = encodestr.decode('UTF-8')[::-1].upper()
    return hashlib.md5(mstr.encode('UTF-8')).hexdigest().upper()

#根据id获取name
def getname(id):
    try:
        name=[FSysEmployee.get(FSysEmployee.id==id).username,FSysEmployee.get(FSysEmployee.id==id).tment]
    except:
        name=['系统没有录入该员工',14]
    return name

#根据name获取id
def getid(name):
    try:
        id=[FSysEmployee.get(FSysEmployee.username==name).id,FSysEmployee.get(FSysEmployee.username==name).tment]
    except:
        id=['系统没有录入该员工',14]
    return id



#根据ID获取部门名称
def getTment(id):
    data = FSysTment.get(FSysTment.id == id)
    return data.name
#根据部门名称获取ID
def getID(tment):
    data = FSysTment.get(FSysTment.name == tment)
    return data.id
#根据编码获取性别
def getsex(sex):
    if sex==1:
        s='男'
    elif sex==2:
        s='女'
    return s

#根据数字获取中文考勤状态
def getAtttStatus(status):
    if status == 0:
        t = '正常'
    elif status == 1:
        t = '迟到'
    elif status == 2:
        t = '脱岗'
    elif status == 3:
        t = '早退'
    elif status == 4:
        t = '缺勤'
    return t
#根据中文考勤状态获取数字
def getStatusAttt(attt):
    if attt == '正常':
        t = 0
    elif attt == '迟到':
        t = 1
    elif attt == '脱岗':
        t = 2
    elif attt == '早退':
        t = 3
    elif attt == '缺勤':
        t = 4
    return t
#根据访客状态返回状态码
def getstatusPeople(tment):
    if tment=='离开':
        t=-1
    if tment=='再访':
        t=0
    return t
#根据状态码返回访客状态
def getpeopleStatus(status):
    if status==-1:
        t='离开'
    if status==0:
        t='再访'
    return t

#根据来访目的id返回来访目的
def getpurpose(id):
    data = FPurpose.get(FPurpose.id == id)
    return data.name


#根据部门id查找到对应的员工列表
def fortmentgetman(tmentid):
    idlist=[]
    result=FSysEmployee.select().where(FSysEmployee.tment==tmentid)
    for item in result:
        idlist.append(item.id)
    return idlist

# 启用状态和禁止状态
def getstatusid(type):
    if type=='禁用':
        it=0
    else:
        it=1
    return it
def getidstatus(it):
    if it==0:
        st='禁用'
    else:
        st='启用'
    return st


#将时间戳转为格式化时间
def transpositionTime(timestamp):
     # 转换成localtime
     if timestamp!=1:
        time_local = time.localtime(timestamp)
    # 转换成新的时间格式(2016-05-05 20:28:54)
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
     else:
        dt=''
     return dt
def timeTransposition(dt):
    local_datatime=datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
    timestamp = utc_datetime_to_timestamp(local_datatime)
    return timestamp
def timestamp_to_utc_strtime(timestamp):
    """将 13 位整数的毫秒时间戳转化成 utc 时间 (字符串格式，含毫秒)
    :param timestamp: 13 位整数的毫秒时间戳 (1456402864242)
    :return: 返回字符串格式 {str}'2016-02-25 12:21:04.242000'
    """
    utc_str_time = datetime.utcfromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')
    return utc_str_time
def timestamp_to_utc_datetime(timestamp):
    """将 13 位整数的毫秒时间戳转化成 utc 时间 (datetime 格式)
    :param timestamp: 13 位整数的时间戳 (1456402864242)
    :return: 返回 datetime 格式 {datetime}2016-02-25 12:21:04.242000
    """
    utc_dt_time = datetime.utcfromtimestamp(timestamp / 1000.0)
    return utc_dt_time
def utc_datetime_to_timestamp(utc_datetime):
    """将 utc 时间 (datetime 格式) 转为 utc 时间戳
    :param utc_datetime: {datetime}2016-02-25 20:21:04.242000
    :return: 13位 的毫秒时间戳 1456431664242
    """
    utc_timestamp = int(calendar.timegm(utc_datetime.timetuple()) * 1000.0 + utc_datetime.microsecond / 1000.0)
    return utc_timestamp
def datetime_to_strtime(datetime_obj):
    """将 datetime 格式的时间 (含毫秒) 转为字符串格式
    :param datetime_obj: {datetime}2016-02-25 20:21:04.242000
    :return: {str}'2016-02-25 20:21:04.242'
    """
    local_str_time = datetime_obj.strftime("%Y-%m-%d %H:%M:%S.%f")
    return local_str_time
def strtime_to_datetime(timestr):
    """将字符串格式的时间 (含毫秒) 转为 datetiem 格式
    :param timestr: {str}'2016-02-25 20:21:04.242'
    :return: {datetime}2016-02-25 20:21:04.242000
    """
    local_datetime = datetime.strptime(timestr, "%Y-%m-%d %H:%M:%S.%f")
    return local_datetime
def utc_strtime_to_timestamp(utc_timestr):
    """将 utc 时间 (字符串格式) 转为 13 位的时间戳
    :param utc_timestr: {str}'2016-02-25 20:21:04.242'
    :return: 1456431664242
    """
    # 先将字符串的格式转为 datetime 格式
    utc_datetime = strtime_to_datetime(utc_timestr)
    # 再将 datetime 格式的时间转为时间戳
    timestamp = utc_datetime_to_timestamp(utc_datetime)
    return timestamp
def utc_current_datetime():
    """返回 utc 当前时间, datetime 格式, 字符串格式, 时间戳格式
    :return: (datetime 格式, 字符串格式, 时间戳格式)
    """
    # utc 当前时间: datetime 格式
    utc_datetime_now = datetime.utcnow()
    # utc 当前时间: 字符串格式
    utc_strtime_now = datetime_to_strtime(utc_datetime_now)
    # utc 当前时间: 时间戳格式 13位整数
    utc_timestamp_now = utc_datetime_to_timestamp(utc_datetime_now)
    return utc_datetime_now, utc_strtime_now, utc_timestamp_now



#将时分秒转成时间戳，方便考勤记录
def utc_strtime_to_timestampshort(utc_timestr):
    """将 utc 时间 (字符串格式) 转为 13 位的时间戳
    :param utc_timestr: {str}'2016-02-25 20:21:04.242'
    :return: 1456431664242
    """
    # 先将字符串的格式转为 datetime 格式
    utc_datetime  = datetime.strptime(utc_timestr, "%Y-%m-%d")
    # 再将 datetime 格式的时间转为时间戳
    timestamp = utc_datetime_to_timestamp(utc_datetime)
    return timestamp
