# karix.WebhookApi

All URIs are relative to *https://api.karix.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhookApi.md#create_webhook) | **POST** /webhook/ | Create webhooks to receive Message
[**delete_webhook_by_id**](WebhookApi.md#delete_webhook_by_id) | **DELETE** /webhook/{uid}/ | Delete a webhook by ID
[**get_webhook**](WebhookApi.md#get_webhook) | **GET** /webhook/ | Get a list of your webhooks
[**get_webhook_by_id**](WebhookApi.md#get_webhook_by_id) | **GET** /webhook/{uid}/ | Get a webhook by ID
[**patch_webhook**](WebhookApi.md#patch_webhook) | **PATCH** /webhook/{uid}/ | Edit a webhook


# **create_webhook**
> InlineResponse2011 create_webhook(api_version=api_version, webhook=webhook)

Create webhooks to receive Message

To receive messages you will need to setup a webhook. A webhook is then attached to your phone number.

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
api_instance = karix.WebhookApi(karix.ApiClient(configuration))
api_version = '1.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 1.0)
webhook = karix.CreateWebhook() # CreateWebhook | Create Webhook object (optional)

try:
    # Create webhooks to receive Message
    api_response = api_instance.create_webhook(api_version=api_version, webhook=webhook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->create_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| API Version. If not specified your pinned verison is used. | [optional] [default to 1.0]
 **webhook** | [**CreateWebhook**](CreateWebhook.md)| Create Webhook object | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook_by_id**
> delete_webhook_by_id(uid, api_version=api_version)

Delete a webhook by ID

Delete a webhook by ID

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
api_instance = karix.WebhookApi(karix.ApiClient(configuration))
uid = 'uid_example' # str | Alphanumeric ID of the webhook to be deleted.
api_version = '1.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 1.0)

try:
    # Delete a webhook by ID
    api_instance.delete_webhook_by_id(uid, api_version=api_version)
except ApiException as e:
    print("Exception when calling WebhookApi->delete_webhook_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Alphanumeric ID of the webhook to be deleted. | 
 **api_version** | **str**| API Version. If not specified your pinned verison is used. | [optional] [default to 1.0]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook**
> InlineResponse2003 get_webhook(api_version=api_version, offset=offset, limit=limit)

Get a list of your webhooks

Get a list of your webhooks

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
api_instance = karix.WebhookApi(karix.ApiClient(configuration))
api_version = '1.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 1.0)
offset = 0 # int | The number of items to skip before starting to collect the result set. (optional) (default to 0)
limit = 10 # int | The numbers of items to return. (optional) (default to 10)

try:
    # Get a list of your webhooks
    api_response = api_instance.get_webhook(api_version=api_version, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->get_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| API Version. If not specified your pinned verison is used. | [optional] [default to 1.0]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] [default to 0]
 **limit** | **int**| The numbers of items to return. | [optional] [default to 10]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_by_id**
> InlineResponse2011 get_webhook_by_id(uid, api_version=api_version)

Get a webhook by ID

Get a webhook by ID

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
api_instance = karix.WebhookApi(karix.ApiClient(configuration))
uid = 'uid_example' # str | Alphanumeric ID of the webhook to get.
api_version = '1.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 1.0)

try:
    # Get a webhook by ID
    api_response = api_instance.get_webhook_by_id(uid, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->get_webhook_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Alphanumeric ID of the webhook to get. | 
 **api_version** | **str**| API Version. If not specified your pinned verison is used. | [optional] [default to 1.0]

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_webhook**
> InlineResponse2011 patch_webhook(uid, api_version=api_version, webhook=webhook)

Edit a webhook

Edit a webhook

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
api_instance = karix.WebhookApi(karix.ApiClient(configuration))
uid = 'uid_example' # str | Alphanumeric ID of the webhook to edit.
api_version = '1.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 1.0)
webhook = karix.EditWebhook() # EditWebhook | Webhook object (optional)

try:
    # Edit a webhook
    api_response = api_instance.patch_webhook(uid, api_version=api_version, webhook=webhook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->patch_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Alphanumeric ID of the webhook to edit. | 
 **api_version** | **str**| API Version. If not specified your pinned verison is used. | [optional] [default to 1.0]
 **webhook** | [**EditWebhook**](EditWebhook.md)| Webhook object | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

