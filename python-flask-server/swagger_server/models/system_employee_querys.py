# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SystemEmployeeQuerys(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, topic: str=None, username: str=None, team: str=None, sex: int=None, remarks: str=None):  # noqa: E501
        """SystemEmployeeQuerys - a model defined in Swagger

        :param id: The id of this SystemEmployeeQuerys.  # noqa: E501
        :type id: int
        :param topic: The topic of this SystemEmployeeQuerys.  # noqa: E501
        :type topic: str
        :param username: The username of this SystemEmployeeQuerys.  # noqa: E501
        :type username: str
        :param team: The team of this SystemEmployeeQuerys.  # noqa: E501
        :type team: str
        :param sex: The sex of this SystemEmployeeQuerys.  # noqa: E501
        :type sex: int
        :param remarks: The remarks of this SystemEmployeeQuerys.  # noqa: E501
        :type remarks: str
        """
        self.swagger_types = {
            'id': int,
            'topic': str,
            'username': str,
            'team': str,
            'sex': int,
            'remarks': str
        }

        self.attribute_map = {
            'id': 'id',
            'topic': 'topic',
            'username': 'username',
            'team': 'team',
            'sex': 'sex',
            'remarks': 'remarks'
        }

        self._id = id
        self._topic = topic
        self._username = username
        self._team = team
        self._sex = sex
        self._remarks = remarks

    @classmethod
    def from_dict(cls, dikt) -> 'SystemEmployeeQuerys':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SystemEmployeeQuerys of this SystemEmployeeQuerys.  # noqa: E501
        :rtype: SystemEmployeeQuerys
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this SystemEmployeeQuerys.

        user id  # noqa: E501

        :return: The id of this SystemEmployeeQuerys.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this SystemEmployeeQuerys.

        user id  # noqa: E501

        :param id: The id of this SystemEmployeeQuerys.
        :type id: int
        """

        self._id = id

    @property
    def topic(self) -> str:
        """Gets the topic of this SystemEmployeeQuerys.

        employee topic url  # noqa: E501

        :return: The topic of this SystemEmployeeQuerys.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic: str):
        """Sets the topic of this SystemEmployeeQuerys.

        employee topic url  # noqa: E501

        :param topic: The topic of this SystemEmployeeQuerys.
        :type topic: str
        """

        self._topic = topic

    @property
    def username(self) -> str:
        """Gets the username of this SystemEmployeeQuerys.

        employee username  # noqa: E501

        :return: The username of this SystemEmployeeQuerys.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this SystemEmployeeQuerys.

        employee username  # noqa: E501

        :param username: The username of this SystemEmployeeQuerys.
        :type username: str
        """

        self._username = username

    @property
    def team(self) -> str:
        """Gets the team of this SystemEmployeeQuerys.

        team  # noqa: E501

        :return: The team of this SystemEmployeeQuerys.
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team: str):
        """Sets the team of this SystemEmployeeQuerys.

        team  # noqa: E501

        :param team: The team of this SystemEmployeeQuerys.
        :type team: str
        """

        self._team = team

    @property
    def sex(self) -> int:
        """Gets the sex of this SystemEmployeeQuerys.

        employee sex  # noqa: E501

        :return: The sex of this SystemEmployeeQuerys.
        :rtype: int
        """
        return self._sex

    @sex.setter
    def sex(self, sex: int):
        """Sets the sex of this SystemEmployeeQuerys.

        employee sex  # noqa: E501

        :param sex: The sex of this SystemEmployeeQuerys.
        :type sex: int
        """

        self._sex = sex

    @property
    def remarks(self) -> str:
        """Gets the remarks of this SystemEmployeeQuerys.

        employee remarks  # noqa: E501

        :return: The remarks of this SystemEmployeeQuerys.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks: str):
        """Sets the remarks of this SystemEmployeeQuerys.

        employee remarks  # noqa: E501

        :param remarks: The remarks of this SystemEmployeeQuerys.
        :type remarks: str
        """

        self._remarks = remarks