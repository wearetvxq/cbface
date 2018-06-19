import connexion
from swagger_server.models.body15 import Body15
from swagger_server.models.body16 import Body16
from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.models.inline_response20018 import InlineResponse20018
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def tcp_camera_get(status):
    """
    TCP Server Data
    TCP Server Data
    :param status: Demand Processing Status
    :type status: str

    :rtype: InlineResponse20018
    """
    return 'do some magic!'


def tcp_camera_post(body):
    """
    TCP Server Add Data
    TCP Server Add Data
    :param body: data
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Body16.from_dict(connexion.request.get_json())
    return 'do some magic!'


def tcp_camera_put(body):
    """
    TCP Server Edit Data
    TCP Server Edit Data
    :param body: data
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Body15.from_dict(connexion.request.get_json())
    return 'do some magic!'
