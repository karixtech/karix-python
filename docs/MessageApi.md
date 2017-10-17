# cpaas.MessageApi

All URIs are relative to *https://api.mgageindia.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_message**](MessageApi.md#get_message) | **GET** /message/ | Get list of messages sent or received
[**get_message_by_id**](MessageApi.md#get_message_by_id) | **GET** /message/{uid}/ | Get message details by id.
[**send_message**](MessageApi.md#send_message) | **POST** /message/ | Send a message to a list of phone numbers


# **get_message**
> InlineResponse2002 get_message(api_version=api_version, direction=direction, account_uid=account_uid, state=state, offset=offset, limit=limit)

Get list of messages sent or received

Get list of messages sent or received. Sorted by descending order of either `queued_time` (latest messages are first) 

### Example 
```python
from __future__ import print_function
import time
import cpaas
from cpaas.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
cpaas.configuration.username = 'YOUR_USERNAME'
cpaas.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = cpaas.MessageApi()
api_version = '1.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 1.0)
direction = 'direction_example' # str | Message direction, inbound or outbound to filter on. If not provided, the filter is not applied.  (optional)
account_uid = 'account_uid_example' # str | Filter the result list by the account which sent the message - If not provided or `null` or empty string, no filter will be placed   and all the messages by the main account and its subaccounts are returned - To get the list of messages sent by main account only, set `account_uid`   to main account's uid.  (optional)
state = 'state_example' # str | Filter the result on the basis of message state.  (optional)
offset = 56 # int | The number of items to skip before starting to collect the result set. (optional)
limit = 56 # int | The numbers of items to return. (optional)

try: 
    # Get list of messages sent or received
    api_response = api_instance.get_message(api_version=api_version, direction=direction, account_uid=account_uid, state=state, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->get_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| API Version. If not specified your pinned verison is used. | [optional] [default to 1.0]
 **direction** | **str**| Message direction, inbound or outbound to filter on. If not provided, the filter is not applied.  | [optional] 
 **account_uid** | **str**| Filter the result list by the account which sent the message - If not provided or &#x60;null&#x60; or empty string, no filter will be placed   and all the messages by the main account and its subaccounts are returned - To get the list of messages sent by main account only, set &#x60;account_uid&#x60;   to main account&#39;s uid.  | [optional] 
 **state** | **str**| Filter the result on the basis of message state.  | [optional] 
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] 
 **limit** | **int**| The numbers of items to return. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_by_id**
> InlineResponse2003 get_message_by_id(uid, api_version=api_version)

Get message details by id.

Get message details by id.

### Example 
```python
from __future__ import print_function
import time
import cpaas
from cpaas.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
cpaas.configuration.username = 'YOUR_USERNAME'
cpaas.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = cpaas.MessageApi()
uid = 'uid_example' # str | message uid
api_version = '1.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 1.0)

try: 
    # Get message details by id.
    api_response = api_instance.get_message_by_id(uid, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->get_message_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| message uid | 
 **api_version** | **str**| API Version. If not specified your pinned verison is used. | [optional] [default to 1.0]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_message**
> InlineResponse202 send_message(api_version=api_version, message=message)

Send a message to a list of phone numbers

Send a message to a list of phone numbers.   - A successful `202` response means that the message has been `queued`     by CPaaS system.   - Once queued, the messages for your account are dequeued and processed at a     rate set for your account (defaults to 5 messages per second).     Contact [sales](http://www.mgageindia.com/contact-us.html) to get your rate limit increased.   - For fair usage, there is no rate limiting for queueing messages using this     API. Dequeue rate would still be applicable as stated. 

### Example 
```python
from __future__ import print_function
import time
import cpaas
from cpaas.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
cpaas.configuration.username = 'YOUR_USERNAME'
cpaas.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = cpaas.MessageApi()
api_version = '1.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 1.0)
message = cpaas.Message() # Message | Message object (optional)

try: 
    # Send a message to a list of phone numbers
    api_response = api_instance.send_message(api_version=api_version, message=message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->send_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| API Version. If not specified your pinned verison is used. | [optional] [default to 1.0]
 **message** | [**Message**](Message.md)| Message object | [optional] 

### Return type

[**InlineResponse202**](InlineResponse202.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

