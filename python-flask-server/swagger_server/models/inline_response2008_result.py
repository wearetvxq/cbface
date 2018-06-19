# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse2008Result(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, username: str=None, mail: str=None, status: int=None, posttime: str=None):  # noqa: E501
        """InlineResponse2008Result - a model defined in Swagger

        :param id: The id of this InlineResponse2008Result.  # noqa: E501
        :type id: int
        :param username: The username of this InlineResponse2008Result.  # noqa: E501
        :type username: str
        :param mail: The mail of this InlineResponse2008Result.  # noqa: E501
        :type mail: str
        :param status: The status of this InlineResponse2008Result.  # noqa: E501
        :type status: int
        :param posttime: The posttime of this InlineResponse2008Result.  # noqa: E501
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
    def from_dict(cls, dikt) -> 'InlineResponse2008Result':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_8_result of this InlineResponse2008Result.  # noqa: E501
        :rtype: InlineResponse2008Result
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this InlineResponse2008Result.

        ID  # noqa: E501

        :return: The id of this InlineResponse2008Result.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this InlineResponse2008Result.

        ID  # noqa: E501

        :param id: The id of this InlineResponse2008Result.
        :type id: int
        """

        self._id = id

    @property
    def username(self) -> str:
        """Gets the username of this InlineResponse2008Result.

        Account name  # noqa: E501

        :return: The username of this InlineResponse2008Result.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this InlineResponse2008Result.

        Account name  # noqa: E501

        :param username: The username of this InlineResponse2008Result.
        :type username: str
        """

        self._username = username

    @property
    def mail(self) -> str:
        """Gets the mail of this InlineResponse2008Result.

        system login account  # noqa: E501

        :return: The mail of this InlineResponse2008Result.
        :rtype: str
        """
        return self._mail

    @mail.setter
    def mail(self, mail: str):
        """Sets the mail of this InlineResponse2008Result.

        system login account  # noqa: E501

        :param mail: The mail of this InlineResponse2008Result.
        :type mail: str
        """

        self._mail = mail

    @property
    def status(self) -> int:
        """Gets the status of this InlineResponse2008Result.

        account status  # noqa: E501

        :return: The status of this InlineResponse2008Result.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status: int):
        """Sets the status of this InlineResponse2008Result.

        account status  # noqa: E501

        :param status: The status of this InlineResponse2008Result.
        :type status: int
        """

        self._status = status

    @property
    def posttime(self) -> str:
        """Gets the posttime of this InlineResponse2008Result.

        Create time  # noqa: E501

        :return: The posttime of this InlineResponse2008Result.
        :rtype: str
        """
        return self._posttime

    @posttime.setter
    def posttime(self, posttime: str):
        """Sets the posttime of this InlineResponse2008Result.

        Create time  # noqa: E501

        :param posttime: The posttime of this InlineResponse2008Result.
        :type posttime: str
        """

        self._posttime = posttime