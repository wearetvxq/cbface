# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.inline_response20014_child import InlineResponse20014Child  # noqa: F401,E501
from swagger_server import util


class SystemAccesss(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, status: str=None, level: str=None, type: str=None, child: List[InlineResponse20014Child]=None, posttime: str=None):  # noqa: E501
        """SystemAccesss - a model defined in Swagger

        :param name: The name of this SystemAccesss.  # noqa: E501
        :type name: str
        :param status: The status of this SystemAccesss.  # noqa: E501
        :type status: str
        :param level: The level of this SystemAccesss.  # noqa: E501
        :type level: str
        :param type: The type of this SystemAccesss.  # noqa: E501
        :type type: str
        :param child: The child of this SystemAccesss.  # noqa: E501
        :type child: List[InlineResponse20014Child]
        :param posttime: The posttime of this SystemAccesss.  # noqa: E501
        :type posttime: str
        """
        self.swagger_types = {
            'name': str,
            'status': str,
            'level': str,
            'type': str,
            'child': List[InlineResponse20014Child],
            'posttime': str
        }

        self.attribute_map = {
            'name': 'name',
            'status': 'status',
            'level': 'level',
            'type': 'type',
            'child': 'child',
            'posttime': 'posttime'
        }

        self._name = name
        self._status = status
        self._level = level
        self._type = type
        self._child = child
        self._posttime = posttime

    @classmethod
    def from_dict(cls, dikt) -> 'SystemAccesss':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SystemAccesss of this SystemAccesss.  # noqa: E501
        :rtype: SystemAccesss
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this SystemAccesss.

        access name  # noqa: E501

        :return: The name of this SystemAccesss.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this SystemAccesss.

        access name  # noqa: E501

        :param name: The name of this SystemAccesss.
        :type name: str
        """

        self._name = name

    @property
    def status(self) -> str:
        """Gets the status of this SystemAccesss.

        access status  # noqa: E501

        :return: The status of this SystemAccesss.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this SystemAccesss.

        access status  # noqa: E501

        :param status: The status of this SystemAccesss.
        :type status: str
        """

        self._status = status

    @property
    def level(self) -> str:
        """Gets the level of this SystemAccesss.

        access level  # noqa: E501

        :return: The level of this SystemAccesss.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level: str):
        """Sets the level of this SystemAccesss.

        access level  # noqa: E501

        :param level: The level of this SystemAccesss.
        :type level: str
        """

        self._level = level

    @property
    def type(self) -> str:
        """Gets the type of this SystemAccesss.

        access show  # noqa: E501

        :return: The type of this SystemAccesss.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this SystemAccesss.

        access show  # noqa: E501

        :param type: The type of this SystemAccesss.
        :type type: str
        """

        self._type = type

    @property
    def child(self) -> List[InlineResponse20014Child]:
        """Gets the child of this SystemAccesss.


        :return: The child of this SystemAccesss.
        :rtype: List[InlineResponse20014Child]
        """
        return self._child

    @child.setter
    def child(self, child: List[InlineResponse20014Child]):
        """Sets the child of this SystemAccesss.


        :param child: The child of this SystemAccesss.
        :type child: List[InlineResponse20014Child]
        """

        self._child = child

    @property
    def posttime(self) -> str:
        """Gets the posttime of this SystemAccesss.

        access add posttime  # noqa: E501

        :return: The posttime of this SystemAccesss.
        :rtype: str
        """
        return self._posttime

    @posttime.setter
    def posttime(self, posttime: str):
        """Sets the posttime of this SystemAccesss.

        access add posttime  # noqa: E501

        :param posttime: The posttime of this SystemAccesss.
        :type posttime: str
        """

        self._posttime = posttime