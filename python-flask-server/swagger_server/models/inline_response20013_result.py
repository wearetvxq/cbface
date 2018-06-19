# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse20013Result(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, name: str=None, status: int=None, remarks: int=None):  # noqa: E501
        """InlineResponse20013Result - a model defined in Swagger

        :param id: The id of this InlineResponse20013Result.  # noqa: E501
        :type id: int
        :param name: The name of this InlineResponse20013Result.  # noqa: E501
        :type name: str
        :param status: The status of this InlineResponse20013Result.  # noqa: E501
        :type status: int
        :param remarks: The remarks of this InlineResponse20013Result.  # noqa: E501
        :type remarks: int
        """
        self.swagger_types = {
            'id': int,
            'name': str,
            'status': int,
            'remarks': int
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'status': 'status',
            'remarks': 'remarks'
        }

        self._id = id
        self._name = name
        self._status = status
        self._remarks = remarks

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse20013Result':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_13_result of this InlineResponse20013Result.  # noqa: E501
        :rtype: InlineResponse20013Result
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this InlineResponse20013Result.

        user id  # noqa: E501

        :return: The id of this InlineResponse20013Result.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this InlineResponse20013Result.

        user id  # noqa: E501

        :param id: The id of this InlineResponse20013Result.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this InlineResponse20013Result.

        tment add  # noqa: E501

        :return: The name of this InlineResponse20013Result.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this InlineResponse20013Result.

        tment add  # noqa: E501

        :param name: The name of this InlineResponse20013Result.
        :type name: str
        """

        self._name = name

    @property
    def status(self) -> int:
        """Gets the status of this InlineResponse20013Result.

        tment status  # noqa: E501

        :return: The status of this InlineResponse20013Result.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status: int):
        """Sets the status of this InlineResponse20013Result.

        tment status  # noqa: E501

        :param status: The status of this InlineResponse20013Result.
        :type status: int
        """

        self._status = status

    @property
    def remarks(self) -> int:
        """Gets the remarks of this InlineResponse20013Result.

        tment remarks  # noqa: E501

        :return: The remarks of this InlineResponse20013Result.
        :rtype: int
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks: int):
        """Sets the remarks of this InlineResponse20013Result.

        tment remarks  # noqa: E501

        :param remarks: The remarks of this InlineResponse20013Result.
        :type remarks: int
        """

        self._remarks = remarks