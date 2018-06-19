# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.inline_response20019_morning import InlineResponse20019Morning  # noqa: F401,E501
from swagger_server import util


class TcpServerList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code: int=None, msg: str=None, morning: List[InlineResponse20019Morning]=None):  # noqa: E501
        """TcpServerList - a model defined in Swagger

        :param code: The code of this TcpServerList.  # noqa: E501
        :type code: int
        :param msg: The msg of this TcpServerList.  # noqa: E501
        :type msg: str
        :param morning: The morning of this TcpServerList.  # noqa: E501
        :type morning: List[InlineResponse20019Morning]
        """
        self.swagger_types = {
            'code': int,
            'msg': str,
            'morning': List[InlineResponse20019Morning]
        }

        self.attribute_map = {
            'code': 'code',
            'msg': 'msg',
            'morning': 'morning'
        }

        self._code = code
        self._msg = msg
        self._morning = morning

    @classmethod
    def from_dict(cls, dikt) -> 'TcpServerList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TcpServerList of this TcpServerList.  # noqa: E501
        :rtype: TcpServerList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """Gets the code of this TcpServerList.

        system return code  # noqa: E501

        :return: The code of this TcpServerList.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this TcpServerList.

        system return code  # noqa: E501

        :param code: The code of this TcpServerList.
        :type code: int
        """

        self._code = code

    @property
    def msg(self) -> str:
        """Gets the msg of this TcpServerList.

        system return news  # noqa: E501

        :return: The msg of this TcpServerList.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg: str):
        """Sets the msg of this TcpServerList.

        system return news  # noqa: E501

        :param msg: The msg of this TcpServerList.
        :type msg: str
        """

        self._msg = msg

    @property
    def morning(self) -> List[InlineResponse20019Morning]:
        """Gets the morning of this TcpServerList.


        :return: The morning of this TcpServerList.
        :rtype: List[InlineResponse20019Morning]
        """
        return self._morning

    @morning.setter
    def morning(self, morning: List[InlineResponse20019Morning]):
        """Sets the morning of this TcpServerList.


        :param morning: The morning of this TcpServerList.
        :type morning: List[InlineResponse20019Morning]
        """

        self._morning = morning