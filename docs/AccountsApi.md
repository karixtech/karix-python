# karix.AccountsApi

All URIs are relative to *https://api.karix.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subaccount**](AccountsApi.md#create_subaccount) | **POST** /account/ | Create a new subaccount
[**get_subaccount**](AccountsApi.md#get_subaccount) | **GET** /account/ | Get a list of accounts
[**get_subaccount_by_id**](AccountsApi.md#get_subaccount_by_id) | **GET** /account/{uid}/ | Get details of an account
[**patch_subaccount**](AccountsApi.md#patch_subaccount) | **PATCH** /account/{uid}/ | Edit an account


# **create_subaccount**
> InlineResponse201 create_subaccount(api_version=api_version, subaccount=subaccount)

Create a new subaccount

Create a new subaccount under your account

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
api_instance = karix.AccountsApi(karix.ApiClient(configuration))
api_version = '2.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 2.0)
subaccount = karix.CreateAccount() # CreateAccount | Subaccount object (optional)

try:
    # Create a new subaccount
    api_response = api_instance.create_subaccount(api_version=api_version, subaccount=subaccount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->create_subaccount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| API Version. If not specified your pinned verison is used. | [optional] [default to 2.0]
 **subaccount** | [**CreateAccount**](CreateAccount.md)| Subaccount object | [optional] 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subaccount**
> InlineResponse200 get_subaccount(api_version=api_version, offset=offset, limit=limit)

Get a list of accounts

Get a list of details of all subaccounts, including the main account. Accounts are sorted by last updated time.

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
api_instance = karix.AccountsApi(karix.ApiClient(configuration))
api_version = '2.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 2.0)
offset = 0 # int | The number of items to skip before starting to collect the result set. (optional) (default to 0)
limit = 10 # int | The numbers of items to return. (optional) (default to 10)

try:
    # Get a list of accounts
    api_response = api_instance.get_subaccount(api_version=api_version, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_subaccount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| API Version. If not specified your pinned verison is used. | [optional] [default to 2.0]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] [default to 0]
 **limit** | **int**| The numbers of items to return. | [optional] [default to 10]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subaccount_by_id**
> InlineResponse201 get_subaccount_by_id(uid, api_version=api_version)

Get details of an account

Get details of an account by its uid. Both main account and subaccounts can be fetched using their uids. 

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
api_instance = karix.AccountsApi(karix.ApiClient(configuration))
uid = 'uid_example' # str | Alphanumeric ID of the subaccount to get.
api_version = '2.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 2.0)

try:
    # Get details of an account
    api_response = api_instance.get_subaccount_by_id(uid, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_subaccount_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Alphanumeric ID of the subaccount to get. | 
 **api_version** | **str**| API Version. If not specified your pinned verison is used. | [optional] [default to 2.0]

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_subaccount**
> InlineResponse201 patch_subaccount(uid, api_version=api_version, subaccount=subaccount)

Edit an account

Edit details of your account or its subaccount   - An account can only change the status of subaccounts under it.     It cant change its own status   - A parent account can edit its own details and the details of its subaccounts 

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
api_instance = karix.AccountsApi(karix.ApiClient(configuration))
uid = 'uid_example' # str | Alphanumeric ID of the account/subaccount to edit.
api_version = '2.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 2.0)
subaccount = karix.EditAccount() # EditAccount | Subaccount object (optional)

try:
    # Edit an account
    api_response = api_instance.patch_subaccount(uid, api_version=api_version, subaccount=subaccount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->patch_subaccount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Alphanumeric ID of the account/subaccount to edit. | 
 **api_version** | **str**| API Version. If not specified your pinned verison is used. | [optional] [default to 2.0]
 **subaccount** | [**EditAccount**](EditAccount.md)| Subaccount object | [optional] 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

