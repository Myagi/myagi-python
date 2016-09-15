# coding: utf-8

"""
CompanysettingsApi.py
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


class CompanysettingsApi(object):
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

    def api_v1_companysettings_get(self, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.api_v1_companysettings_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str limit: 
        :param str offset: 
        :param str company: 
        :param str company__isnull: 
        :param str ordering: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'company', 'company__isnull', 'ordering']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_companysettings_get" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/v1/companysettings/'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'company' in params:
            query_params['company'] = params['company']
        if 'company__isnull' in params:
            query_params['company__isnull'] = params['company__isnull']
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
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def api_v1_companysettings_post(self, company, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.api_v1_companysettings_post(company, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str company:  (required)
        :param str access_code: 
        :param str users_can_consume_any_available_content: If True, users can consume any content that is available without being able to be explicitly enrolled in it
        :param str users_must_watch_videos_in_full: If True, users much watch module videos in full, regardless of whether that is required at the module level
        :param str users_can_make_own_connections: allow individual users of this entity to connect to  channels at their own discretion
        :param str users_can_invite_others_to_join: If True, all users (not just admins and managers) may invite other users to join their company
        :param str module_feedback_modal_switch: If True, the module popup modal will show after users complete a module
        :param str freeform_address: raw address input for the related entity's physical location
        :param str geocoder_response_code: code of the response received from geocoding service
        :param str geocoded_formatted_address: the fully formatted address string as returned bythe geocoding service
        :param str geocoded_address_object: address object including street name, street numberpostal_code, locality (city), country
        :param str google_place_id: 
        :param str google_place_name: 
        :param str google_place_url: 
        :param str latitude: 
        :param str longitude: 
        :param str allow_any_user_to_join: allow any user to join the related entitywithout approval
        :param str host_whitelist: a list of email hosts that can sign up to the entity related to this setting without further approval
        :param str host_whitelist_enabled: if a whitelist of email hosts exists, allow users with authorized email addresses to join this entity
        :param str leaderboard_enabled: Whether leaderboards should be displayed. This setting only exists for the benefit ofMoss Bros...so once they are ok with leaderboards we should remove this setting.
        :param str product_search_enabled: 
        :param str video_search_enabled: 
        :param str style_customization_enabled: 
        :param str large_cover_photo: 
        :param str nav_color: 
        :param str nav_logo: 
        :param str primary_color: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company', 'access_code', 'users_can_consume_any_available_content', 'users_must_watch_videos_in_full', 'users_can_make_own_connections', 'users_can_invite_others_to_join', 'module_feedback_modal_switch', 'freeform_address', 'geocoder_response_code', 'geocoded_formatted_address', 'geocoded_address_object', 'google_place_id', 'google_place_name', 'google_place_url', 'latitude', 'longitude', 'allow_any_user_to_join', 'host_whitelist', 'host_whitelist_enabled', 'leaderboard_enabled', 'product_search_enabled', 'video_search_enabled', 'style_customization_enabled', 'large_cover_photo', 'nav_color', 'nav_logo', 'primary_color']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_companysettings_post" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'company' is set
        if ('company' not in params) or (params['company'] is None):
            raise ValueError("Missing the required parameter `company` when calling `api_v1_companysettings_post`")

        resource_path = '/api/v1/companysettings/'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}
        if 'access_code' in params:
            form_params['access_code'] = params['access_code']
        if 'users_can_consume_any_available_content' in params:
            form_params['users_can_consume_any_available_content'] = params['users_can_consume_any_available_content']
        if 'users_must_watch_videos_in_full' in params:
            form_params['users_must_watch_videos_in_full'] = params['users_must_watch_videos_in_full']
        if 'users_can_make_own_connections' in params:
            form_params['users_can_make_own_connections'] = params['users_can_make_own_connections']
        if 'users_can_invite_others_to_join' in params:
            form_params['users_can_invite_others_to_join'] = params['users_can_invite_others_to_join']
        if 'module_feedback_modal_switch' in params:
            form_params['module_feedback_modal_switch'] = params['module_feedback_modal_switch']
        if 'freeform_address' in params:
            form_params['freeform_address'] = params['freeform_address']
        if 'geocoder_response_code' in params:
            form_params['geocoder_response_code'] = params['geocoder_response_code']
        if 'geocoded_formatted_address' in params:
            form_params['geocoded_formatted_address'] = params['geocoded_formatted_address']
        if 'geocoded_address_object' in params:
            form_params['geocoded_address_object'] = params['geocoded_address_object']
        if 'google_place_id' in params:
            form_params['google_place_id'] = params['google_place_id']
        if 'google_place_name' in params:
            form_params['google_place_name'] = params['google_place_name']
        if 'google_place_url' in params:
            form_params['google_place_url'] = params['google_place_url']
        if 'latitude' in params:
            form_params['latitude'] = params['latitude']
        if 'longitude' in params:
            form_params['longitude'] = params['longitude']
        if 'allow_any_user_to_join' in params:
            form_params['allow_any_user_to_join'] = params['allow_any_user_to_join']
        if 'host_whitelist' in params:
            form_params['host_whitelist'] = params['host_whitelist']
        if 'host_whitelist_enabled' in params:
            form_params['host_whitelist_enabled'] = params['host_whitelist_enabled']
        if 'leaderboard_enabled' in params:
            form_params['leaderboard_enabled'] = params['leaderboard_enabled']
        if 'product_search_enabled' in params:
            form_params['product_search_enabled'] = params['product_search_enabled']
        if 'video_search_enabled' in params:
            form_params['video_search_enabled'] = params['video_search_enabled']
        if 'style_customization_enabled' in params:
            form_params['style_customization_enabled'] = params['style_customization_enabled']
        if 'large_cover_photo' in params:
            form_params['large_cover_photo'] = params['large_cover_photo']
        if 'nav_color' in params:
            form_params['nav_color'] = params['nav_color']
        if 'nav_logo' in params:
            form_params['nav_logo'] = params['nav_logo']
        if 'primary_color' in params:
            form_params['primary_color'] = params['primary_color']
        if 'company' in params:
            form_params['company'] = params['company']

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
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def api_v1_companysettings_pk_get(self, pk, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.api_v1_companysettings_pk_get(pk, callback=callback_function)

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
                    " to method api_v1_companysettings_pk_get" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'pk' is set
        if ('pk' not in params) or (params['pk'] is None):
            raise ValueError("Missing the required parameter `pk` when calling `api_v1_companysettings_pk_get`")

        resource_path = '/api/v1/companysettings/{pk}/'.replace('{format}', 'json')
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
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def api_v1_companysettings_pk_put(self, pk, company, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.api_v1_companysettings_pk_put(pk, company, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str pk:  (required)
        :param str company:  (required)
        :param str access_code: 
        :param str users_can_consume_any_available_content: If True, users can consume any content that is available without being able to be explicitly enrolled in it
        :param str users_must_watch_videos_in_full: If True, users much watch module videos in full, regardless of whether that is required at the module level
        :param str users_can_make_own_connections: allow individual users of this entity to connect to  channels at their own discretion
        :param str users_can_invite_others_to_join: If True, all users (not just admins and managers) may invite other users to join their company
        :param str module_feedback_modal_switch: If True, the module popup modal will show after users complete a module
        :param str freeform_address: raw address input for the related entity's physical location
        :param str geocoder_response_code: code of the response received from geocoding service
        :param str geocoded_formatted_address: the fully formatted address string as returned bythe geocoding service
        :param str geocoded_address_object: address object including street name, street numberpostal_code, locality (city), country
        :param str google_place_id: 
        :param str google_place_name: 
        :param str google_place_url: 
        :param str latitude: 
        :param str longitude: 
        :param str allow_any_user_to_join: allow any user to join the related entitywithout approval
        :param str host_whitelist: a list of email hosts that can sign up to the entity related to this setting without further approval
        :param str host_whitelist_enabled: if a whitelist of email hosts exists, allow users with authorized email addresses to join this entity
        :param str leaderboard_enabled: Whether leaderboards should be displayed. This setting only exists for the benefit ofMoss Bros...so once they are ok with leaderboards we should remove this setting.
        :param str product_search_enabled: 
        :param str video_search_enabled: 
        :param str style_customization_enabled: 
        :param str large_cover_photo: 
        :param str nav_color: 
        :param str nav_logo: 
        :param str primary_color: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pk', 'company', 'access_code', 'users_can_consume_any_available_content', 'users_must_watch_videos_in_full', 'users_can_make_own_connections', 'users_can_invite_others_to_join', 'module_feedback_modal_switch', 'freeform_address', 'geocoder_response_code', 'geocoded_formatted_address', 'geocoded_address_object', 'google_place_id', 'google_place_name', 'google_place_url', 'latitude', 'longitude', 'allow_any_user_to_join', 'host_whitelist', 'host_whitelist_enabled', 'leaderboard_enabled', 'product_search_enabled', 'video_search_enabled', 'style_customization_enabled', 'large_cover_photo', 'nav_color', 'nav_logo', 'primary_color']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_companysettings_pk_put" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'pk' is set
        if ('pk' not in params) or (params['pk'] is None):
            raise ValueError("Missing the required parameter `pk` when calling `api_v1_companysettings_pk_put`")
        # verify the required parameter 'company' is set
        if ('company' not in params) or (params['company'] is None):
            raise ValueError("Missing the required parameter `company` when calling `api_v1_companysettings_pk_put`")

        resource_path = '/api/v1/companysettings/{pk}/'.replace('{format}', 'json')
        method = 'PUT'

        path_params = {}
        if 'pk' in params:
            path_params['pk'] = params['pk']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}
        if 'access_code' in params:
            form_params['access_code'] = params['access_code']
        if 'users_can_consume_any_available_content' in params:
            form_params['users_can_consume_any_available_content'] = params['users_can_consume_any_available_content']
        if 'users_must_watch_videos_in_full' in params:
            form_params['users_must_watch_videos_in_full'] = params['users_must_watch_videos_in_full']
        if 'users_can_make_own_connections' in params:
            form_params['users_can_make_own_connections'] = params['users_can_make_own_connections']
        if 'users_can_invite_others_to_join' in params:
            form_params['users_can_invite_others_to_join'] = params['users_can_invite_others_to_join']
        if 'module_feedback_modal_switch' in params:
            form_params['module_feedback_modal_switch'] = params['module_feedback_modal_switch']
        if 'freeform_address' in params:
            form_params['freeform_address'] = params['freeform_address']
        if 'geocoder_response_code' in params:
            form_params['geocoder_response_code'] = params['geocoder_response_code']
        if 'geocoded_formatted_address' in params:
            form_params['geocoded_formatted_address'] = params['geocoded_formatted_address']
        if 'geocoded_address_object' in params:
            form_params['geocoded_address_object'] = params['geocoded_address_object']
        if 'google_place_id' in params:
            form_params['google_place_id'] = params['google_place_id']
        if 'google_place_name' in params:
            form_params['google_place_name'] = params['google_place_name']
        if 'google_place_url' in params:
            form_params['google_place_url'] = params['google_place_url']
        if 'latitude' in params:
            form_params['latitude'] = params['latitude']
        if 'longitude' in params:
            form_params['longitude'] = params['longitude']
        if 'allow_any_user_to_join' in params:
            form_params['allow_any_user_to_join'] = params['allow_any_user_to_join']
        if 'host_whitelist' in params:
            form_params['host_whitelist'] = params['host_whitelist']
        if 'host_whitelist_enabled' in params:
            form_params['host_whitelist_enabled'] = params['host_whitelist_enabled']
        if 'leaderboard_enabled' in params:
            form_params['leaderboard_enabled'] = params['leaderboard_enabled']
        if 'product_search_enabled' in params:
            form_params['product_search_enabled'] = params['product_search_enabled']
        if 'video_search_enabled' in params:
            form_params['video_search_enabled'] = params['video_search_enabled']
        if 'style_customization_enabled' in params:
            form_params['style_customization_enabled'] = params['style_customization_enabled']
        if 'large_cover_photo' in params:
            form_params['large_cover_photo'] = params['large_cover_photo']
        if 'nav_color' in params:
            form_params['nav_color'] = params['nav_color']
        if 'nav_logo' in params:
            form_params['nav_logo'] = params['nav_logo']
        if 'primary_color' in params:
            form_params['primary_color'] = params['primary_color']
        if 'company' in params:
            form_params['company'] = params['company']

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
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def api_v1_companysettings_pk_delete(self, pk, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.api_v1_companysettings_pk_delete(pk, callback=callback_function)

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
                    " to method api_v1_companysettings_pk_delete" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'pk' is set
        if ('pk' not in params) or (params['pk'] is None):
            raise ValueError("Missing the required parameter `pk` when calling `api_v1_companysettings_pk_delete`")

        resource_path = '/api/v1/companysettings/{pk}/'.replace('{format}', 'json')
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
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def api_v1_companysettings_pk_patch(self, pk, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.api_v1_companysettings_pk_patch(pk, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str pk:  (required)
        :param str access_code: 
        :param str users_can_consume_any_available_content: If True, users can consume any content that is available without being able to be explicitly enrolled in it
        :param str users_must_watch_videos_in_full: If True, users much watch module videos in full, regardless of whether that is required at the module level
        :param str users_can_make_own_connections: allow individual users of this entity to connect to  channels at their own discretion
        :param str users_can_invite_others_to_join: If True, all users (not just admins and managers) may invite other users to join their company
        :param str module_feedback_modal_switch: If True, the module popup modal will show after users complete a module
        :param str freeform_address: raw address input for the related entity's physical location
        :param str geocoder_response_code: code of the response received from geocoding service
        :param str geocoded_formatted_address: the fully formatted address string as returned bythe geocoding service
        :param str geocoded_address_object: address object including street name, street numberpostal_code, locality (city), country
        :param str google_place_id: 
        :param str google_place_name: 
        :param str google_place_url: 
        :param str latitude: 
        :param str longitude: 
        :param str allow_any_user_to_join: allow any user to join the related entitywithout approval
        :param str host_whitelist: a list of email hosts that can sign up to the entity related to this setting without further approval
        :param str host_whitelist_enabled: if a whitelist of email hosts exists, allow users with authorized email addresses to join this entity
        :param str leaderboard_enabled: Whether leaderboards should be displayed. This setting only exists for the benefit ofMoss Bros...so once they are ok with leaderboards we should remove this setting.
        :param str product_search_enabled: 
        :param str video_search_enabled: 
        :param str style_customization_enabled: 
        :param str large_cover_photo: 
        :param str nav_color: 
        :param str nav_logo: 
        :param str primary_color: 
        :param str company: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pk', 'access_code', 'users_can_consume_any_available_content', 'users_must_watch_videos_in_full', 'users_can_make_own_connections', 'users_can_invite_others_to_join', 'module_feedback_modal_switch', 'freeform_address', 'geocoder_response_code', 'geocoded_formatted_address', 'geocoded_address_object', 'google_place_id', 'google_place_name', 'google_place_url', 'latitude', 'longitude', 'allow_any_user_to_join', 'host_whitelist', 'host_whitelist_enabled', 'leaderboard_enabled', 'product_search_enabled', 'video_search_enabled', 'style_customization_enabled', 'large_cover_photo', 'nav_color', 'nav_logo', 'primary_color', 'company']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_companysettings_pk_patch" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'pk' is set
        if ('pk' not in params) or (params['pk'] is None):
            raise ValueError("Missing the required parameter `pk` when calling `api_v1_companysettings_pk_patch`")

        resource_path = '/api/v1/companysettings/{pk}/'.replace('{format}', 'json')
        method = 'PATCH'

        path_params = {}
        if 'pk' in params:
            path_params['pk'] = params['pk']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}
        if 'access_code' in params:
            form_params['access_code'] = params['access_code']
        if 'users_can_consume_any_available_content' in params:
            form_params['users_can_consume_any_available_content'] = params['users_can_consume_any_available_content']
        if 'users_must_watch_videos_in_full' in params:
            form_params['users_must_watch_videos_in_full'] = params['users_must_watch_videos_in_full']
        if 'users_can_make_own_connections' in params:
            form_params['users_can_make_own_connections'] = params['users_can_make_own_connections']
        if 'users_can_invite_others_to_join' in params:
            form_params['users_can_invite_others_to_join'] = params['users_can_invite_others_to_join']
        if 'module_feedback_modal_switch' in params:
            form_params['module_feedback_modal_switch'] = params['module_feedback_modal_switch']
        if 'freeform_address' in params:
            form_params['freeform_address'] = params['freeform_address']
        if 'geocoder_response_code' in params:
            form_params['geocoder_response_code'] = params['geocoder_response_code']
        if 'geocoded_formatted_address' in params:
            form_params['geocoded_formatted_address'] = params['geocoded_formatted_address']
        if 'geocoded_address_object' in params:
            form_params['geocoded_address_object'] = params['geocoded_address_object']
        if 'google_place_id' in params:
            form_params['google_place_id'] = params['google_place_id']
        if 'google_place_name' in params:
            form_params['google_place_name'] = params['google_place_name']
        if 'google_place_url' in params:
            form_params['google_place_url'] = params['google_place_url']
        if 'latitude' in params:
            form_params['latitude'] = params['latitude']
        if 'longitude' in params:
            form_params['longitude'] = params['longitude']
        if 'allow_any_user_to_join' in params:
            form_params['allow_any_user_to_join'] = params['allow_any_user_to_join']
        if 'host_whitelist' in params:
            form_params['host_whitelist'] = params['host_whitelist']
        if 'host_whitelist_enabled' in params:
            form_params['host_whitelist_enabled'] = params['host_whitelist_enabled']
        if 'leaderboard_enabled' in params:
            form_params['leaderboard_enabled'] = params['leaderboard_enabled']
        if 'product_search_enabled' in params:
            form_params['product_search_enabled'] = params['product_search_enabled']
        if 'video_search_enabled' in params:
            form_params['video_search_enabled'] = params['video_search_enabled']
        if 'style_customization_enabled' in params:
            form_params['style_customization_enabled'] = params['style_customization_enabled']
        if 'large_cover_photo' in params:
            form_params['large_cover_photo'] = params['large_cover_photo']
        if 'nav_color' in params:
            form_params['nav_color'] = params['nav_color']
        if 'nav_logo' in params:
            form_params['nav_logo'] = params['nav_logo']
        if 'primary_color' in params:
            form_params['primary_color'] = params['primary_color']
        if 'company' in params:
            form_params['company'] = params['company']

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
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
