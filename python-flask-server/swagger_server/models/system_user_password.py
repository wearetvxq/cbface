# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SystemUserPassword(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, old: str=None, new: str=None):  # noqa: E501
        """SystemUserPassword - a model defined in Swagger

        :param id: The id of this SystemUserPassword.  # noqa: E501
        :type id: str
        :param old: The old of this SystemUserPassword.  # noqa: E501
        :type old: str
        :param new: The new of this SystemUserPassword.  # noqa: E501
        :type new: str
        """
        self.swagger_types = {
            'id': str,
            'old': str,
            'new': str
        }

        self.attribute_map = {
            'id': 'id',
            'old': 'old',
            'new': 'new'
        }

        self._id = id
        self._old = old
        self._new = new

    @classmethod
    def from_dict(cls, dikt) -> 'SystemUserPassword':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SystemUserPassword of this SystemUserPassword.  # noqa: E501
        :rtype: SystemUserPassword
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this SystemUserPassword.

        user id  # noqa: E501

        :return: The id of this SystemUserPassword.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this SystemUserPassword.

        user id  # noqa: E501

        :param id: The id of this SystemUserPassword.
        :type id: str
        """

        self._id = id

    @property
    def old(self) -> str:
        """Gets the old of this SystemUserPassword.

        old password  # noqa: E501

        :return: The old of this SystemUserPassword.
        :rtype: str
        """
        return self._old

    @old.setter
    def old(self, old: str):
        """Sets the old of this SystemUserPassword.

        old password  # noqa: E501

        :param old: The old of this SystemUserPassword.
        :type old: str
        """

        self._old = old

    @property
    def new(self) -> str:
        """Gets the new of this SystemUserPassword.

        new password  # noqa: E501

        :return: The new of this SystemUserPassword.
        :rtype: str
        """
        return self._new

    @new.setter
    def new(self, new: str):
        """Sets the new of this SystemUserPassword.

        new password  # noqa: E501

        :param new: The new of this SystemUserPassword.
        :type new: str
        """

        self._new = new
