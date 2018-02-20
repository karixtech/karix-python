# coding: utf-8

"""
    karix api

    # Overview  Karix API lets you interact with the Karix platform. It allows you to query your account, set up webhooks, send messages and buy phone numbers.  # API and Clients Versioning  Karix APIs are versioned using the format vX.Y where X is the major version number and Y is minor. All minor version changes are backwards compatible but major releases are not. Please be careful when upgrading.  A new user account is pinned to the latest version at the time of first request. By default every request sent Karix is processed using that version, even if there have been subsequent breaking changes. This is done to prevent existing user applications from breaking. You can change the pinned version for your account using the account dashboard. The default API version can be overridden by specifying the header `api-version`. Note: Specifying this value will not change your pinned version for other calls.  Karix also provides HTTP API clients for all major languages. Release versions of these clients correspond to their API Version supported. Client version vX.Y.Z supports API version vX.Y. HTTP Clients are configured to use `api-version` header for that client version. When using official Karix HTTP Clients only, you dont need to concern yourself with pinned version. To upgrade your API version simply update the client.  # Common Request Structures  All Karix APIs follow a common REST format with the following resources:   - account   - message   - webhook   - number  ## Creating a resource To create a request send a `POST` request with the desired parameters in a JSON object to `/<resource>/` url. A successful response will contain the details of the single resource created with HTTP status code `201 Created`. Note: An exception to this is the `Create Message` API which is a bulk API and returns       a list of message records.  ## Fetching a resource To fetch a resource by its Unique ID send a `GET` request to `/<resource>/<uid>/` where `uid` is the Alphanumeric Unique ID of the resource. A successful response will contain the details of the single resource fetched with HTTP status code `200 OK`  ## Editing a resource To edit certain parameters of a resource send a `PATCH` request to `/<resource>/<uid>/` where `uid` is the Alphanumeric Unique ID of the resource, with a JSON object containing only the parameters which need to be updated. Edit resource APIs generally have no required parameters. A successful response will contain all the details of the single resource after editing.  ## Deleting a resource To delete a resource send a `DELETE` request to `/<resource>/<uid>/` where `uid` is the Alphanumeric Unique ID of the resource. A successful response will return HTTP status code `204 No Content` with no body.  ## Fetching a list of resources To fetch a list of resources send a `GET` request to `/<resource>/` with filters as GET parameters. A successful response will contain a list of filtered paginated objects with HTTP status code `200 OK`.  ### Pagination Pagination for list APIs are controlled using GET parameters:   - `limit`: Number of objects to be returned   - `offset`: Number of objects to skip before collecting the output list.  # Common Response Structures  All Karix APIs follow some common respose structures.  ## Success Responses  ### Single Resource Response  Responses returning a single object will have the following keys | Key           | Child Key     | Description                               | |:------------- |:------------- |:----------------------------------------- | | meta          |               | Meta Details about request and response   | |               | request_uuid  | Unique request identifier                 | | data          |               | Details of the object                     |  ### List Resource Response  Responses returning a list of objects will have the following keys | Key           | Child Key     | Description                               | |:------------- |:------------- |:----------------------------------------- | | meta          |               | Meta Details about request and response   | |               | request_uuid  | Unique request identifier                 | |               | previous      | Link to the previous page of the list     | |               | next          | Link to the next page of the list         | |               | count         | Total number of objects over all pages    | |               | limit         | Limit the API was requested with          | |               | offset        | Page Offset the API was requested with    | | objects       |               | List of objects with details              |  ## Error Responses  ### Validation Error Response  Responses for requests which failed due to validation errors will have the follwing keys: | Key           | Child Key     | Description                                | |:------------- |:------------- |:------------------------------------------ | | meta          |               | Meta Details about request and response    | |               | request_uuid  | Unique request identifier                  | | error         |               | Details for the error                      | |               | message       | Error message                              | |               | param         | (Optional) parameter this error relates to |  Validation error responses will return HTTP Status Code `400 Bad Request`  ### Insufficient Balance Response  Some requests will require to consume account credits. In case of insufficient balance the following keys will be returned: | Key           | Child Key     | Description                               | |:------------- |:------------- |:----------------------------------------- | | meta          |               | Meta Details about request and response   | |               | request_uuid  | Unique request identifier                 | | error         |               | Details for the error                     | |               | message       | `Insufficient Balance`                    |  Insufficient balance response will return HTTP Status Code `402 Payment Required`   # noqa: E501

    OpenAPI spec version: 1.0
    Contact: apiteam@karix.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from karix.models.big_decimal import BigDecimal  # noqa: F401,E501
from karix.models.message_error import MessageError  # noqa: F401,E501


class Message(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'uid': 'str',
        'account_uid': 'str',
        'source': 'str',
        'destination': 'str',
        'status': 'str',
        'text': 'str',
        'queued_time': 'datetime',
        'sent_time': 'datetime',
        'updated_time': 'datetime',
        'direction': 'str',
        'error': 'MessageError',
        'rate': 'BigDecimal',
        'refund': 'BigDecimal',
        'total_cost': 'str',
        'parts': 'int',
        'message_type': 'str',
        'mobile_country_code': 'str',
        'mobile_network_code': 'str'
    }

    attribute_map = {
        'uid': 'uid',
        'account_uid': 'account_uid',
        'source': 'source',
        'destination': 'destination',
        'status': 'status',
        'text': 'text',
        'queued_time': 'queued_time',
        'sent_time': 'sent_time',
        'updated_time': 'updated_time',
        'direction': 'direction',
        'error': 'error',
        'rate': 'rate',
        'refund': 'refund',
        'total_cost': 'total_cost',
        'parts': 'parts',
        'message_type': 'message_type',
        'mobile_country_code': 'mobile_country_code',
        'mobile_network_code': 'mobile_network_code'
    }

    def __init__(self, uid=None, account_uid=None, source=None, destination=None, status=None, text=None, queued_time=None, sent_time=None, updated_time=None, direction=None, error=None, rate=None, refund=None, total_cost=None, parts=None, message_type=None, mobile_country_code=None, mobile_network_code=None):  # noqa: E501
        """Message - a model defined in Swagger"""  # noqa: E501

        self._uid = None
        self._account_uid = None
        self._source = None
        self._destination = None
        self._status = None
        self._text = None
        self._queued_time = None
        self._sent_time = None
        self._updated_time = None
        self._direction = None
        self._error = None
        self._rate = None
        self._refund = None
        self._total_cost = None
        self._parts = None
        self._message_type = None
        self._mobile_country_code = None
        self._mobile_network_code = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if account_uid is not None:
            self.account_uid = account_uid
        if source is not None:
            self.source = source
        if destination is not None:
            self.destination = destination
        if status is not None:
            self.status = status
        if text is not None:
            self.text = text
        if queued_time is not None:
            self.queued_time = queued_time
        if sent_time is not None:
            self.sent_time = sent_time
        if updated_time is not None:
            self.updated_time = updated_time
        if direction is not None:
            self.direction = direction
        if error is not None:
            self.error = error
        if rate is not None:
            self.rate = rate
        if refund is not None:
            self.refund = refund
        if total_cost is not None:
            self.total_cost = total_cost
        if parts is not None:
            self.parts = parts
        if message_type is not None:
            self.message_type = message_type
        if mobile_country_code is not None:
            self.mobile_country_code = mobile_country_code
        if mobile_network_code is not None:
            self.mobile_network_code = mobile_network_code

    @property
    def uid(self):
        """Gets the uid of this Message.  # noqa: E501

        Unique ID for a message sent or received  # noqa: E501

        :return: The uid of this Message.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this Message.

        Unique ID for a message sent or received  # noqa: E501

        :param uid: The uid of this Message.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def account_uid(self):
        """Gets the account_uid of this Message.  # noqa: E501

        Unique ID of Account which created this message  # noqa: E501

        :return: The account_uid of this Message.  # noqa: E501
        :rtype: str
        """
        return self._account_uid

    @account_uid.setter
    def account_uid(self, account_uid):
        """Sets the account_uid of this Message.

        Unique ID of Account which created this message  # noqa: E501

        :param account_uid: The account_uid of this Message.  # noqa: E501
        :type: str
        """

        self._account_uid = account_uid

    @property
    def source(self):
        """Gets the source of this Message.  # noqa: E501

        Sender ID for the message  # noqa: E501

        :return: The source of this Message.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Message.

        Sender ID for the message  # noqa: E501

        :param source: The source of this Message.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def destination(self):
        """Gets the destination of this Message.  # noqa: E501

        Destination number for the message in E.164 format  # noqa: E501

        :return: The destination of this Message.  # noqa: E501
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this Message.

        Destination number for the message in E.164 format  # noqa: E501

        :param destination: The destination of this Message.  # noqa: E501
        :type: str
        """

        self._destination = destination

    @property
    def status(self):
        """Gets the status of this Message.  # noqa: E501

        Current status of the message. Possible values: - `queued`: Message has been queued in Karix system             (for either `inbound` or `outbound` direction) - `sent`: The `outbound` message has been sent to carriers for delivery - `failed`: In case of `outbound` message, this means that Karix failed             to send the message to a carrier.             In case of `inbound` message, this means that Karix failed             to send the message to its webhook, if configured. - `delivered`: The `outbound` message was delivered to its receiver. - `undelivered`: The `outbound` message falied to be delivered to its receiver. - `rejected`: The `outbound` message was rejected by the chosen carrier.   # noqa: E501

        :return: The status of this Message.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Message.

        Current status of the message. Possible values: - `queued`: Message has been queued in Karix system             (for either `inbound` or `outbound` direction) - `sent`: The `outbound` message has been sent to carriers for delivery - `failed`: In case of `outbound` message, this means that Karix failed             to send the message to a carrier.             In case of `inbound` message, this means that Karix failed             to send the message to its webhook, if configured. - `delivered`: The `outbound` message was delivered to its receiver. - `undelivered`: The `outbound` message falied to be delivered to its receiver. - `rejected`: The `outbound` message was rejected by the chosen carrier.   # noqa: E501

        :param status: The status of this Message.  # noqa: E501
        :type: str
        """
        allowed_values = ["queued", "sent", "failed", "delivered", "undelivered", "rejected"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def text(self):
        """Gets the text of this Message.  # noqa: E501

        Text of the message to be sent. - Message can contain non-GSM and unicode characters - A GSM only message with more than 160 characters will be automatically broken   into parts each of length 153 for billing purposes - A Non-GSM (and unicode) message with more than 70 characters will be automatically   broken into parts each of length 67 for billing purposes   # noqa: E501

        :return: The text of this Message.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Message.

        Text of the message to be sent. - Message can contain non-GSM and unicode characters - A GSM only message with more than 160 characters will be automatically broken   into parts each of length 153 for billing purposes - A Non-GSM (and unicode) message with more than 70 characters will be automatically   broken into parts each of length 67 for billing purposes   # noqa: E501

        :param text: The text of this Message.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def queued_time(self):
        """Gets the queued_time of this Message.  # noqa: E501

        The timestamp when message was accepted and queued in Karix system  # noqa: E501

        :return: The queued_time of this Message.  # noqa: E501
        :rtype: datetime
        """
        return self._queued_time

    @queued_time.setter
    def queued_time(self, queued_time):
        """Sets the queued_time of this Message.

        The timestamp when message was accepted and queued in Karix system  # noqa: E501

        :param queued_time: The queued_time of this Message.  # noqa: E501
        :type: datetime
        """

        self._queued_time = queued_time

    @property
    def sent_time(self):
        """Gets the sent_time of this Message.  # noqa: E501

        The timestamp when the message was processed and sent to destination  # noqa: E501

        :return: The sent_time of this Message.  # noqa: E501
        :rtype: datetime
        """
        return self._sent_time

    @sent_time.setter
    def sent_time(self, sent_time):
        """Sets the sent_time of this Message.

        The timestamp when the message was processed and sent to destination  # noqa: E501

        :param sent_time: The sent_time of this Message.  # noqa: E501
        :type: datetime
        """

        self._sent_time = sent_time

    @property
    def updated_time(self):
        """Gets the updated_time of this Message.  # noqa: E501

        The timestamp when the status of message was last updated. - If the current status is `delivered` then this timestamp also represents   delivered time - If the current status is `undelivered` then this timestamp also represents   undelivered time   # noqa: E501

        :return: The updated_time of this Message.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this Message.

        The timestamp when the status of message was last updated. - If the current status is `delivered` then this timestamp also represents   delivered time - If the current status is `undelivered` then this timestamp also represents   undelivered time   # noqa: E501

        :param updated_time: The updated_time of this Message.  # noqa: E501
        :type: datetime
        """

        self._updated_time = updated_time

    @property
    def direction(self):
        """Gets the direction of this Message.  # noqa: E501

        Direction of the message. - inbound: Message was sent to a number owned by the karix account - outbound: Message was sent to a destination using karix account   # noqa: E501

        :return: The direction of this Message.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this Message.

        Direction of the message. - inbound: Message was sent to a number owned by the karix account - outbound: Message was sent to a destination using karix account   # noqa: E501

        :param direction: The direction of this Message.  # noqa: E501
        :type: str
        """
        allowed_values = ["inbound", "outbound"]  # noqa: E501
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def error(self):
        """Gets the error of this Message.  # noqa: E501


        :return: The error of this Message.  # noqa: E501
        :rtype: MessageError
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this Message.


        :param error: The error of this Message.  # noqa: E501
        :type: MessageError
        """

        self._error = error

    @property
    def rate(self):
        """Gets the rate of this Message.  # noqa: E501

        Cost per part of this message. Refer to [`text`](#/definitions/Message/properties/text)   # noqa: E501

        :return: The rate of this Message.  # noqa: E501
        :rtype: BigDecimal
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this Message.

        Cost per part of this message. Refer to [`text`](#/definitions/Message/properties/text)   # noqa: E501

        :param rate: The rate of this Message.  # noqa: E501
        :type: BigDecimal
        """

        self._rate = rate

    @property
    def refund(self):
        """Gets the refund of this Message.  # noqa: E501

        In case we are unable to send the message to destination after queueing we will refund the `total_cost` you were charged. `null` if there was no refund.   # noqa: E501

        :return: The refund of this Message.  # noqa: E501
        :rtype: BigDecimal
        """
        return self._refund

    @refund.setter
    def refund(self, refund):
        """Sets the refund of this Message.

        In case we are unable to send the message to destination after queueing we will refund the `total_cost` you were charged. `null` if there was no refund.   # noqa: E501

        :param refund: The refund of this Message.  # noqa: E501
        :type: BigDecimal
        """

        self._refund = refund

    @property
    def total_cost(self):
        """Gets the total_cost of this Message.  # noqa: E501

        Total cost for this message including all parts. Refer to [`text`](#/definitions/Message/properties/text)   # noqa: E501

        :return: The total_cost of this Message.  # noqa: E501
        :rtype: str
        """
        return self._total_cost

    @total_cost.setter
    def total_cost(self, total_cost):
        """Sets the total_cost of this Message.

        Total cost for this message including all parts. Refer to [`text`](#/definitions/Message/properties/text)   # noqa: E501

        :param total_cost: The total_cost of this Message.  # noqa: E501
        :type: str
        """

        self._total_cost = total_cost

    @property
    def parts(self):
        """Gets the parts of this Message.  # noqa: E501

        Number of parts to the message if the message was too long Refer to [`text`](#/definitions/Message/properties/text)   # noqa: E501

        :return: The parts of this Message.  # noqa: E501
        :rtype: int
        """
        return self._parts

    @parts.setter
    def parts(self, parts):
        """Sets the parts of this Message.

        Number of parts to the message if the message was too long Refer to [`text`](#/definitions/Message/properties/text)   # noqa: E501

        :param parts: The parts of this Message.  # noqa: E501
        :type: int
        """

        self._parts = parts

    @property
    def message_type(self):
        """Gets the message_type of this Message.  # noqa: E501


        :return: The message_type of this Message.  # noqa: E501
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this Message.


        :param message_type: The message_type of this Message.  # noqa: E501
        :type: str
        """

        self._message_type = message_type

    @property
    def mobile_country_code(self):
        """Gets the mobile_country_code of this Message.  # noqa: E501

        Mobile Country Code of the destination number. Refer to [Wikipedia: Mobile country code](https://en.wikipedia.org/wiki/Mobile_country_code)   # noqa: E501

        :return: The mobile_country_code of this Message.  # noqa: E501
        :rtype: str
        """
        return self._mobile_country_code

    @mobile_country_code.setter
    def mobile_country_code(self, mobile_country_code):
        """Sets the mobile_country_code of this Message.

        Mobile Country Code of the destination number. Refer to [Wikipedia: Mobile country code](https://en.wikipedia.org/wiki/Mobile_country_code)   # noqa: E501

        :param mobile_country_code: The mobile_country_code of this Message.  # noqa: E501
        :type: str
        """

        self._mobile_country_code = mobile_country_code

    @property
    def mobile_network_code(self):
        """Gets the mobile_network_code of this Message.  # noqa: E501

        Mobile Network Code of the destination number. Refer to [Wikipedia: Mobile country code](https://en.wikipedia.org/wiki/Mobile_country_code)   # noqa: E501

        :return: The mobile_network_code of this Message.  # noqa: E501
        :rtype: str
        """
        return self._mobile_network_code

    @mobile_network_code.setter
    def mobile_network_code(self, mobile_network_code):
        """Sets the mobile_network_code of this Message.

        Mobile Network Code of the destination number. Refer to [Wikipedia: Mobile country code](https://en.wikipedia.org/wiki/Mobile_country_code)   # noqa: E501

        :param mobile_network_code: The mobile_network_code of this Message.  # noqa: E501
        :type: str
        """

        self._mobile_network_code = mobile_network_code

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Message):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
