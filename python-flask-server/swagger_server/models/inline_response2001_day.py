# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse2001Day(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, val: str=None):  # noqa: E501
        """InlineResponse2001Day - a model defined in Swagger

        :param name: The name of this InlineResponse2001Day.  # noqa: E501
        :type name: str
        :param val: The val of this InlineResponse2001Day.  # noqa: E501
        :type val: str
        """
        self.swagger_types = {
            'name': str,
            'val': str
        }

        self.attribute_map = {
            'name': 'name',
            'val': 'val'
        }

        self._name = name
        self._val = val

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2001Day':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_1_day of this InlineResponse2001Day.  # noqa: E501
        :rtype: InlineResponse2001Day
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this InlineResponse2001Day.

        Pie Chart Name  # noqa: E501

        :return: The name of this InlineResponse2001Day.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this InlineResponse2001Day.

        Pie Chart Name  # noqa: E501

        :param name: The name of this InlineResponse2001Day.
        :type name: str
        """

        self._name = name

    @property
    def val(self) -> str:
        """Gets the val of this InlineResponse2001Day.

        Pie Chart val  # noqa: E501

        :return: The val of this InlineResponse2001Day.
        :rtype: str
        """
        return self._val

    @val.setter
    def val(self, val: str):
        """Sets the val of this InlineResponse2001Day.

        Pie Chart val  # noqa: E501

        :param val: The val of this InlineResponse2001Day.
        :type val: str
        """

        self._val = val