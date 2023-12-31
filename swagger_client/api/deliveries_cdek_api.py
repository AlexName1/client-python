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


class DeliveriesCdekApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_api_v1_deliveries_cdek_delete(self, delivery_cdek_id, **kwargs):  # noqa: E501
        """Delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_api_v1_deliveries_cdek_delete(delivery_cdek_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int delivery_cdek_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_api_v1_deliveries_cdek_delete_with_http_info(delivery_cdek_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_api_v1_deliveries_cdek_delete_with_http_info(delivery_cdek_id, **kwargs)  # noqa: E501
            return data

    def delete_api_v1_deliveries_cdek_delete_with_http_info(self, delivery_cdek_id, **kwargs):  # noqa: E501
        """Delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_api_v1_deliveries_cdek_delete_with_http_info(delivery_cdek_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int delivery_cdek_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['delivery_cdek_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_api_v1_deliveries_cdek_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'delivery_cdek_id' is set
        if ('delivery_cdek_id' not in params or
                params['delivery_cdek_id'] is None):
            raise ValueError("Missing the required parameter `delivery_cdek_id` when calling `delete_api_v1_deliveries_cdek_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'delivery_cdek_id' in params:
            query_params.append(('delivery_cdek_id', params['delivery_cdek_id']))  # noqa: E501

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
            '/api/v1/deliveries-cdek', 'DELETE',
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

    def insert_api_v1_deliveries_cdek_post(self, body, **kwargs):  # noqa: E501
        """Insert  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.insert_api_v1_deliveries_cdek_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.insert_api_v1_deliveries_cdek_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.insert_api_v1_deliveries_cdek_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def insert_api_v1_deliveries_cdek_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Insert  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.insert_api_v1_deliveries_cdek_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: (required)
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
                    " to method insert_api_v1_deliveries_cdek_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `insert_api_v1_deliveries_cdek_post`")  # noqa: E501

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
            '/api/v1/deliveries-cdek', 'POST',
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

    def update_api_v1_deliveries_cdek_put(self, body, **kwargs):  # noqa: E501
        """Update  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_api_v1_deliveries_cdek_put(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeliveryCdekUpdate body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_api_v1_deliveries_cdek_put_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_api_v1_deliveries_cdek_put_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def update_api_v1_deliveries_cdek_put_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_api_v1_deliveries_cdek_put_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeliveryCdekUpdate body: (required)
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
                    " to method update_api_v1_deliveries_cdek_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_api_v1_deliveries_cdek_put`")  # noqa: E501

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
            '/api/v1/deliveries-cdek', 'PUT',
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
