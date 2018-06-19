# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.inline_response2008_result import InlineResponse2008Result  # noqa: F401,E501
from swagger_server import util


class InlineResponse2008(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code: int=None, msg: str=None, total: int=None, result: List[InlineResponse2008Result]=None):  # noqa: E501
        """InlineResponse2008 - a model defined in Swagger

        :param code: The code of this InlineResponse2008.  # noqa: E501
        :type code: int
        :param msg: The msg of this InlineResponse2008.  # noqa: E501
        :type msg: str
        :param total: The total of this InlineResponse2008.  # noqa: E501
        :type total: int
        :param result: The result of this InlineResponse2008.  # noqa: E501
        :type result: List[InlineResponse2008Result]
        """
        self.swagger_types = {
            'code': int,
            'msg': str,
            'total': int,
            'result': List[InlineResponse2008Result]
        }

        self.attribute_map = {
            'code': 'code',
            'msg': 'msg',
            'total': 'total',
            'result': 'result'
        }

        self._code = code
        self._msg = msg
        self._total = total
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2008':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_8 of this InlineResponse2008.  # noqa: E501
        :rtype: InlineResponse2008
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """Gets the code of this InlineResponse2008.

        system return code  # noqa: E501

        :return: The code of this InlineResponse2008.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this InlineResponse2008.

        system return code  # noqa: E501

        :param code: The code of this InlineResponse2008.
        :type code: int
        """

        self._code = code

    @property
    def msg(self) -> str:
        """Gets the msg of this InlineResponse2008.

        system return news  # noqa: E501

        :return: The msg of this InlineResponse2008.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg: str):
        """Sets the msg of this InlineResponse2008.

        system return news  # noqa: E501

        :param msg: The msg of this InlineResponse2008.
        :type msg: str
        """

        self._msg = msg

    @property
    def total(self) -> int:
        """Gets the total of this InlineResponse2008.

        list total  # noqa: E501

        :return: The total of this InlineResponse2008.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total: int):
        """Sets the total of this InlineResponse2008.

        list total  # noqa: E501

        :param total: The total of this InlineResponse2008.
        :type total: int
        """

        self._total = total

    @property
    def result(self) -> List[InlineResponse2008Result]:
        """Gets the result of this InlineResponse2008.


        :return: The result of this InlineResponse2008.
        :rtype: List[InlineResponse2008Result]
        """
        return self._result

    @result.setter
    def result(self, result: List[InlineResponse2008Result]):
        """Sets the result of this InlineResponse2008.


        :param result: The result of this InlineResponse2008.
        :type result: List[InlineResponse2008Result]
        """

        self._result = result
