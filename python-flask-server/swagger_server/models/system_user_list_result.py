# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SystemUserListResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, username: str=None, mail: str=None, status: int=None, posttime: str=None):  # noqa: E501
        """SystemUserListResult - a model defined in Swagger

        :param id: The id of this SystemUserListResult.  # noqa: E501
        :type id: int
        :param username: The username of this SystemUserListResult.  # noqa: E501
        :type username: str
        :param mail: The mail of this SystemUserListResult.  # noqa: E501
        :type mail: str
        :param status: The status of this SystemUserListResult.  # noqa: E501
        :type status: int
        :param posttime: The posttime of this SystemUserListResult.  # noqa: E501
        :type posttime: str
        """
        self.swagger_types = {
            'id': int,
            'username': str,
            'mail': str,
            'status': int,
            'posttime': str
        }

        self.attribute_map = {
            'id': 'id',
            'username': 'username',
            'mail': 'mail',
            'status': 'status',
            'posttime': 'posttime'
        }

        self._id = id
        self._username = username
        self._mail = mail
        self._status = status
        self._posttime = posttime

    @classmethod
    def from_dict(cls, dikt) -> 'SystemUserListResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SystemUserListResult of this SystemUserListResult.  # noqa: E501
        :rtype: SystemUserListResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this SystemUserListResult.

        ID  # noqa: E501

        :return: The id of this SystemUserListResult.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this SystemUserListResult.

        ID  # noqa: E501

        :param id: The id of this SystemUserListResult.
        :type id: int
        """

        self._id = id

    @property
    def username(self) -> str:
        """Gets the username of this SystemUserListResult.

        Account name  # noqa: E501

        :return: The username of this SystemUserListResult.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this SystemUserListResult.

        Account name  # noqa: E501

        :param username: The username of this SystemUserListResult.
        :type username: str
        """

        self._username = username

    @property
    def mail(self) -> str:
        """Gets the mail of this SystemUserListResult.

        system login account  # noqa: E501

        :return: The mail of this SystemUserListResult.
        :rtype: str
        """
        return self._mail

    @mail.setter
    def mail(self, mail: str):
        """Sets the mail of this SystemUserListResult.

        system login account  # noqa: E501

        :param mail: The mail of this SystemUserListResult.
        :type mail: str
        """

        self._mail = mail

    @property
    def status(self) -> int:
        """Gets the status of this SystemUserListResult.

        account status  # noqa: E501

        :return: The status of this SystemUserListResult.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status: int):
        """Sets the status of this SystemUserListResult.

        account status  # noqa: E501

        :param status: The status of this SystemUserListResult.
        :type status: int
        """

        self._status = status

    @property
    def posttime(self) -> str:
        """Gets the posttime of this SystemUserListResult.

        Create time  # noqa: E501

        :return: The posttime of this SystemUserListResult.
        :rtype: str
        """
        return self._posttime

    @posttime.setter
    def posttime(self, posttime: str):
        """Sets the posttime of this SystemUserListResult.

        Create time  # noqa: E501

        :param posttime: The posttime of this SystemUserListResult.
        :type posttime: str
        """

        self._posttime = posttime
