# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse20021Pic(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, img: str=None):  # noqa: E501
        """InlineResponse20021Pic - a model defined in Swagger

        :param img: The img of this InlineResponse20021Pic.  # noqa: E501
        :type img: str
        """
        self.swagger_types = {
            'img': str
        }

        self.attribute_map = {
            'img': 'img'
        }

        self._img = img

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse20021Pic':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_21_pic of this InlineResponse20021Pic.  # noqa: E501
        :rtype: InlineResponse20021Pic
        """
        return util.deserialize_model(dikt, cls)

    @property
    def img(self) -> str:
        """Gets the img of this InlineResponse20021Pic.

        id  # noqa: E501

        :return: The img of this InlineResponse20021Pic.
        :rtype: str
        """
        return self._img

    @img.setter
    def img(self, img: str):
        """Sets the img of this InlineResponse20021Pic.

        id  # noqa: E501

        :param img: The img of this InlineResponse20021Pic.
        :type img: str
        """

        self._img = img
