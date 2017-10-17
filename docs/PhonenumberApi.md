# cpaas.PhonenumberApi

All URIs are relative to *https://api.mgageindia.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**phonenumber_get**](PhonenumberApi.md#phonenumber_get) | **GET** /phonenumber/ | Query for phone numbers in our inventory.
[**phonenumber_num_post**](PhonenumberApi.md#phonenumber_num_post) | **POST** /phonenumber/{num}/ | Buy number from inventory


# **phonenumber_get**
> InlineResponse2008 phonenumber_get(api_version=api_version, country=country, pattern=pattern, number_type=number_type, service=service, offset=offset, limit=limit)

Query for phone numbers in our inventory.

Query for phone numbers in our inventory

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
api_instance = cpaas.PhonenumberApi()
api_version = '1.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 1.0)
country = 'country_example' # str | Filter by country ISO (optional)
pattern = 'pattern_example' # str | Filter by number pattern (optional)
number_type = 'number_type_example' # str | Filter by number type; fixed, mobile, tollfree (optional)
service = ['service_example'] # list[str] | Filter by service; voice, sms (optional)
offset = 56 # int | The number of items to skip before starting to collect the result set. (optional)
limit = 56 # int | The numbers of items to return. (optional)

try: 
    # Query for phone numbers in our inventory.
    api_response = api_instance.phonenumber_get(api_version=api_version, country=country, pattern=pattern, number_type=number_type, service=service, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhonenumberApi->phonenumber_get: %s\n" % e)
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

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **phonenumber_num_post**
> InlineResponse2012 phonenumber_num_post(num, api_version=api_version, webhook=webhook)

Buy number from inventory

Buy a number from inventory

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
api_instance = cpaas.PhonenumberApi()
num = 56 # int | Number which you want to buy
api_version = '1.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 1.0)
webhook = cpaas.NumberWebhook() # NumberWebhook | Webhook object (optional)

try: 
    # Buy number from inventory
    api_response = api_instance.phonenumber_num_post(num, api_version=api_version, webhook=webhook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhonenumberApi->phonenumber_num_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num** | **int**| Number which you want to buy | 
 **api_version** | **str**| API Version. If not specified your pinned verison is used. | [optional] [default to 1.0]
 **webhook** | [**NumberWebhook**](NumberWebhook.md)| Webhook object | [optional] 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

