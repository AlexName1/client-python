# coding: utf-8

"""
    Rest DB

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.users_api import UsersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_count_api_v1_users_count_get(self):
        """Test case for get_count_api_v1_users_count_get

        Get Count  # noqa: E501
        """
        pass

    def test_get_ids_api_v1_users_ids_get(self):
        """Test case for get_ids_api_v1_users_ids_get

        Get Ids  # noqa: E501
        """
        pass

    def test_get_items_api_v1_users_user_id_items_get(self):
        """Test case for get_items_api_v1_users_user_id_items_get

        Get Items  # noqa: E501
        """
        pass

    def test_get_user_api_v1_users_user_id_one_get(self):
        """Test case for get_user_api_v1_users_user_id_one_get

        Get User  # noqa: E501
        """
        pass

    def test_insert_or_nothing_api_v1_users_post(self):
        """Test case for insert_or_nothing_api_v1_users_post

        Insert Or Nothing  # noqa: E501
        """
        pass

    def test_update_items_api_v1_users_user_id_items_put(self):
        """Test case for update_items_api_v1_users_user_id_items_put

        Update Items  # noqa: E501
        """
        pass

    def test_update_last_mess_api_v1_users_user_id_mess_put(self):
        """Test case for update_last_mess_api_v1_users_user_id_mess_put

        Update Last Mess  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
