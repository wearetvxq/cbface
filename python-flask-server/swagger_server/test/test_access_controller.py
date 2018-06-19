# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.body19 import Body19
from swagger_server.models.body20 import Body20
from swagger_server.models.body21 import Body21
from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.models.inline_response20020 import InlineResponse20020
from swagger_server.models.inline_response20021 import InlineResponse20021
from swagger_server.models.inline_response20022 import InlineResponse20022
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAccessController(BaseTestCase):
    """ AccessController integration test stubs """

    def test_access_delete(self):
        """
        Test case for access_delete

        Access Del
        """
        body = Body21()
        response = self.client.open('/v1/access',
                                    method='DELETE',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_access_get(self):
        """
        Test case for access_get

        Access List
        """
        query_string = [('size', 'size_example'),
                        ('_from', '_from_example'),
                        ('keyword', 'keyword_example'),
                        ('status', 'status_example')]
        response = self.client.open('/v1/access',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_access_level_level_get(self):
        """
        Test case for access_level_level_get

        Access Query Info
        """
        response = self.client.open('/v1/access/level/{level}'.format(level='level_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_access_post(self):
        """
        Test case for access_post

        Access Add
        """
        body = Body20()
        response = self.client.open('/v1/access',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_access_put(self):
        """
        Test case for access_put

        Access Edit
        """
        body = Body19()
        response = self.client.open('/v1/access',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_access_query_id_get(self):
        """
        Test case for access_query_id_get

        Access Query Info
        """
        response = self.client.open('/v1/access/query/{id}'.format(id='id_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
