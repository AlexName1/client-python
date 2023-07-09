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


class UsersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_ids_users_api_v1_users_ids_get(self, **kwargs):  # noqa: E501
        """Get All Ids Users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_ids_users_api_v1_users_ids_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_ids_users_api_v1_users_ids_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_ids_users_api_v1_users_ids_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_ids_users_api_v1_users_ids_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get All Ids Users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_ids_users_api_v1_users_ids_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_ids_users_api_v1_users_ids_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/api/v1/users/ids', 'GET',
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

    def get_all_users_api_v1_users_get(self, **kwargs):  # noqa: E501
        """Get All Users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_users_api_v1_users_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[UserBase]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_users_api_v1_users_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_users_api_v1_users_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_users_api_v1_users_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get All Users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_users_api_v1_users_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[UserBase]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_users_api_v1_users_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/api/v1/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[UserBase]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_api_v1_users_user_id_get(self, user_id, first_name, **kwargs):  # noqa: E501
        """Get User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_api_v1_users_user_id_get(user_id, first_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int user_id: (required)
        :param str first_name: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_api_v1_users_user_id_get_with_http_info(user_id, first_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_api_v1_users_user_id_get_with_http_info(user_id, first_name, **kwargs)  # noqa: E501
            return data

    def get_user_api_v1_users_user_id_get_with_http_info(self, user_id, first_name, **kwargs):  # noqa: E501
        """Get User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_api_v1_users_user_id_get_with_http_info(user_id, first_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int user_id: (required)
        :param str first_name: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'first_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_api_v1_users_user_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_api_v1_users_user_id_get`")  # noqa: E501
        # verify the required parameter 'first_name' is set
        if ('first_name' not in params or
                params['first_name'] is None):
            raise ValueError("Missing the required parameter `first_name` when calling `get_user_api_v1_users_user_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501

        query_params = []
        if 'first_name' in params:
            query_params.append(('first_name', params['first_name']))  # noqa: E501

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
            '/api/v1/users/{user_id}', 'GET',
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

    def get_user_client_api_v1_users_clients_user_id_get(self, user_id, **kwargs):  # noqa: E501
        """Get User Client  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_client_api_v1_users_clients_user_id_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int user_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_client_api_v1_users_clients_user_id_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_client_api_v1_users_clients_user_id_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def get_user_client_api_v1_users_clients_user_id_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """Get User Client  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_client_api_v1_users_clients_user_id_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int user_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_client_api_v1_users_clients_user_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_client_api_v1_users_clients_user_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501

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
            '/api/v1/users/clients/{user_id}', 'GET',
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

    def get_user_codes_api_v1_users_user_id_codes_get(self, user_id, **kwargs):  # noqa: E501
        """Get User Codes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_codes_api_v1_users_user_id_codes_get(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int user_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_codes_api_v1_users_user_id_codes_get_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_codes_api_v1_users_user_id_codes_get_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def get_user_codes_api_v1_users_user_id_codes_get_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """Get User Codes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_codes_api_v1_users_user_id_codes_get_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int user_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_codes_api_v1_users_user_id_codes_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_codes_api_v1_users_user_id_codes_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501

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
            '/api/v1/users/{user_id}/codes', 'GET',
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

    def update_last_mess_api_v1_users_user_id_mess_put(self, user_id, message_id, **kwargs):  # noqa: E501
        """Update Last Mess  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_last_mess_api_v1_users_user_id_mess_put(user_id, message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int user_id: (required)
        :param int message_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_last_mess_api_v1_users_user_id_mess_put_with_http_info(user_id, message_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_last_mess_api_v1_users_user_id_mess_put_with_http_info(user_id, message_id, **kwargs)  # noqa: E501
            return data

    def update_last_mess_api_v1_users_user_id_mess_put_with_http_info(self, user_id, message_id, **kwargs):  # noqa: E501
        """Update Last Mess  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_last_mess_api_v1_users_user_id_mess_put_with_http_info(user_id, message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int user_id: (required)
        :param int message_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'message_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_last_mess_api_v1_users_user_id_mess_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `update_last_mess_api_v1_users_user_id_mess_put`")  # noqa: E501
        # verify the required parameter 'message_id' is set
        if ('message_id' not in params or
                params['message_id'] is None):
            raise ValueError("Missing the required parameter `message_id` when calling `update_last_mess_api_v1_users_user_id_mess_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501

        query_params = []
        if 'message_id' in params:
            query_params.append(('message_id', params['message_id']))  # noqa: E501

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
            '/api/v1/users/{user_id}/mess', 'PUT',
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

    def update_user_items_api_v1_users_user_id_items_put(self, body, user_id, **kwargs):  # noqa: E501
        """Update User Items  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user_items_api_v1_users_user_id_items_put(body, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: (required)
        :param int user_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_user_items_api_v1_users_user_id_items_put_with_http_info(body, user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_user_items_api_v1_users_user_id_items_put_with_http_info(body, user_id, **kwargs)  # noqa: E501
            return data

    def update_user_items_api_v1_users_user_id_items_put_with_http_info(self, body, user_id, **kwargs):  # noqa: E501
        """Update User Items  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user_items_api_v1_users_user_id_items_put_with_http_info(body, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: (required)
        :param int user_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_user_items_api_v1_users_user_id_items_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_user_items_api_v1_users_user_id_items_put`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `update_user_items_api_v1_users_user_id_items_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501

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
            '/api/v1/users/{user_id}/items', 'PUT',
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
