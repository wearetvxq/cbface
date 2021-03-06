# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SystemTmentListResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, name: str=None, total: str=None, status: int=None, posttime: str=None):  # noqa: E501
        """SystemTmentListResult - a model defined in Swagger

        :param id: The id of this SystemTmentListResult.  # noqa: E501
        :type id: int
        :param name: The name of this SystemTmentListResult.  # noqa: E501
        :type name: str
        :param total: The total of this SystemTmentListResult.  # noqa: E501
        :type total: str
        :param status: The status of this SystemTmentListResult.  # noqa: E501
        :type status: int
        :param posttime: The posttime of this SystemTmentListResult.  # noqa: E501
        :type posttime: str
        """
        self.swagger_types = {
            'id': int,
            'name': str,
            'total': str,
            'status': int,
            'posttime': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'total': 'total',
            'status': 'status',
            'posttime': 'posttime'
        }

        self._id = id
        self._name = name
        self._total = total
        self._status = status
        self._posttime = posttime

    @classmethod
    def from_dict(cls, dikt) -> 'SystemTmentListResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SystemTmentListResult of this SystemTmentListResult.  # noqa: E501
        :rtype: SystemTmentListResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this SystemTmentListResult.

        ID  # noqa: E501

        :return: The id of this SystemTmentListResult.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this SystemTmentListResult.

        ID  # noqa: E501

        :param id: The id of this SystemTmentListResult.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this SystemTmentListResult.

        tment name  # noqa: E501

        :return: The name of this SystemTmentListResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this SystemTmentListResult.

        tment name  # noqa: E501

        :param name: The name of this SystemTmentListResult.
        :type name: str
        """

        self._name = name

    @property
    def total(self) -> str:
        """Gets the total of this SystemTmentListResult.

        tment num  # noqa: E501

        :return: The total of this SystemTmentListResult.
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total: str):
        """Sets the total of this SystemTmentListResult.

        tment num  # noqa: E501

        :param total: The total of this SystemTmentListResult.
        :type total: str
        """

        self._total = total

    @property
    def status(self) -> int:
        """Gets the status of this SystemTmentListResult.

        tment status  # noqa: E501

        :return: The status of this SystemTmentListResult.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status: int):
        """Sets the status of this SystemTmentListResult.

        tment status  # noqa: E501

        :param status: The status of this SystemTmentListResult.
        :type status: int
        """

        self._status = status

    @property
    def posttime(self) -> str:
        """Gets the posttime of this SystemTmentListResult.

        Create time  # noqa: E501

        :return: The posttime of this SystemTmentListResult.
        :rtype: str
        """
        return self._posttime

    @posttime.setter
    def posttime(self, posttime: str):
        """Sets the posttime of this SystemTmentListResult.

        Create time  # noqa: E501

        :param posttime: The posttime of this SystemTmentListResult.
        :type posttime: str
        """

        self._posttime = posttime
