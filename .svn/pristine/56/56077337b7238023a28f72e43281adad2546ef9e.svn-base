# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.models.inline_response20017 import InlineResponse20017
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestLabelController(BaseTestCase):
    """ LabelController integration test stubs """

    def test_label_team_get(self):
        """
        Test case for label_team_get

        System department
        """
        response = self.client.open('/v1/label/team',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
