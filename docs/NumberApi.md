# karix.NumberApi

All URIs are relative to *https://api.karix.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_number**](NumberApi.md#get_number) | **GET** /number/ | Get details of all phone numbers linked to your account.
[**number_num_delete**](NumberApi.md#number_num_delete) | **DELETE** /number/{num}/ | Unrent number from your account
[**number_num_get**](NumberApi.md#number_num_get) | **GET** /number/{num}/ | Get details of a number
[**number_num_patch**](NumberApi.md#number_num_patch) | **PATCH** /number/{num}/ | Edit phone number belonging to your account
[**rent_number**](NumberApi.md#rent_number) | **POST** /number/ | Rent a phone number


# **get_number**
> InlineResponse2004 get_number(api_version=api_version, offset=offset, limit=limit, country=country, contains=contains, number_type=number_type)

Get details of all phone numbers linked to your account.

Get details of all phone numbers linked to your account.

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
api_instance = karix.NumberApi(karix.ApiClient(configuration))
api_version = '2.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 2.0)
offset = 0 # int | The number of items to skip before starting to collect the result set. (optional) (default to 0)
limit = 10 # int | The numbers of items to return. (optional) (default to 10)
country = 'country_example' # str | Filter by country ISO (optional)
contains = 'contains_example' # str | Filter by numbers which contain this value (optional)
number_type = ['number_type_example'] # list[str] | Filter by number type: fixed, mobile, tollfree (optional)

try:
    # Get details of all phone numbers linked to your account.
    api_response = api_instance.get_number(api_version=api_version, offset=offset, limit=limit, country=country, contains=contains, number_type=number_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumberApi->get_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| API Version. If not specified your pinned verison is used. | [optional] [default to 2.0]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] [default to 0]
 **limit** | **int**| The numbers of items to return. | [optional] [default to 10]
 **country** | **str**| Filter by country ISO | [optional] 
 **contains** | **str**| Filter by numbers which contain this value | [optional] 
 **number_type** | [**list[str]**](str.md)| Filter by number type: fixed, mobile, tollfree | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **number_num_delete**
> number_num_delete(num, api_version=api_version)

Unrent number from your account

Unrent number from your account

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
api_instance = karix.NumberApi(karix.ApiClient(configuration))
num = 56 # int | Number which needs to be unrented
api_version = '2.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 2.0)

try:
    # Unrent number from your account
    api_instance.number_num_delete(num, api_version=api_version)
except ApiException as e:
    print("Exception when calling NumberApi->number_num_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num** | **int**| Number which needs to be unrented | 
 **api_version** | **str**| API Version. If not specified your pinned verison is used. | [optional] [default to 2.0]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **number_num_get**
> InlineResponse2005 number_num_get(num, api_version=api_version)

Get details of a number

Get details of a number

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
api_instance = karix.NumberApi(karix.ApiClient(configuration))
num = 56 # int | Number for which details need to be fetched
api_version = '2.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 2.0)

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
 **api_version** | **str**| API Version. If not specified your pinned verison is used. | [optional] [default to 2.0]

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **number_num_patch**
> InlineResponse2005 number_num_patch(num, api_version=api_version, number=number)

Edit phone number belonging to your account

Edit phone number belonging to your account

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
api_instance = karix.NumberApi(karix.ApiClient(configuration))
num = 56 # int | Number which needs to be edited
api_version = '2.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 2.0)
number = karix.EditAccountNumber() # EditAccountNumber | Account Number object (optional)

try:
    # Edit phone number belonging to your account
    api_response = api_instance.number_num_patch(num, api_version=api_version, number=number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumberApi->number_num_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num** | **int**| Number which needs to be edited | 
 **api_version** | **str**| API Version. If not specified your pinned verison is used. | [optional] [default to 2.0]
 **number** | [**EditAccountNumber**](EditAccountNumber.md)| Account Number object | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rent_number**
> InlineResponse2012 rent_number(number, api_version=api_version)

Rent a phone number

Rent a phone number. Refer to Number Search API to find available phone numbers 

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
api_instance = karix.NumberApi(karix.ApiClient(configuration))
number = karix.RentNumber() # RentNumber | Rent Details object
api_version = '2.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 2.0)

try:
    # Rent a phone number
    api_response = api_instance.rent_number(number, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumberApi->rent_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | [**RentNumber**](RentNumber.md)| Rent Details object | 
 **api_version** | **str**| API Version. If not specified your pinned verison is used. | [optional] [default to 2.0]

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

