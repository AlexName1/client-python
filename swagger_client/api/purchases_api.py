# coding: utf-8

"""
    Rest DB

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class PurchasesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_purchase_api_v1_purchases_purchase_id_delete(self, purchase_id, **kwargs):  # noqa: E501
        """Delete Purchase  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_purchase_api_v1_purchases_purchase_id_delete(purchase_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int purchase_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_purchase_api_v1_purchases_purchase_id_delete_with_http_info(purchase_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_purchase_api_v1_purchases_purchase_id_delete_with_http_info(purchase_id, **kwargs)  # noqa: E501
            return data

    def delete_purchase_api_v1_purchases_purchase_id_delete_with_http_info(self, purchase_id, **kwargs):  # noqa: E501
        """Delete Purchase  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_purchase_api_v1_purchases_purchase_id_delete_with_http_info(purchase_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int purchase_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['purchase_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_purchase_api_v1_purchases_purchase_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'purchase_id' is set
        if ('purchase_id' not in params or
                params['purchase_id'] is None):
            raise ValueError("Missing the required parameter `purchase_id` when calling `delete_purchase_api_v1_purchases_purchase_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'purchase_id' in params:
            path_params['purchase_id'] = params['purchase_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HTTPBasic']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/purchases/{purchase_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_api_v1_purchases_get(self, token, **kwargs):  # noqa: E501
        """Get All  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_api_v1_purchases_get(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: (required)
        :return: list[PurchaseBaseDb]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_api_v1_purchases_get_with_http_info(token, **kwargs)  # noqa: E501
        else:
            (data) = self.get_all_api_v1_purchases_get_with_http_info(token, **kwargs)  # noqa: E501
            return data

    def get_all_api_v1_purchases_get_with_http_info(self, token, **kwargs):  # noqa: E501
        """Get All  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_api_v1_purchases_get_with_http_info(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: (required)
        :return: list[PurchaseBaseDb]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_api_v1_purchases_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if ('token' not in params or
                params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `get_all_api_v1_purchases_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HTTPBasic']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/purchases', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PurchaseBaseDb]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_count_api_v1_purchases_token_status_count_get(self, token, status, **kwargs):  # noqa: E501
        """Get Count  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_count_api_v1_purchases_token_status_count_get(token, status, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: (required)
        :param int status: (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_count_api_v1_purchases_token_status_count_get_with_http_info(token, status, **kwargs)  # noqa: E501
        else:
            (data) = self.get_count_api_v1_purchases_token_status_count_get_with_http_info(token, status, **kwargs)  # noqa: E501
            return data

    def get_count_api_v1_purchases_token_status_count_get_with_http_info(self, token, status, **kwargs):  # noqa: E501
        """Get Count  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_count_api_v1_purchases_token_status_count_get_with_http_info(token, status, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: (required)
        :param int status: (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token', 'status']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_count_api_v1_purchases_token_status_count_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if ('token' not in params or
                params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `get_count_api_v1_purchases_token_status_count_get`")  # noqa: E501
        # verify the required parameter 'status' is set
        if ('status' not in params or
                params['status'] is None):
            raise ValueError("Missing the required parameter `status` when calling `get_count_api_v1_purchases_token_status_count_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'token' in params:
            path_params['token'] = params['token']  # noqa: E501
        if 'status' in params:
            path_params['status'] = params['status']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HTTPBasic']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/purchases/{token}/{status}/count', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_purchase_by_id_api_v1_purchases_purchase_id_get(self, purchase_id, token, **kwargs):  # noqa: E501
        """Get Purchase By Id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_purchase_by_id_api_v1_purchases_purchase_id_get(purchase_id, token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int purchase_id: (required)
        :param str token: (required)
        :param bool delivery_cdek:
        :param bool waybill:
        :param bool stock:
        :param bool user_stock:
        :return: PurchaseBaseDb
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_purchase_by_id_api_v1_purchases_purchase_id_get_with_http_info(purchase_id, token, **kwargs)  # noqa: E501
        else:
            (data) = self.get_purchase_by_id_api_v1_purchases_purchase_id_get_with_http_info(purchase_id, token, **kwargs)  # noqa: E501
            return data

    def get_purchase_by_id_api_v1_purchases_purchase_id_get_with_http_info(self, purchase_id, token, **kwargs):  # noqa: E501
        """Get Purchase By Id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_purchase_by_id_api_v1_purchases_purchase_id_get_with_http_info(purchase_id, token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int purchase_id: (required)
        :param str token: (required)
        :param bool delivery_cdek:
        :param bool waybill:
        :param bool stock:
        :param bool user_stock:
        :return: PurchaseBaseDb
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['purchase_id', 'token', 'delivery_cdek', 'waybill', 'stock', 'user_stock']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_purchase_by_id_api_v1_purchases_purchase_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'purchase_id' is set
        if ('purchase_id' not in params or
                params['purchase_id'] is None):
            raise ValueError("Missing the required parameter `purchase_id` when calling `get_purchase_by_id_api_v1_purchases_purchase_id_get`")  # noqa: E501
        # verify the required parameter 'token' is set
        if ('token' not in params or
                params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `get_purchase_by_id_api_v1_purchases_purchase_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'purchase_id' in params:
            path_params['purchase_id'] = params['purchase_id']  # noqa: E501

        query_params = []
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501
        if 'delivery_cdek' in params:
            query_params.append(('delivery_cdek', params['delivery_cdek']))  # noqa: E501
        if 'waybill' in params:
            query_params.append(('waybill', params['waybill']))  # noqa: E501
        if 'stock' in params:
            query_params.append(('stock', params['stock']))  # noqa: E501
        if 'user_stock' in params:
            query_params.append(('user_stock', params['user_stock']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HTTPBasic']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/purchases/{purchase_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PurchaseBaseDb',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_only_api_v1_purchases_put(self, body, **kwargs):  # noqa: E501
        """Update Only  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_only_api_v1_purchases_put(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdatePurchase body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_only_api_v1_purchases_put_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_only_api_v1_purchases_put_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def update_only_api_v1_purchases_put_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update Only  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_only_api_v1_purchases_put_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdatePurchase body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_only_api_v1_purchases_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_only_api_v1_purchases_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HTTPBasic']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/purchases', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
