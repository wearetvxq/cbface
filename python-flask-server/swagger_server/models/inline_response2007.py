# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.inline_response2007_basic import InlineResponse2007Basic  # noqa: F401,E501
from swagger_server.models.inline_response2007_topic import InlineResponse2007Topic  # noqa: F401,E501
from swagger_server import util


class InlineResponse2007(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code: int=None, msg: str=None, basic: List[InlineResponse2007Basic]=None, topic: List[InlineResponse2007Topic]=None):  # noqa: E501
        """InlineResponse2007 - a model defined in Swagger

        :param code: The code of this InlineResponse2007.  # noqa: E501
        :type code: int
        :param msg: The msg of this InlineResponse2007.  # noqa: E501
        :type msg: str
        :param basic: The basic of this InlineResponse2007.  # noqa: E501
        :type basic: List[InlineResponse2007Basic]
        :param topic: The topic of this InlineResponse2007.  # noqa: E501
        :type topic: List[InlineResponse2007Topic]
        """
        self.swagger_types = {
            'code': int,
            'msg': str,
            'basic': List[InlineResponse2007Basic],
            'topic': List[InlineResponse2007Topic]
        }

        self.attribute_map = {
            'code': 'code',
            'msg': 'msg',
            'basic': 'basic',
            'topic': 'topic'
        }

        self._code = code
        self._msg = msg
        self._basic = basic
        self._topic = topic

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2007':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_7 of this InlineResponse2007.  # noqa: E501
        :rtype: InlineResponse2007
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """Gets the code of this InlineResponse2007.

        system return code  # noqa: E501

        :return: The code of this InlineResponse2007.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this InlineResponse2007.

        system return code  # noqa: E501

        :param code: The code of this InlineResponse2007.
        :type code: int
        """

        self._code = code

    @property
    def msg(self) -> str:
        """Gets the msg of this InlineResponse2007.

        system return news  # noqa: E501

        :return: The msg of this InlineResponse2007.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg: str):
        """Sets the msg of this InlineResponse2007.

        system return news  # noqa: E501

        :param msg: The msg of this InlineResponse2007.
        :type msg: str
        """

        self._msg = msg

    @property
    def basic(self) -> List[InlineResponse2007Basic]:
        """Gets the basic of this InlineResponse2007.


        :return: The basic of this InlineResponse2007.
        :rtype: List[InlineResponse2007Basic]
        """
        return self._basic

    @basic.setter
    def basic(self, basic: List[InlineResponse2007Basic]):
        """Sets the basic of this InlineResponse2007.


        :param basic: The basic of this InlineResponse2007.
        :type basic: List[InlineResponse2007Basic]
        """

        self._basic = basic

    @property
    def topic(self) -> List[InlineResponse2007Topic]:
        """Gets the topic of this InlineResponse2007.


        :return: The topic of this InlineResponse2007.
        :rtype: List[InlineResponse2007Topic]
        """
        return self._topic

    @topic.setter
    def topic(self, topic: List[InlineResponse2007Topic]):
        """Sets the topic of this InlineResponse2007.


        :param topic: The topic of this InlineResponse2007.
        :type topic: List[InlineResponse2007Topic]
        """

        self._topic = topic
