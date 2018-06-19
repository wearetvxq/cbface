# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.models.inline_response2001 import InlineResponse2001
from swagger_server.models.inline_response2002 import InlineResponse2002
from swagger_server.models.inline_response2003 import InlineResponse2003
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestHomeController(BaseTestCase):
    """ HomeController integration test stubs """

    def test_index_by_get(self):
        """
        Test case for index_by_get

        Index Pie Chart
        """
        response = self.client.open('/v1/index/by',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_index_log_get(self):
        """
        Test case for index_log_get

        Index Chart Log
        """
        response = self.client.open('/v1/index/log',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_index_pie_get(self):
        """
        Test case for index_pie_get

        Index Pie Chart
        """
        response = self.client.open('/v1/index/pie',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
