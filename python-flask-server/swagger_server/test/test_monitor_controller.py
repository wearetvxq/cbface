# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.body17 import Body17
from swagger_server.models.body18 import Body18
from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.models.inline_response20019 import InlineResponse20019
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestMonitorController(BaseTestCase):
    """ MonitorController integration test stubs """

    def test_monitor_get(self):
        """
        Test case for monitor_get

        Get access to people information
        """
        query_string = [('status', 'status_example')]
        response = self.client.open('/v1/monitor',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_monitor_open_post(self):
        """
        Test case for monitor_open_post

        Open
        """
        body = Body18()
        response = self.client.open('/v1/monitor/open',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_monitor_post(self):
        """
        Test case for monitor_post

        Update visitor log
        """
        body = Body17()
        response = self.client.open('/v1/monitor',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
