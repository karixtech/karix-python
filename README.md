# karix-python
# Overview
Karix API lets you interact with the Karix platform. It allows you to query your account, set up webhooks, send messages and buy phone numbers.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/karixtech/karix-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/karixtech/karix-python.git`)

Then import the package:
```python
import karix 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import karix
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import karix
from karix.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
karix.configuration.username = 'YOUR_USERNAME'
karix.configuration.password = 'YOUR_PASSWORD'
# create an instance of the API class
api_instance = karix.AccountsApi()
api_version = '1.0' # str | API Version. If not specified your pinned verison is used. (optional) (default to 1.0)
subaccount = karix.CreateAccount() # CreateAccount | Subaccount object (optional)

try:
    # Create a new subaccount
    api_response = api_instance.create_subaccount(api_version=api_version, subaccount=subaccount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->create_subaccount: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.karix.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**create_subaccount**](docs/AccountsApi.md#create_subaccount) | **POST** /account/ | Create a new subaccount
*AccountsApi* | [**get_subaccount**](docs/AccountsApi.md#get_subaccount) | **GET** /account/ | Get a list of accounts
*AccountsApi* | [**get_subaccount_by_id**](docs/AccountsApi.md#get_subaccount_by_id) | **GET** /account/{uid}/ | Get details of an account
*AccountsApi* | [**patch_subaccount**](docs/AccountsApi.md#patch_subaccount) | **PATCH** /account/{uid}/ | Edit an account
*MessageApi* | [**get_message**](docs/MessageApi.md#get_message) | **GET** /message/ | Get list of messages sent or received
*MessageApi* | [**get_message_by_id**](docs/MessageApi.md#get_message_by_id) | **GET** /message/{uid}/ | Get message details by id.
*MessageApi* | [**send_message**](docs/MessageApi.md#send_message) | **POST** /message/ | Send a message to a list of phone numbers
*NumberApi* | [**get_number**](docs/NumberApi.md#get_number) | **GET** /number/ | Get details of all phone numbers linked to your account.
*NumberApi* | [**number_num_delete**](docs/NumberApi.md#number_num_delete) | **DELETE** /number/{num}/ | Unrent number from your account
*NumberApi* | [**number_num_get**](docs/NumberApi.md#number_num_get) | **GET** /number/{num}/ | Get details of a number
*NumberApi* | [**number_num_patch**](docs/NumberApi.md#number_num_patch) | **PATCH** /number/{num}/ | Edit phone number belonging to your account
*NumberApi* | [**rent_number**](docs/NumberApi.md#rent_number) | **POST** /number/ | Rent a phone number
*NumberSearchApi* | [**numbersearch_get**](docs/NumberSearchApi.md#numbersearch_get) | **GET** /numbersearch/ | Query for phone numbers in our inventory.
*WebhookApi* | [**create_webhook**](docs/WebhookApi.md#create_webhook) | **POST** /webhook/ | Create webhooks to receive Message
*WebhookApi* | [**delete_webhook_by_id**](docs/WebhookApi.md#delete_webhook_by_id) | **DELETE** /webhook/{uid}/ | Delete a webhook by ID
*WebhookApi* | [**get_webhook**](docs/WebhookApi.md#get_webhook) | **GET** /webhook/ | Get a list of your webhooks
*WebhookApi* | [**get_webhook_by_id**](docs/WebhookApi.md#get_webhook_by_id) | **GET** /webhook/{uid}/ | Get a webhook by ID
*WebhookApi* | [**patch_webhook**](docs/WebhookApi.md#patch_webhook) | **PATCH** /webhook/{uid}/ | Edit a webhook


## Documentation For Models

 - [CreateAccount](docs/CreateAccount.md)
 - [CreateMessage](docs/CreateMessage.md)
 - [CreateWebhook](docs/CreateWebhook.md)
 - [EditAccount](docs/EditAccount.md)
 - [EditAccountNumber](docs/EditAccountNumber.md)
 - [EditWebhook](docs/EditWebhook.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse201](docs/InlineResponse201.md)
 - [InlineResponse2011](docs/InlineResponse2011.md)
 - [InlineResponse2012](docs/InlineResponse2012.md)
 - [InlineResponse202](docs/InlineResponse202.md)
 - [InlineResponse402](docs/InlineResponse402.md)
 - [InlineResponse402Error](docs/InlineResponse402Error.md)
 - [InlineResponse403](docs/InlineResponse403.md)
 - [InlineResponse403Error](docs/InlineResponse403Error.md)
 - [InlineResponse404](docs/InlineResponse404.md)
 - [InlineResponse404Error](docs/InlineResponse404Error.md)
 - [InlineResponse500](docs/InlineResponse500.md)
 - [InlineResponse500Error](docs/InlineResponse500Error.md)
 - [Message](docs/Message.md)
 - [MessageError](docs/MessageError.md)
 - [MetaResponse](docs/MetaResponse.md)
 - [PhoneNumber](docs/PhoneNumber.md)
 - [PhoneNumberRate](docs/PhoneNumberRate.md)
 - [PhoneNumberRegion](docs/PhoneNumberRegion.md)
 - [PhoneNumberService](docs/PhoneNumberService.md)
 - [RentNumber](docs/RentNumber.md)
 - [Account](docs/Account.md)
 - [AccountNumber](docs/AccountNumber.md)
 - [ArrayMetaResponse](docs/ArrayMetaResponse.md)
 - [MetaResponseWithBalance](docs/MetaResponseWithBalance.md)
 - [ObjectMetaResponse](docs/ObjectMetaResponse.md)
 - [Webhook](docs/Webhook.md)


## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## Author

apiteam@karix.com

