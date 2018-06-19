# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.inline_response20018_result import InlineResponse20018Result  # noqa: F401,E501
from swagger_server import util


class LabelTeam(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code: int=None, msg: str=None, result: List[InlineResponse20018Result]=None):  # noqa: E501
        """LabelTeam - a model defined in Swagger

        :param code: The code of this LabelTeam.  # noqa: E501
        :type code: int
        :param msg: The msg of this LabelTeam.  # noqa: E501
        :type msg: str
        :param result: The result of this LabelTeam.  # noqa: E501
        :type result: List[InlineResponse20018Result]
        """
        self.swagger_types = {
            'code': int,
            'msg': str,
            'result': List[InlineResponse20018Result]
        }

        self.attribute_map = {
            'code': 'code',
            'msg': 'msg',
            'result': 'result'
        }

        self._code = code
        self._msg = msg
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'LabelTeam':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LabelTeam of this LabelTeam.  # noqa: E501
        :rtype: LabelTeam
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """Gets the code of this LabelTeam.

        system return code  # noqa: E501

        :return: The code of this LabelTeam.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this LabelTeam.

        system return code  # noqa: E501

        :param code: The code of this LabelTeam.
        :type code: int
        """

        self._code = code

    @property
    def msg(self) -> str:
        """Gets the msg of this LabelTeam.

        system return news  # noqa: E501

        :return: The msg of this LabelTeam.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg: str):
        """Sets the msg of this LabelTeam.

        system return news  # noqa: E501

        :param msg: The msg of this LabelTeam.
        :type msg: str
        """

        self._msg = msg

    @property
    def result(self) -> List[InlineResponse20018Result]:
        """Gets the result of this LabelTeam.


        :return: The result of this LabelTeam.
        :rtype: List[InlineResponse20018Result]
        """
        return self._result

    @result.setter
    def result(self, result: List[InlineResponse20018Result]):
        """Sets the result of this LabelTeam.


        :param result: The result of this LabelTeam.
        :type result: List[InlineResponse20018Result]
        """

        self._result = result
