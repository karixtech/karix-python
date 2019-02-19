# coding: utf-8

"""
    karix api

    # Overview  Karix API lets you interact with the Karix platform. It allows you to query your account, set up webhooks, send messages and buy phone numbers.  # API and Clients Versioning  Karix APIs are versioned using the format vX.Y where X is the major version number and Y is minor. All minor version changes are backwards compatible but major releases are not. Please be careful when upgrading.  A new user account is pinned to the latest version at the time of first request. By default every request sent Karix is processed using that version, even if there have been subsequent breaking changes. This is done to prevent existing user applications from breaking. You can change the pinned version for your account using the account dashboard. The default API version can be overridden by specifying the header `api-version`. Note: Specifying this value will not change your pinned version for other calls.  Karix also provides HTTP API clients for all major languages. Release versions of these clients correspond to their API Version supported. Client version vX.Y.Z supports API version vX.Y. HTTP Clients are configured to use `api-version` header for that client version. When using official Karix HTTP Clients only, you dont need to concern yourself with pinned version. To upgrade your API version simply update the client.  # Common Request Structures  All Karix APIs follow a common REST format with the following resources:   - account   - message   - webhook   - number  ## Creating a resource To create a resource send a `POST` request with the desired parameters in a JSON object to `/<resource>/` url. A successful response will contain the details of the single resource created with HTTP status code `201 Created`. Note: An exception to this is the `Create Message` API which is a bulk API and returns       a list of message records.  ## Fetching a resource To fetch a resource by its Unique ID send a `GET` request to `/<resource>/<uid>/` where `uid` is the Alphanumeric Unique ID of the resource. A successful response will contain the details of the single resource fetched with HTTP status code `200 OK`  ## Editing a resource To edit certain parameters of a resource send a `PATCH` request to `/<resource>/<uid>/` where `uid` is the Alphanumeric Unique ID of the resource, with a JSON object containing only the parameters which need to be updated. Edit resource APIs generally have no required parameters. A successful response will contain all the details of the single resource after editing.  ## Deleting a resource To delete a resource send a `DELETE` request to `/<resource>/<uid>/` where `uid` is the Alphanumeric Unique ID of the resource. A successful response will return HTTP status code `204 No Content` with no body.  ## Fetching a list of resources To fetch a list of resources send a `GET` request to `/<resource>/` with filters as GET parameters. A successful response will contain a list of filtered paginated objects with HTTP status code `200 OK`.  ### Pagination Pagination for list APIs are controlled using GET parameters:   - `limit`: Number of objects to be returned   - `offset`: Number of objects to skip before collecting the output list.  # Common Response Structures  All Karix APIs follow some common respose structures.  ## Success Responses  ### Single Resource Response  Responses returning a single object will have the following keys | Key           | Child Key     | Description                               | |:------------- |:------------- |:----------------------------------------- | | meta          |               | Meta Details about request and response   | |               | request_uuid  | Unique request identifier                 | | data          |               | Details of the object                     |  ### List Resource Response  Responses returning a list of objects will have the following keys | Key           | Child Key     | Description                               | |:------------- |:------------- |:----------------------------------------- | | meta          |               | Meta Details about request and response   | |               | request_uuid  | Unique request identifier                 | |               | previous      | Link to the previous page of the list     | |               | next          | Link to the next page of the list         | |               | count         | Total number of objects over all pages    | |               | limit         | Limit the API was requested with          | |               | offset        | Page Offset the API was requested with    | | objects       |               | List of objects with details              |  ## Error Responses  ### Validation Error Response  Responses for requests which failed due to validation errors will have the follwing keys: | Key           | Child Key     | Description                                | |:------------- |:------------- |:------------------------------------------ | | meta          |               | Meta Details about request and response    | |               | request_uuid  | Unique request identifier                  | | error         |               | Details for the error                      | |               | message       | Error message                              | |               | param         | (Optional) parameter this error relates to |  Validation error responses will return HTTP Status Code `400 Bad Request`  ### Insufficient Balance Response  Some requests will require to consume account credits. In case of insufficient balance the following keys will be returned: | Key           | Child Key     | Description                               | |:------------- |:------------- |:----------------------------------------- | | meta          |               | Meta Details about request and response   | |               | request_uuid  | Unique request identifier                 | | error         |               | Details for the error                     | |               | message       | `Insufficient Balance`                    |  Insufficient balance response will return HTTP Status Code `402 Payment Required`   # noqa: E501

    OpenAPI spec version: 1.0
    Contact: support@karix.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from karix.api_client import ApiClient


class MessageApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_message(self, **kwargs):  # noqa: E501
        """Get list of messages sent or received  # noqa: E501

        Get list of messages sent or received. Sorted by descending order of `queued_time` (latest messages are first)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_message(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: API Version. If not specified your pinned verison is used.
        :param str direction: Message direction, inbound or outbound to filter on. If not provided, the filter is not applied. 
        :param str account_uid: Filter the result list by the account which sent the message - If not provided or `null` or empty string, no filter will be placed   and all the messages by the main account and its subaccounts are returned - To get the list of messages sent by main account only, set `account_uid`   to main account's uid. 
        :param str state: Filter the result on the basis of message state. 
        :param int offset: The number of items to skip before starting to collect the result set.
        :param int limit: The numbers of items to return.
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_message_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_message_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_message_with_http_info(self, **kwargs):  # noqa: E501
        """Get list of messages sent or received  # noqa: E501

        Get list of messages sent or received. Sorted by descending order of `queued_time` (latest messages are first)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_message_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: API Version. If not specified your pinned verison is used.
        :param str direction: Message direction, inbound or outbound to filter on. If not provided, the filter is not applied. 
        :param str account_uid: Filter the result list by the account which sent the message - If not provided or `null` or empty string, no filter will be placed   and all the messages by the main account and its subaccounts are returned - To get the list of messages sent by main account only, set `account_uid`   to main account's uid. 
        :param str state: Filter the result on the basis of message state. 
        :param int offset: The number of items to skip before starting to collect the result set.
        :param int limit: The numbers of items to return.
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_version', 'direction', 'account_uid', 'state', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_message" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'direction' in params:
            query_params.append(('direction', params['direction']))  # noqa: E501
        if 'account_uid' in params:
            query_params.append(('account_uid', params['account_uid']))  # noqa: E501
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/message/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_message_by_id(self, uid, **kwargs):  # noqa: E501
        """Get message details by id.  # noqa: E501

        Get message details by id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_message_by_id(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: Alphanumeric ID of the message to get. (required)
        :param str api_version: API Version. If not specified your pinned verison is used.
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_message_by_id_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_message_by_id_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def get_message_by_id_with_http_info(self, uid, **kwargs):  # noqa: E501
        """Get message details by id.  # noqa: E501

        Get message details by id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_message_by_id_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: Alphanumeric ID of the message to get. (required)
        :param str api_version: API Version. If not specified your pinned verison is used.
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_message_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_message_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uid' in params:
            path_params['uid'] = params['uid']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/message/{uid}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def send_message(self, **kwargs):  # noqa: E501
        """Send a message to a list of phone numbers  # noqa: E501

        Send a message to a list of destinations.   - A successful `202` response means that a message record has been created in Karix.     It does not mean that each message was successfully `queued`, `sent` or `delivered`.   - To know the status of the message check the parameter `status` of the message record.   - Message records might be created with a `failed` state due issues with Karix or     validation issues. Please check `error` to know the reason of the failure.     No balance is deducted and `total_cost` is always zero for such cases.   - Message records might be updated to state `undelivered`. This is due to carrier/operator     related issues. Please check `error` to know the reason of the failure.     Balance is still deducted for such cases.   - Since this is a bulk API the response structure follows the List Response format     rather than the Single Response format.   - Once queued, the messages for your account are dequeued and processed at a     rate set for your account (defaults to 5 messages per second).     Contact [sales](support@karix.io) to get your rate limit increased.   - For fair usage, there is no rate limiting for queueing messages using this     API. Dequeue rate would still be applicable as stated.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_message(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: API Version. If not specified your pinned verison is used.
        :param CreateMessage message: Create Message object
        :return: InlineResponse202
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.send_message_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.send_message_with_http_info(**kwargs)  # noqa: E501
            return data

    def send_message_with_http_info(self, **kwargs):  # noqa: E501
        """Send a message to a list of phone numbers  # noqa: E501

        Send a message to a list of destinations.   - A successful `202` response means that a message record has been created in Karix.     It does not mean that each message was successfully `queued`, `sent` or `delivered`.   - To know the status of the message check the parameter `status` of the message record.   - Message records might be created with a `failed` state due issues with Karix or     validation issues. Please check `error` to know the reason of the failure.     No balance is deducted and `total_cost` is always zero for such cases.   - Message records might be updated to state `undelivered`. This is due to carrier/operator     related issues. Please check `error` to know the reason of the failure.     Balance is still deducted for such cases.   - Since this is a bulk API the response structure follows the List Response format     rather than the Single Response format.   - Once queued, the messages for your account are dequeued and processed at a     rate set for your account (defaults to 5 messages per second).     Contact [sales](support@karix.io) to get your rate limit increased.   - For fair usage, there is no rate limiting for queueing messages using this     API. Dequeue rate would still be applicable as stated.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_message_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: API Version. If not specified your pinned verison is used.
        :param CreateMessage message: Create Message object
        :return: InlineResponse202
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_version', 'message']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_message" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'message' in params:
            body_params = params['message']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/message/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse202',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
