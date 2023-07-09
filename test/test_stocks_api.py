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
from swagger_client.api.stocks_api import StocksApi  # noqa: E501
from swagger_client.rest import ApiException


class TestStocksApi(unittest.TestCase):
    """StocksApi unit test stubs"""

    def setUp(self):
        self.api = StocksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_stock_by_stock_id_api_v1_stocks_user_stock_id_get(self):
        """Test case for get_stock_by_stock_id_api_v1_stocks_user_stock_id_get

        Get Stock By Stock Id  # noqa: E501
        """
        pass

    def test_get_stock_without_load_by_stock_id_api_v1_stocks_stock_id_get(self):
        """Test case for get_stock_without_load_by_stock_id_api_v1_stocks_stock_id_get

        Get Stock Without Load By Stock Id  # noqa: E501
        """
        pass

    def test_get_stocks_by_order_code_api_v1_stocks_code_size_get(self):
        """Test case for get_stocks_by_order_code_api_v1_stocks_code_size_get

        Get Stocks By Order Code  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
