# karix.NumberSearchApi

All URIs are relative to *https://api.karix.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**numbersearch_get**](NumberSearchApi.md#numbersearch_get) | **GET** /numbersearch/ | Query for phone numbers in our inventory.


# **numbersearch_get**
> InlineResponse2006 numbersearch_get(api_version=api_version, offset=offset, limit=limit, country=country, prefix=prefix, contains=contains, number_type=number_type)

Query for phone numbers in our inventory.

Query for phone numbers in our inventory

### Example
```python
from __future__ import print_function
import time
import karix
from karix.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = karix.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = karix.NumberSearchApi(karix.ApiClient(configuration))
api_version = '2.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 2.0)
offset = 0 # int | The number of items to skip before starting to collect the result set. (optional) (default to 0)
limit = 10 # int | The numbers of items to return. (optional) (default to 10)
country = 'US' # str | Filter by country ISO. Only one country can be filtered at a time. If not country is provided results for United States are returned by default.  (optional) (default to US)
prefix = 'prefix_example' # str | Filter by numbers with this prefix after country code (optional)
contains = 'contains_example' # str | Filter by numbers which contain this value (optional)
number_type = ['number_type_example'] # list[str] | Filter by number type: fixed, mobile, tollfree (optional)

try:
    # Query for phone numbers in our inventory.
    api_response = api_instance.numbersearch_get(api_version=api_version, offset=offset, limit=limit, country=country, prefix=prefix, contains=contains, number_type=number_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumberSearchApi->numbersearch_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| API Version. If not specified your pinned verison is used. | [optional] [default to 2.0]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] [default to 0]
 **limit** | **int**| The numbers of items to return. | [optional] [default to 10]
 **country** | **str**| Filter by country ISO. Only one country can be filtered at a time. If not country is provided results for United States are returned by default.  | [optional] [default to US]
 **prefix** | **str**| Filter by numbers with this prefix after country code | [optional] 
 **contains** | **str**| Filter by numbers which contain this value | [optional] 
 **number_type** | [**list[str]**](str.md)| Filter by number type: fixed, mobile, tollfree | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

