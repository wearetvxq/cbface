# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.body import Body
from swagger_server.models.inline_response200 import InlineResponse200
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestUserController(BaseTestCase):
    """ UserController integration test stubs """

    def test_login_post(self):
        """
        Test case for login_post

        User Login
        """
        body = Body()
        response = self.client.open('/v1/login',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
