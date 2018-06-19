# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.models.inline_response2004 import InlineResponse2004
from swagger_server.models.inline_response2005 import InlineResponse2005
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAttendanceController(BaseTestCase):
    """ AttendanceController integration test stubs """

    def test_attendance_export_get(self):
        """
        Test case for attendance_export_get

        attendance export
        """
        query_string = [('team', 'team_example'),
                        ('keyword', 'keyword_example'),
                        ('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example')]
        response = self.client.open('/v1/attendance/export',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_attendance_info_id_get(self):
        """
        Test case for attendance_info_id_get

        attendance info
        """
        response = self.client.open('/v1/attendance/info/{id}'.format(id='id_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_attendance_list_get(self):
        """
        Test case for attendance_list_get

        attendance list
        """
        query_string = [('size', 'size_example'),
                        ('_from', '_from_example'),
                        ('team', 'team_example'),
                        ('keyword', 'keyword_example'),
                        ('starttime', 'starttime_example'),
                        ('endtime', 'endtime_example')]
        response = self.client.open('/v1/attendance/list',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
