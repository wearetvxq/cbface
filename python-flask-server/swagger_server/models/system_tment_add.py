# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SystemTmentAdd(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, status: int=None, remarks: str=None):  # noqa: E501
        """SystemTmentAdd - a model defined in Swagger

        :param name: The name of this SystemTmentAdd.  # noqa: E501
        :type name: str
        :param status: The status of this SystemTmentAdd.  # noqa: E501
        :type status: int
        :param remarks: The remarks of this SystemTmentAdd.  # noqa: E501
        :type remarks: str
        """
        self.swagger_types = {
            'name': str,
            'status': int,
            'remarks': str
        }

        self.attribute_map = {
            'name': 'name',
            'status': 'status',
            'remarks': 'remarks'
        }

        self._name = name
        self._status = status
        self._remarks = remarks

    @classmethod
    def from_dict(cls, dikt) -> 'SystemTmentAdd':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SystemTmentAdd of this SystemTmentAdd.  # noqa: E501
        :rtype: SystemTmentAdd
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this SystemTmentAdd.

        tment add  # noqa: E501

        :return: The name of this SystemTmentAdd.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this SystemTmentAdd.

        tment add  # noqa: E501

        :param name: The name of this SystemTmentAdd.
        :type name: str
        """

        self._name = name

    @property
    def status(self) -> int:
        """Gets the status of this SystemTmentAdd.

        tment status  # noqa: E501

        :return: The status of this SystemTmentAdd.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status: int):
        """Sets the status of this SystemTmentAdd.

        tment status  # noqa: E501

        :param status: The status of this SystemTmentAdd.
        :type status: int
        """

        self._status = status

    @property
    def remarks(self) -> str:
        """Gets the remarks of this SystemTmentAdd.

        tment remarks  # noqa: E501

        :return: The remarks of this SystemTmentAdd.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks: str):
        """Sets the remarks of this SystemTmentAdd.

        tment remarks  # noqa: E501

        :param remarks: The remarks of this SystemTmentAdd.
        :type remarks: str
        """

        self._remarks = remarks
