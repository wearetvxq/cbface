import connexion
from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.models.inline_response20018 import InlineResponse20018
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from swagger_server.db import FSysTment, FPurpose

def label_team_get():
    """
    System department
    System department

    :rtype: InlineResponse20017
    """
    try:
        data = FSysTment.select().where(FSysTment.status==1)
        msg = {"code": 0, "msg": "success", "result":[{'id': item.id, 'name': item.name} for item in data]}
    except:
        msg = {"code": -1, "msg": "system error"}
    return msg

def label_purpose_get():
    """
    System purpose
    System purpose

    :rtype: InlineResponse20018
    """
    try:
        data = FPurpose.select().where(FPurpose.status==0)
        msg = {"code": 0, "msg": "success", "result":[{'id': item.id, 'name': item.name} for item in data]}
    except:
        msg = {"code": -1, "msg": "system error"}
    return msg
