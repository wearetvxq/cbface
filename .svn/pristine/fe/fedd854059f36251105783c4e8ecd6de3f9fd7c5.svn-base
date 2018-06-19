# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.body15 import Body15
from swagger_server.models.body16 import Body16
from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.models.inline_response20018 import InlineResponse20018
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestCameraController(BaseTestCase):
    """ CameraController integration test stubs """

    def test_tcp_camera_get(self):
        """
        Test case for tcp_camera_get

        TCP Server Data
        """
        query_string = [('status', 'status_example')]
        response = self.client.open('/v1/tcp/camera',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_tcp_camera_post(self):
        """
        Test case for tcp_camera_post

        TCP Server Add Data
        """
        body = Body16()
        response = self.client.open('/v1/tcp/camera',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_tcp_camera_put(self):
        """
        Test case for tcp_camera_put

        TCP Server Edit Data
        """
        body = Body15()
        response = self.client.open('/v1/tcp/camera',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
