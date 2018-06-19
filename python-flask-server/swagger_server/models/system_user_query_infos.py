# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SystemUserQueryInfos(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, team: int=None, mail: str=None, passwd: str=None):  # noqa: E501
        """SystemUserQueryInfos - a model defined in Swagger

        :param id: The id of this SystemUserQueryInfos.  # noqa: E501
        :type id: int
        :param team: The team of this SystemUserQueryInfos.  # noqa: E501
        :type team: int
        :param mail: The mail of this SystemUserQueryInfos.  # noqa: E501
        :type mail: str
        :param passwd: The passwd of this SystemUserQueryInfos.  # noqa: E501
        :type passwd: str
        """
        self.swagger_types = {
            'id': int,
            'team': int,
            'mail': str,
            'passwd': str
        }

        self.attribute_map = {
            'id': 'id',
            'team': 'team',
            'mail': 'mail',
            'passwd': 'passwd'
        }

        self._id = id
        self._team = team
        self._mail = mail
        self._passwd = passwd

    @classmethod
    def from_dict(cls, dikt) -> 'SystemUserQueryInfos':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SystemUserQueryInfos of this SystemUserQueryInfos.  # noqa: E501
        :rtype: SystemUserQueryInfos
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this SystemUserQueryInfos.

        user id  # noqa: E501

        :return: The id of this SystemUserQueryInfos.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this SystemUserQueryInfos.

        user id  # noqa: E501

        :param id: The id of this SystemUserQueryInfos.
        :type id: int
        """

        self._id = id

    @property
    def team(self) -> int:
        """Gets the team of this SystemUserQueryInfos.

        team id  # noqa: E501

        :return: The team of this SystemUserQueryInfos.
        :rtype: int
        """
        return self._team

    @team.setter
    def team(self, team: int):
        """Sets the team of this SystemUserQueryInfos.

        team id  # noqa: E501

        :param team: The team of this SystemUserQueryInfos.
        :type team: int
        """

        self._team = team

    @property
    def mail(self) -> str:
        """Gets the mail of this SystemUserQueryInfos.

        login mail  # noqa: E501

        :return: The mail of this SystemUserQueryInfos.
        :rtype: str
        """
        return self._mail

    @mail.setter
    def mail(self, mail: str):
        """Sets the mail of this SystemUserQueryInfos.

        login mail  # noqa: E501

        :param mail: The mail of this SystemUserQueryInfos.
        :type mail: str
        """

        self._mail = mail

    @property
    def passwd(self) -> str:
        """Gets the passwd of this SystemUserQueryInfos.

        login password  # noqa: E501

        :return: The passwd of this SystemUserQueryInfos.
        :rtype: str
        """
        return self._passwd

    @passwd.setter
    def passwd(self, passwd: str):
        """Sets the passwd of this SystemUserQueryInfos.

        login password  # noqa: E501

        :param passwd: The passwd of this SystemUserQueryInfos.
        :type passwd: str
        """

        self._passwd = passwd
