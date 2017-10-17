# cpaas.NumberApi

All URIs are relative to *https://api.mgageindia.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_number**](NumberApi.md#get_number) | **GET** /number/ | Get details of all phone numbers linked to your account.
[**number_num_delete**](NumberApi.md#number_num_delete) | **DELETE** /number/{num}/ | Unrent number from your account
[**number_num_get**](NumberApi.md#number_num_get) | **GET** /number/{num}/ | Get details of a number
[**number_num_patch**](NumberApi.md#number_num_patch) | **PATCH** /number/{num}/ | Edit phone number belonging to your account


# **get_number**
> InlineResponse2006 get_number(api_version=api_version, country=country, pattern=pattern, number_type=number_type, service=service, offset=offset, limit=limit)

Get details of all phone numbers linked to your account.

Get details of all phone numbers linked to your account.

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
api_instance = cpaas.NumberApi()
api_version = '1.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 1.0)
country = 'country_example' # str | Filter by country ISO (optional)
pattern = 'pattern_example' # str | Filter by number pattern (optional)
number_type = 'number_type_example' # str | Filter by number type; fixed, mobile, tollfree (optional)
service = ['service_example'] # list[str] | Filter by service; voice, sms (optional)
offset = 56 # int | The number of items to skip before starting to collect the result set. (optional)
limit = 56 # int | The numbers of items to return. (optional)

try: 
    # Get details of all phone numbers linked to your account.
    api_response = api_instance.get_number(api_version=api_version, country=country, pattern=pattern, number_type=number_type, service=service, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumberApi->get_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| API Version. If not specified your pinned verison is used. | [optional] [default to 1.0]
 **country** | **str**| Filter by country ISO | [optional] 
 **pattern** | **str**| Filter by number pattern | [optional] 
 **number_type** | **str**| Filter by number type; fixed, mobile, tollfree | [optional] 
 **service** | [**list[str]**](str.md)| Filter by service; voice, sms | [optional] 
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] 
 **limit** | **int**| The numbers of items to return. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **number_num_delete**
> object number_num_delete(num, api_version=api_version)

Unrent number from your account

Unrent number from your account

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
api_instance = cpaas.NumberApi()
num = 56 # int | Number which needs to be unrented
api_version = '1.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 1.0)

try: 
    # Unrent number from your account
    api_response = api_instance.number_num_delete(num, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumberApi->number_num_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num** | **int**| Number which needs to be unrented | 
 **api_version** | **str**| API Version. If not specified your pinned verison is used. | [optional] [default to 1.0]

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **number_num_get**
> InlineResponse2007 number_num_get(num, api_version=api_version)

Get details of a number

Get details of a number

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
api_instance = cpaas.NumberApi()
num = 56 # int | Number for which details need to be fetched
api_version = '1.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 1.0)

try: 
    # Get details of a number
    api_response = api_instance.number_num_get(num, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumberApi->number_num_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num** | **int**| Number for which details need to be fetched | 
 **api_version** | **str**| API Version. If not specified your pinned verison is used. | [optional] [default to 1.0]

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **number_num_patch**
> InlineResponse2007 number_num_patch(num, api_version=api_version, webhook=webhook)

Edit phone number belonging to your account

Edit phone number belonging to your account

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
api_instance = cpaas.NumberApi()
num = 56 # int | Number which needs to be edited
api_version = '1.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 1.0)
webhook = cpaas.NumberWebhook() # NumberWebhook | Webhook object (optional)

try: 
    # Edit phone number belonging to your account
    api_response = api_instance.number_num_patch(num, api_version=api_version, webhook=webhook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumberApi->number_num_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num** | **int**| Number which needs to be edited | 
 **api_version** | **str**| API Version. If not specified your pinned verison is used. | [optional] [default to 1.0]
 **webhook** | [**NumberWebhook**](NumberWebhook.md)| Webhook object | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

