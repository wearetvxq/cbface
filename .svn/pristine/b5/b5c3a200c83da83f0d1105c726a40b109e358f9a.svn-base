# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.models.inline_response2006 import InlineResponse2006
from swagger_server.models.inline_response2007 import InlineResponse2007
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestVisitorsController(BaseTestCase):
    """ VisitorsController integration test stubs """

    def test_visitors_export_get(self):
        """
        Test case for visitors_export_get

        Visitors Export
        """
        query_string = [('team', 'team_example'),
                        ('keyword', 'keyword_example'),
                        ('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example')]
        response = self.client.open('/v1/visitors/export',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_visitors_info_id_get(self):
        """
        Test case for visitors_info_id_get

        Visitors info
        """
        response = self.client.open('/v1/visitors/info/{id}'.format(id='id_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_visitors_list_get(self):
        """
        Test case for visitors_list_get

        Visitors list
        """
        query_string = [('size', 'size_example'),
                        ('_from', '_from_example'),
                        ('team', 'team_example'),
                        ('keyword', 'keyword_example'),
                        ('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example')]
        response = self.client.open('/v1/visitors/list',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
