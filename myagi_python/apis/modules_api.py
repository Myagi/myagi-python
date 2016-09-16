# coding: utf-8

"""
ModulesApi.py
Copyright 2015 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ModulesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def api_v1_modules_get(self, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.api_v1_modules_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str limit: 
        :param str offset: 
        :param str training_plan: 
        :param str training_plans: 
        :param str training_plan__isnull: 
        :param str training_plans__isnull: 
        :param str ordering: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'training_plan', 'training_plans', 'training_plan__isnull', 'training_plans__isnull', 'ordering']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_modules_get" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/v1/modules/'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'training_plan' in params:
            query_params['training_plan'] = params['training_plan']
        if 'training_plans' in params:
            query_params['training_plans'] = params['training_plans']
        if 'training_plan__isnull' in params:
            query_params['training_plan__isnull'] = params['training_plan__isnull']
        if 'training_plans__isnull' in params:
            query_params['training_plans__isnull'] = params['training_plans__isnull']
        if 'ordering' in params:
            query_params['ordering'] = params['ordering']

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type=object,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def api_v1_modules_post(self, name, training_plan, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.api_v1_modules_post(name, training_plan, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name:  (required)
        :param str training_plan:  (required)
        :param str pages: 
        :param str categories: 
        :param str custom_thumbnail: 
        :param str deactivated: 
        :param str description: 
        :param str pass_percentage: 
        :param str product_reference: 
        :param str training_plans: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'training_plan', 'pages', 'categories', 'custom_thumbnail', 'deactivated', 'description', 'pass_percentage', 'product_reference', 'training_plans']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_modules_post" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `api_v1_modules_post`")
        # verify the required parameter 'training_plan' is set
        if ('training_plan' not in params) or (params['training_plan'] is None):
            raise ValueError("Missing the required parameter `training_plan` when calling `api_v1_modules_post`")

        resource_path = '/api/v1/modules/'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}
        if 'pages' in params:
            form_params['pages'] = params['pages']
        if 'categories' in params:
            form_params['categories'] = params['categories']
        if 'custom_thumbnail' in params:
            form_params['custom_thumbnail'] = params['custom_thumbnail']
        if 'deactivated' in params:
            form_params['deactivated'] = params['deactivated']
        if 'name' in params:
            form_params['name'] = params['name']
        if 'description' in params:
            form_params['description'] = params['description']
        if 'pass_percentage' in params:
            form_params['pass_percentage'] = params['pass_percentage']
        if 'product_reference' in params:
            form_params['product_reference'] = params['product_reference']
        if 'training_plan' in params:
            form_params['training_plan'] = params['training_plan']
        if 'training_plans' in params:
            form_params['training_plans'] = params['training_plans']

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type=object,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def api_v1_modules_pk_get(self, pk, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.api_v1_modules_pk_get(pk, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str pk:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pk']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_modules_pk_get" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'pk' is set
        if ('pk' not in params) or (params['pk'] is None):
            raise ValueError("Missing the required parameter `pk` when calling `api_v1_modules_pk_get`")

        resource_path = '/api/v1/modules/{pk}/'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        if 'pk' in params:
            path_params['pk'] = params['pk']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type=object,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def api_v1_modules_pk_put(self, pk, name, training_plan, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.api_v1_modules_pk_put(pk, name, training_plan, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str pk:  (required)
        :param str name:  (required)
        :param str training_plan:  (required)
        :param str pages: 
        :param str categories: 
        :param str custom_thumbnail: 
        :param str deactivated: 
        :param str description: 
        :param str pass_percentage: 
        :param str product_reference: 
        :param str training_plans: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pk', 'name', 'training_plan', 'pages', 'categories', 'custom_thumbnail', 'deactivated', 'description', 'pass_percentage', 'product_reference', 'training_plans']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_modules_pk_put" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'pk' is set
        if ('pk' not in params) or (params['pk'] is None):
            raise ValueError("Missing the required parameter `pk` when calling `api_v1_modules_pk_put`")
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `api_v1_modules_pk_put`")
        # verify the required parameter 'training_plan' is set
        if ('training_plan' not in params) or (params['training_plan'] is None):
            raise ValueError("Missing the required parameter `training_plan` when calling `api_v1_modules_pk_put`")

        resource_path = '/api/v1/modules/{pk}/'.replace('{format}', 'json')
        method = 'PUT'

        path_params = {}
        if 'pk' in params:
            path_params['pk'] = params['pk']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}
        if 'pages' in params:
            form_params['pages'] = params['pages']
        if 'categories' in params:
            form_params['categories'] = params['categories']
        if 'custom_thumbnail' in params:
            form_params['custom_thumbnail'] = params['custom_thumbnail']
        if 'deactivated' in params:
            form_params['deactivated'] = params['deactivated']
        if 'name' in params:
            form_params['name'] = params['name']
        if 'description' in params:
            form_params['description'] = params['description']
        if 'pass_percentage' in params:
            form_params['pass_percentage'] = params['pass_percentage']
        if 'product_reference' in params:
            form_params['product_reference'] = params['product_reference']
        if 'training_plan' in params:
            form_params['training_plan'] = params['training_plan']
        if 'training_plans' in params:
            form_params['training_plans'] = params['training_plans']

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type=object,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def api_v1_modules_pk_delete(self, pk, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.api_v1_modules_pk_delete(pk, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str pk:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pk']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_modules_pk_delete" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'pk' is set
        if ('pk' not in params) or (params['pk'] is None):
            raise ValueError("Missing the required parameter `pk` when calling `api_v1_modules_pk_delete`")

        resource_path = '/api/v1/modules/{pk}/'.replace('{format}', 'json')
        method = 'DELETE'

        path_params = {}
        if 'pk' in params:
            path_params['pk'] = params['pk']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type=object,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def api_v1_modules_pk_patch(self, pk, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.api_v1_modules_pk_patch(pk, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str pk:  (required)
        :param str pages: 
        :param str categories: 
        :param str custom_thumbnail: 
        :param str deactivated: 
        :param str name: 
        :param str description: 
        :param str pass_percentage: 
        :param str product_reference: 
        :param str training_plan: 
        :param str training_plans: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pk', 'pages', 'categories', 'custom_thumbnail', 'deactivated', 'name', 'description', 'pass_percentage', 'product_reference', 'training_plan', 'training_plans']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_modules_pk_patch" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'pk' is set
        if ('pk' not in params) or (params['pk'] is None):
            raise ValueError("Missing the required parameter `pk` when calling `api_v1_modules_pk_patch`")

        resource_path = '/api/v1/modules/{pk}/'.replace('{format}', 'json')
        method = 'PATCH'

        path_params = {}
        if 'pk' in params:
            path_params['pk'] = params['pk']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}
        if 'pages' in params:
            form_params['pages'] = params['pages']
        if 'categories' in params:
            form_params['categories'] = params['categories']
        if 'custom_thumbnail' in params:
            form_params['custom_thumbnail'] = params['custom_thumbnail']
        if 'deactivated' in params:
            form_params['deactivated'] = params['deactivated']
        if 'name' in params:
            form_params['name'] = params['name']
        if 'description' in params:
            form_params['description'] = params['description']
        if 'pass_percentage' in params:
            form_params['pass_percentage'] = params['pass_percentage']
        if 'product_reference' in params:
            form_params['product_reference'] = params['product_reference']
        if 'training_plan' in params:
            form_params['training_plan'] = params['training_plan']
        if 'training_plans' in params:
            form_params['training_plans'] = params['training_plans']

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type=object,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
