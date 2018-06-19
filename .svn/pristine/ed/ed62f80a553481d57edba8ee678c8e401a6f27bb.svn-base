# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.body1 import Body1
from swagger_server.models.body10 import Body10
from swagger_server.models.body11 import Body11
from swagger_server.models.body12 import Body12
from swagger_server.models.body13 import Body13
from swagger_server.models.body14 import Body14
from swagger_server.models.body2 import Body2
from swagger_server.models.body3 import Body3
from swagger_server.models.body4 import Body4
from swagger_server.models.body5 import Body5
from swagger_server.models.body6 import Body6
from swagger_server.models.body7 import Body7
from swagger_server.models.body8 import Body8
from swagger_server.models.body9 import Body9
from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.models.inline_response20010 import InlineResponse20010
from swagger_server.models.inline_response20011 import InlineResponse20011
from swagger_server.models.inline_response20012 import InlineResponse20012
from swagger_server.models.inline_response20013 import InlineResponse20013
from swagger_server.models.inline_response20014 import InlineResponse20014
from swagger_server.models.inline_response20015 import InlineResponse20015
from swagger_server.models.inline_response20016 import InlineResponse20016
from swagger_server.models.inline_response2008 import InlineResponse2008
from swagger_server.models.inline_response2009 import InlineResponse2009
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestSystemController(BaseTestCase):
    """ SystemController integration test stubs """

    def test_system_access_delete(self):
        """
        Test case for system_access_delete

        System Tment Del
        """
        body = Body12()
        response = self.client.open('/v1/system/access',
                                    method='DELETE',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_system_access_get(self):
        """
        Test case for system_access_get

        System tment get
        """
        query_string = [('size', 'size_example'),
                        ('_from', '_from_example'),
                        ('keyword', 'keyword_example'),
                        ('status', 'status_example')]
        response = self.client.open('/v1/system/access',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_system_access_post(self):
        """
        Test case for system_access_post

        System Tment Add
        """
        body = Body11()
        response = self.client.open('/v1/system/access',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_system_access_put(self):
        """
        Test case for system_access_put

        System Tment Edit
        """
        body = Body10()
        response = self.client.open('/v1/system/access',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_system_access_query_id_get(self):
        """
        Test case for system_access_query_id_get

        System access get
        """
        response = self.client.open('/v1/system/access/query/{id}'.format(id='id_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_system_attendance_get(self):
        """
        Test case for system_attendance_get

        System attendance set
        """
        response = self.client.open('/v1/system/attendance',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_system_attendance_post(self):
        """
        Test case for system_attendance_post

        System attendance set
        """
        body = Body13()
        response = self.client.open('/v1/system/attendance',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_system_employee_delete(self):
        """
        Test case for system_employee_delete

        System employee Del
        """
        body = Body6()
        response = self.client.open('/v1/system/employee',
                                    method='DELETE',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_system_employee_export_get(self):
        """
        Test case for system_employee_export_get

        System employee export
        """
        query_string = [('team', 'team_example'),
                        ('keyword', 'keyword_example'),
                        ('status', 'status_example')]
        response = self.client.open('/v1/system/employee/export',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_system_employee_list_get(self):
        """
        Test case for system_employee_list_get

        System employee list
        """
        query_string = [('size', 'size_example'),
                        ('_from', '_from_example'),
                        ('team', 'team_example'),
                        ('keyword', 'keyword_example'),
                        ('status', 'status_example')]
        response = self.client.open('/v1/system/employee/list',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_system_employee_post(self):
        """
        Test case for system_employee_post

        System employee Add
        """
        body = Body5()
        response = self.client.open('/v1/system/employee',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_system_employee_put(self):
        """
        Test case for system_employee_put

        System employee Edit
        """
        body = Body4()
        response = self.client.open('/v1/system/employee',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_system_employee_query_id_get(self):
        """
        Test case for system_employee_query_id_get

        System employee get
        """
        response = self.client.open('/v1/system/employee/query/{id}'.format(id='id_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_system_password_post(self):
        """
        Test case for system_password_post

        System User Edit Password
        """
        body = Body14()
        response = self.client.open('/v1/system/password',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_system_tment_delete(self):
        """
        Test case for system_tment_delete

        System Tment Del
        """
        body = Body9()
        response = self.client.open('/v1/system/tment',
                                    method='DELETE',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_system_tment_export_get(self):
        """
        Test case for system_tment_export_get

        System tment export
        """
        query_string = [('keyword', 'keyword_example'),
                        ('status', 'status_example')]
        response = self.client.open('/v1/system/tment/export',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_system_tment_list_get(self):
        """
        Test case for system_tment_list_get

        System tment list
        """
        query_string = [('size', 'size_example'),
                        ('_from', '_from_example'),
                        ('keyword', 'keyword_example'),
                        ('status', 'status_example')]
        response = self.client.open('/v1/system/tment/list',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_system_tment_post(self):
        """
        Test case for system_tment_post

        System Tment Add
        """
        body = Body8()
        response = self.client.open('/v1/system/tment',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_system_tment_put(self):
        """
        Test case for system_tment_put

        System Tment Put
        """
        body = Body7()
        response = self.client.open('/v1/system/tment',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_system_tment_query_id_get(self):
        """
        Test case for system_tment_query_id_get

        System tment get
        """
        response = self.client.open('/v1/system/tment/query/{id}'.format(id='id_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_system_user_delete(self):
        """
        Test case for system_user_delete

        System User Del
        """
        body = Body3()
        response = self.client.open('/v1/system/user',
                                    method='DELETE',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_system_user_export_get(self):
        """
        Test case for system_user_export_get

        System User export
        """
        query_string = [('team', 'team_example'),
                        ('keyword', 'keyword_example'),
                        ('status', 'status_example')]
        response = self.client.open('/v1/system/user/export',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_system_user_list_get(self):
        """
        Test case for system_user_list_get

        System User list
        """
        query_string = [('size', 'size_example'),
                        ('_from', '_from_example'),
                        ('team', 'team_example'),
                        ('keyword', 'keyword_example'),
                        ('status', 'status_example')]
        response = self.client.open('/v1/system/user/list',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_system_user_post(self):
        """
        Test case for system_user_post

        System User Add
        """
        body = Body2()
        response = self.client.open('/v1/system/user',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_system_user_put(self):
        """
        Test case for system_user_put

        System User Edit
        """
        body = Body1()
        response = self.client.open('/v1/system/user',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_system_user_query_id_get(self):
        """
        Test case for system_user_query_id_get

        System User get
        """
        response = self.client.open('/v1/system/user/query/{id}'.format(id='id_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
