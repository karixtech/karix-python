# coding: utf-8

# flake8: noqa

"""
    karix api

    # Overview  Karix API lets you interact with the Karix platform. It allows you to query your account, set up webhooks, send messages and buy phone numbers.  # API and Clients Versioning  Karix APIs are versioned using the format vX.Y where X is the major version number and Y is minor. All minor version changes are backwards compatible but major releases are not. Please be careful when upgrading.  A new user account is pinned to the latest version at the time of first request. By default every request sent Karix is processed using that version, even if there have been subsequent breaking changes. This is done to prevent existing user applications from breaking. You can change the pinned version for your account using the account dashboard. The default API version can be overridden by specifying the header `api-version`. Note: Specifying this value will not change your pinned version for other calls.  Karix also provides HTTP API clients for all major languages. Release versions of these clients correspond to their API Version supported. Client version vX.Y.Z supports API version vX.Y. HTTP Clients are configured to use `api-version` header for that client version. When using official Karix HTTP Clients only, you dont need to concern yourself with pinned version. To upgrade your API version simply update the client.  # Common Request Structures  All Karix APIs follow a common REST format with the following resources:   - account   - message   - webhook   - number  ## Creating a resource To create a request send a `POST` request with the desired parameters in a JSON object to `/<resource>/` url. A successful response will contain the details of the single resource created with HTTP status code `201 Created`. Note: An exception to this is the `Create Message` API which is a bulk API and returns       a list of message records.  ## Fetching a resource To fetch a resource by its Unique ID send a `GET` request to `/<resource>/<uid>/` where `uid` is the Alphanumeric Unique ID of the resource. A successful response will contain the details of the single resource fetched with HTTP status code `200 OK`  ## Editing a resource To edit certain parameters of a resource send a `PATCH` request to `/<resource>/<uid>/` where `uid` is the Alphanumeric Unique ID of the resource, with a JSON object containing only the parameters which need to be updated. Edit resource APIs generally have no required parameters. A successful response will contain all the details of the single resource after editing.  ## Deleting a resource To delete a resource send a `DELETE` request to `/<resource>/<uid>/` where `uid` is the Alphanumeric Unique ID of the resource. A successful response will return HTTP status code `204 No Content` with no body.  ## Fetching a list of resources To fetch a list of resources send a `GET` request to `/<resource>/` with filters as GET parameters. A successful response will contain a list of filtered paginated objects with HTTP status code `200 OK`.  ### Pagination Pagination for list APIs are controlled using GET parameters:   - `limit`: Number of objects to be returned   - `offset`: Number of objects to skip before collecting the output list.  # Common Response Structures  All Karix APIs follow some common respose structures.  ## Success Responses  ### Single Resource Response  Responses returning a single object will have the following keys | Key           | Child Key     | Description                               | |:------------- |:------------- |:----------------------------------------- | | meta          |               | Meta Details about request and response   | |               | request_uuid  | Unique request identifier                 | | data          |               | Details of the object                     |  ### List Resource Response  Responses returning a list of objects will have the following keys | Key           | Child Key     | Description                               | |:------------- |:------------- |:----------------------------------------- | | meta          |               | Meta Details about request and response   | |               | request_uuid  | Unique request identifier                 | |               | previous      | Link to the previous page of the list     | |               | next          | Link to the next page of the list         | |               | count         | Total number of objects over all pages    | |               | limit         | Limit the API was requested with          | |               | offset        | Page Offset the API was requested with    | | objects       |               | List of objects with details              |  ## Error Responses  ### Validation Error Response  Responses for requests which failed due to validation errors will have the follwing keys: | Key           | Child Key     | Description                                | |:------------- |:------------- |:------------------------------------------ | | meta          |               | Meta Details about request and response    | |               | request_uuid  | Unique request identifier                  | | error         |               | Details for the error                      | |               | message       | Error message                              | |               | param         | (Optional) parameter this error relates to |  Validation error responses will return HTTP Status Code `400 Bad Request`  ### Insufficient Balance Response  Some requests will require to consume account credits. In case of insufficient balance the following keys will be returned: | Key           | Child Key     | Description                               | |:------------- |:------------- |:----------------------------------------- | | meta          |               | Meta Details about request and response   | |               | request_uuid  | Unique request identifier                 | | error         |               | Details for the error                     | |               | message       | `Insufficient Balance`                    |  Insufficient balance response will return HTTP Status Code `402 Payment Required`   # noqa: E501

    OpenAPI spec version: 1.0
    Contact: apiteam@karix.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from karix.api.accounts_api import AccountsApi
from karix.api.message_api import MessageApi
from karix.api.number_api import NumberApi
from karix.api.number_search_api import NumberSearchApi
from karix.api.webhook_api import WebhookApi

# import ApiClient
from karix.api_client import ApiClient
from karix.configuration import Configuration
# import models into sdk package
from karix.models.create_account import CreateAccount
from karix.models.create_message import CreateMessage
from karix.models.create_webhook import CreateWebhook
from karix.models.edit_account import EditAccount
from karix.models.edit_account_number import EditAccountNumber
from karix.models.edit_webhook import EditWebhook
from karix.models.inline_response_200 import InlineResponse200
from karix.models.inline_response_200_1 import InlineResponse2001
from karix.models.inline_response_200_2 import InlineResponse2002
from karix.models.inline_response_200_3 import InlineResponse2003
from karix.models.inline_response_200_4 import InlineResponse2004
from karix.models.inline_response_200_5 import InlineResponse2005
from karix.models.inline_response_200_6 import InlineResponse2006
from karix.models.inline_response_201 import InlineResponse201
from karix.models.inline_response_201_1 import InlineResponse2011
from karix.models.inline_response_201_2 import InlineResponse2012
from karix.models.inline_response_202 import InlineResponse202
from karix.models.inline_response_402 import InlineResponse402
from karix.models.inline_response_402_error import InlineResponse402Error
from karix.models.inline_response_403 import InlineResponse403
from karix.models.inline_response_403_error import InlineResponse403Error
from karix.models.inline_response_404 import InlineResponse404
from karix.models.inline_response_404_error import InlineResponse404Error
from karix.models.inline_response_500 import InlineResponse500
from karix.models.inline_response_500_error import InlineResponse500Error
from karix.models.message import Message
from karix.models.message_error import MessageError
from karix.models.meta_response import MetaResponse
from karix.models.phone_number import PhoneNumber
from karix.models.phone_number_rate import PhoneNumberRate
from karix.models.phone_number_region import PhoneNumberRegion
from karix.models.phone_number_service import PhoneNumberService
from karix.models.rent_number import RentNumber
from karix.models.account import Account
from karix.models.account_number import AccountNumber
from karix.models.array_meta_response import ArrayMetaResponse
from karix.models.meta_response_with_balance import MetaResponseWithBalance
from karix.models.object_meta_response import ObjectMetaResponse
from karix.models.webhook import Webhook
