# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class HomePasss(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, team: str=None, desc: str=None, posttime: str=None):  # noqa: E501
        """HomePasss - a model defined in Swagger

        :param name: The name of this HomePasss.  # noqa: E501
        :type name: str
        :param team: The team of this HomePasss.  # noqa: E501
        :type team: str
        :param desc: The desc of this HomePasss.  # noqa: E501
        :type desc: str
        :param posttime: The posttime of this HomePasss.  # noqa: E501
        :type posttime: str
        """
        self.swagger_types = {
            'name': str,
            'team': str,
            'desc': str,
            'posttime': str
        }

        self.attribute_map = {
            'name': 'name',
            'team': 'team',
            'desc': 'desc',
            'posttime': 'posttime'
        }

        self._name = name
        self._team = team
        self._desc = desc
        self._posttime = posttime

    @classmethod
    def from_dict(cls, dikt) -> 'HomePasss':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HomePasss of this HomePasss.  # noqa: E501
        :rtype: HomePasss
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this HomePasss.

        by user name  # noqa: E501

        :return: The name of this HomePasss.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this HomePasss.

        by user name  # noqa: E501

        :param name: The name of this HomePasss.
        :type name: str
        """

        self._name = name

    @property
    def team(self) -> str:
        """Gets the team of this HomePasss.

        by user team  # noqa: E501

        :return: The team of this HomePasss.
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team: str):
        """Sets the team of this HomePasss.

        by user team  # noqa: E501

        :param team: The team of this HomePasss.
        :type team: str
        """

        self._team = team

    @property
    def desc(self) -> str:
        """Gets the desc of this HomePasss.

        by user desc  # noqa: E501

        :return: The desc of this HomePasss.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc: str):
        """Sets the desc of this HomePasss.

        by user desc  # noqa: E501

        :param desc: The desc of this HomePasss.
        :type desc: str
        """

        self._desc = desc

    @property
    def posttime(self) -> str:
        """Gets the posttime of this HomePasss.

        by user time  # noqa: E501

        :return: The posttime of this HomePasss.
        :rtype: str
        """
        return self._posttime

    @posttime.setter
    def posttime(self, posttime: str):
        """Sets the posttime of this HomePasss.

        by user time  # noqa: E501

        :param posttime: The posttime of this HomePasss.
        :type posttime: str
        """

        self._posttime = posttime
