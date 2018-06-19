# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SystemTmentListMorning(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, startwork: str=None, endwork: str=None, startwork_late: str=None, endwork_late: str=None):  # noqa: E501
        """SystemTmentListMorning - a model defined in Swagger

        :param startwork: The startwork of this SystemTmentListMorning.  # noqa: E501
        :type startwork: str
        :param endwork: The endwork of this SystemTmentListMorning.  # noqa: E501
        :type endwork: str
        :param startwork_late: The startwork_late of this SystemTmentListMorning.  # noqa: E501
        :type startwork_late: str
        :param endwork_late: The endwork_late of this SystemTmentListMorning.  # noqa: E501
        :type endwork_late: str
        """
        self.swagger_types = {
            'startwork': str,
            'endwork': str,
            'startwork_late': str,
            'endwork_late': str
        }

        self.attribute_map = {
            'startwork': 'startwork',
            'endwork': 'endwork',
            'startwork_late': 'startwork_late',
            'endwork_late': 'endwork_late'
        }

        self._startwork = startwork
        self._endwork = endwork
        self._startwork_late = startwork_late
        self._endwork_late = endwork_late

    @classmethod
    def from_dict(cls, dikt) -> 'SystemTmentListMorning':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SystemTmentListMorning of this SystemTmentListMorning.  # noqa: E501
        :rtype: SystemTmentListMorning
        """
        return util.deserialize_model(dikt, cls)

    @property
    def startwork(self) -> str:
        """Gets the startwork of this SystemTmentListMorning.

        start work time  # noqa: E501

        :return: The startwork of this SystemTmentListMorning.
        :rtype: str
        """
        return self._startwork

    @startwork.setter
    def startwork(self, startwork: str):
        """Sets the startwork of this SystemTmentListMorning.

        start work time  # noqa: E501

        :param startwork: The startwork of this SystemTmentListMorning.
        :type startwork: str
        """

        self._startwork = startwork

    @property
    def endwork(self) -> str:
        """Gets the endwork of this SystemTmentListMorning.

        end work time  # noqa: E501

        :return: The endwork of this SystemTmentListMorning.
        :rtype: str
        """
        return self._endwork

    @endwork.setter
    def endwork(self, endwork: str):
        """Sets the endwork of this SystemTmentListMorning.

        end work time  # noqa: E501

        :param endwork: The endwork of this SystemTmentListMorning.
        :type endwork: str
        """

        self._endwork = endwork

    @property
    def startwork_late(self) -> str:
        """Gets the startwork_late of this SystemTmentListMorning.

        end work time  # noqa: E501

        :return: The startwork_late of this SystemTmentListMorning.
        :rtype: str
        """
        return self._startwork_late

    @startwork_late.setter
    def startwork_late(self, startwork_late: str):
        """Sets the startwork_late of this SystemTmentListMorning.

        end work time  # noqa: E501

        :param startwork_late: The startwork_late of this SystemTmentListMorning.
        :type startwork_late: str
        """

        self._startwork_late = startwork_late

    @property
    def endwork_late(self) -> str:
        """Gets the endwork_late of this SystemTmentListMorning.

        end work time  # noqa: E501

        :return: The endwork_late of this SystemTmentListMorning.
        :rtype: str
        """
        return self._endwork_late

    @endwork_late.setter
    def endwork_late(self, endwork_late: str):
        """Sets the endwork_late of this SystemTmentListMorning.

        end work time  # noqa: E501

        :param endwork_late: The endwork_late of this SystemTmentListMorning.
        :type endwork_late: str
        """

        self._endwork_late = endwork_late