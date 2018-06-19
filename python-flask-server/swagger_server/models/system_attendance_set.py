# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.inline_response20016_morning import InlineResponse20016Morning  # noqa: F401,E501
from swagger_server import util


class SystemAttendanceSet(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code: int=None, msg: str=None, morning: List[InlineResponse20016Morning]=None, afternoon: List[InlineResponse20016Morning]=None):  # noqa: E501
        """SystemAttendanceSet - a model defined in Swagger

        :param code: The code of this SystemAttendanceSet.  # noqa: E501
        :type code: int
        :param msg: The msg of this SystemAttendanceSet.  # noqa: E501
        :type msg: str
        :param morning: The morning of this SystemAttendanceSet.  # noqa: E501
        :type morning: List[InlineResponse20016Morning]
        :param afternoon: The afternoon of this SystemAttendanceSet.  # noqa: E501
        :type afternoon: List[InlineResponse20016Morning]
        """
        self.swagger_types = {
            'code': int,
            'msg': str,
            'morning': List[InlineResponse20016Morning],
            'afternoon': List[InlineResponse20016Morning]
        }

        self.attribute_map = {
            'code': 'code',
            'msg': 'msg',
            'morning': 'morning',
            'afternoon': 'afternoon'
        }

        self._code = code
        self._msg = msg
        self._morning = morning
        self._afternoon = afternoon

    @classmethod
    def from_dict(cls, dikt) -> 'SystemAttendanceSet':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SystemAttendanceSet of this SystemAttendanceSet.  # noqa: E501
        :rtype: SystemAttendanceSet
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """Gets the code of this SystemAttendanceSet.

        system return code  # noqa: E501

        :return: The code of this SystemAttendanceSet.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this SystemAttendanceSet.

        system return code  # noqa: E501

        :param code: The code of this SystemAttendanceSet.
        :type code: int
        """

        self._code = code

    @property
    def msg(self) -> str:
        """Gets the msg of this SystemAttendanceSet.

        system return news  # noqa: E501

        :return: The msg of this SystemAttendanceSet.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg: str):
        """Sets the msg of this SystemAttendanceSet.

        system return news  # noqa: E501

        :param msg: The msg of this SystemAttendanceSet.
        :type msg: str
        """

        self._msg = msg

    @property
    def morning(self) -> List[InlineResponse20016Morning]:
        """Gets the morning of this SystemAttendanceSet.


        :return: The morning of this SystemAttendanceSet.
        :rtype: List[InlineResponse20016Morning]
        """
        return self._morning

    @morning.setter
    def morning(self, morning: List[InlineResponse20016Morning]):
        """Sets the morning of this SystemAttendanceSet.


        :param morning: The morning of this SystemAttendanceSet.
        :type morning: List[InlineResponse20016Morning]
        """

        self._morning = morning

    @property
    def afternoon(self) -> List[InlineResponse20016Morning]:
        """Gets the afternoon of this SystemAttendanceSet.


        :return: The afternoon of this SystemAttendanceSet.
        :rtype: List[InlineResponse20016Morning]
        """
        return self._afternoon

    @afternoon.setter
    def afternoon(self, afternoon: List[InlineResponse20016Morning]):
        """Sets the afternoon of this SystemAttendanceSet.


        :param afternoon: The afternoon of this SystemAttendanceSet.
        :type afternoon: List[InlineResponse20016Morning]
        """

        self._afternoon = afternoon