# coding: utf-8

"""
    karix api

    # Overview  Karix API lets you interact with the Karix platform using an omnichannel messaging API. It also allows you to query your account, set up webhooks and buy phone numbers.  # API and Clients Versioning  Karix APIs are versioned using the format vX.Y where X is the major version number and Y is minor. All minor version releases are backwards compatible but major releases are not, please be careful when upgrading.  Version header `api-version` is used by Karix platform to determine the version of the API request. To use Karix API v2 you can send `api-version` as `\"2.0\"`.  If an API request does not contain `api-version` header then Karix platform uses the pinned API version of the account as the default verison. Your account defaults to the latest API version release at the time of signup. You can check the pinned API version form the [dashboard](https://cloud.karix.io/dashboard).  Karix also provides Helper Libraries for all major languages. Release versions of these libraries correspond to their API Version supported. Client version vX.Y.Z supports API version vX.Y. Helper libraries are configured to send `api-version` header based on the library version. When using official Karix helper libraries, you dont need to concern yourself with pinned version. Using helper library of latest version will give you access to latest features.  # Supported Channels  Karix omnichannel messaging API supports the following channels:   - sms   - whatsapp  ## SMS Channel To send a message to one or more destinations over SMS channel set `channel` to `sms` in the [Messaging API](#operation/sendMessage).  In trial mode, your account can only send messages to numbers within the sandbox.  ## Whatsapp Channel To send a message to a destination over WhatsApp channel set `channel` to `whatsapp` in the [Messaging API](#operation/sendMessage).  Currently WhatsApp channel can only be used from within the sandbox. Contact [support](mailto:support@karix.io) for an early access outside the sandbox.  Any messages you initiate over WhatsApp to end users must conform to a template configured in WhatsApp. These messages are called \"Notification Messages\". Currently only text messages can be sent as Notification Messages.  Any responses you receive from end users and all replies you send within 24 hours of the last received response are called \"Conversation Messages\".  When using the sandbox for testing and development purposes, we have provided for the following pre-approved templates for \"Notification Messages\":    - Your order * has been dispatched. Please expect delivery by *   - OTP requested by you on * is *   - Thank you for your payment of * * on *. Your transaction ID is *  You can replace `*` with any text of your choice.  Both Notification and Conversation messages are priced differently, please refer to the [pricing page](http://karix.io/messaging/pricing/) for more details.  # Common Request Structures  All Karix APIs follow a common REST format with the following resources:   - account   - message   - webhook   - number  ## Creating a resource To create a resource send a `POST` request with the desired parameters in a JSON object to `/<resource>/` url. A successful response will contain the details of the single resource created with HTTP status code `201 Created`. Note: An exception to this is the `Create Message` API which is a bulk API and returns       a list of message records.  ## Fetching a resource To fetch a resource by its Unique ID send a `GET` request to `/<resource>/<uid>/` where `uid` is the Alphanumeric Unique ID of the resource. A successful response will contain the details of the single resource fetched with HTTP status code `200 OK`  ## Editing a resource To edit certain parameters of a resource send a `PATCH` request to `/<resource>/<uid>/` where `uid` is the Alphanumeric Unique ID of the resource, with a JSON object containing only the parameters which need to be updated. Edit resource APIs generally have no required parameters. A successful response will contain all the details of the single resource after editing.  ## Deleting a resource To delete a resource send a `DELETE` request to `/<resource>/<uid>/` where `uid` is the Alphanumeric Unique ID of the resource. A successful response will return HTTP status code `204 No Content` with no body.  ## Fetching a list of resources To fetch a list of resources send a `GET` request to `/<resource>/` with filters as GET parameters. A successful response will contain a list of filtered paginated objects with HTTP status code `200 OK`.  ### Pagination Pagination for list APIs are controlled using GET parameters:   - `limit`: Number of objects to be returned   - `offset`: Number of objects to skip before collecting the output list.  # Common Response Structures  All Karix APIs follow a common respose structure.  ## Success Responses  ### Single Resource Response  Responses returning a single object will have the following keys | Key           | Child Key     | Description                               | |:------------- |:------------- |:----------------------------------------- | | meta          |               | Meta Details about request and response   | |               | request_uuid  | Unique request identifier                 | | data          |               | Details of the object                     |  ### List Resource Response  Responses returning a list of objects will have the following keys | Key           | Child Key     | Description                               | |:------------- |:------------- |:----------------------------------------- | | meta          |               | Meta Details about request and response   | |               | request_uuid  | Unique request identifier                 | |               | previous      | Link to the previous page of the list     | |               | next          | Link to the next page of the list         | |               | total         | Total number of objects over all pages    | | objects       |               | List of objects with details              |  ## Error Responses  ### Validation Error Response  Responses for requests which failed due to validation errors will have the follwing keys: | Key           | Child Key     | Description                                | |:------------- |:------------- |:------------------------------------------ | | meta          |               | Meta Details about request and response    | |               | request_uuid  | Unique request identifier                  | | error         |               | Details for the error                      | |               | message       | Error message                              | |               | param         | (Optional) parameter this error relates to |  Validation error responses will return HTTP Status Code `400 Bad Request`  ### Insufficient Balance Response  Some requests will require to consume account credits. In case of insufficient balance the following keys will be returned: | Key           | Child Key     | Description                               | |:------------- |:------------- |:----------------------------------------- | | meta          |               | Meta Details about request and response   | |               | request_uuid  | Unique request identifier                 | | error         |               | Details for the error                     | |               | message       | `Insufficient Balance`                    |  Insufficient balance response will return HTTP Status Code `402 Payment Required`  # Events and Webhooks  All asynchronous events generated by Karix platform follow a common structure:  | Key           | Child Key     | Description                                 | |:------------- |:------------- |:------------------------------------------- | | uid           |               | Alphanumeric unique ID of the event         | | api_version   |               | 2.0                                         | | type          |               | Type of the event.                          | | data          |               | Details of the object attached to the event |  Currently implemented event types are:   - `message`: These events are generated when a message is created or       its status is changed. When event `type` is `message` the `data`       parameter contains the Message object (check out the response.data of       [Get Message](#operation/getMessageById) API).     - For outbound messages, `message` events are sent to `events_url` parameter of       [Send Message](#operation/sendMessage) API     - For inbound messages, `message` events are sent to the webhook attached       to the phone number resource using [Edit Number](#tag/Number) API     - For inbound messages to whatsapp sandbox, `message` events are sent to       Webhook URL set on the [Dashboard](https://cloud.karix.io/dashboard/#whatsapp-demo).   # noqa: E501

    OpenAPI spec version: 2.0
    Contact: support@karix.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from karix.models.message_channel_details import MessageChannelDetails  # noqa: F401,E501
from karix.models.message_content import MessageContent  # noqa: F401,E501
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
        'total_cost': 'str',
        'refund': 'str',
        'source': 'str',
        'destination': 'str',
        'country': 'str',
        'content_type': 'str',
        'content': 'MessageContent',
        'created_time': 'datetime',
        'sent_time': 'datetime',
        'delivered_time': 'datetime',
        'updated_time': 'datetime',
        'status': 'str',
        'direction': 'str',
        'error': 'MessageError',
        'redact': 'bool',
        'channel_details': 'MessageChannelDetails'
    }

    attribute_map = {
        'uid': 'uid',
        'account_uid': 'account_uid',
        'total_cost': 'total_cost',
        'refund': 'refund',
        'source': 'source',
        'destination': 'destination',
        'country': 'country',
        'content_type': 'content_type',
        'content': 'content',
        'created_time': 'created_time',
        'sent_time': 'sent_time',
        'delivered_time': 'delivered_time',
        'updated_time': 'updated_time',
        'status': 'status',
        'direction': 'direction',
        'error': 'error',
        'redact': 'redact',
        'channel_details': 'channel_details'
    }

    def __init__(self, uid=None, account_uid=None, total_cost=None, refund=None, source=None, destination=None, country=None, content_type=None, content=None, created_time=None, sent_time=None, delivered_time=None, updated_time=None, status=None, direction=None, error=None, redact=None, channel_details=None):  # noqa: E501
        """Message - a model defined in Swagger"""  # noqa: E501

        self._uid = None
        self._account_uid = None
        self._total_cost = None
        self._refund = None
        self._source = None
        self._destination = None
        self._country = None
        self._content_type = None
        self._content = None
        self._created_time = None
        self._sent_time = None
        self._delivered_time = None
        self._updated_time = None
        self._status = None
        self._direction = None
        self._error = None
        self._redact = None
        self._channel_details = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if account_uid is not None:
            self.account_uid = account_uid
        if total_cost is not None:
            self.total_cost = total_cost
        if refund is not None:
            self.refund = refund
        if source is not None:
            self.source = source
        if destination is not None:
            self.destination = destination
        if country is not None:
            self.country = country
        if content_type is not None:
            self.content_type = content_type
        if content is not None:
            self.content = content
        if created_time is not None:
            self.created_time = created_time
        if sent_time is not None:
            self.sent_time = sent_time
        if delivered_time is not None:
            self.delivered_time = delivered_time
        if updated_time is not None:
            self.updated_time = updated_time
        if status is not None:
            self.status = status
        if direction is not None:
            self.direction = direction
        if error is not None:
            self.error = error
        if redact is not None:
            self.redact = redact
        if channel_details is not None:
            self.channel_details = channel_details

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
    def total_cost(self):
        """Gets the total_cost of this Message.  # noqa: E501

        Total cost deducted from your credits for this message - `total_cost` will reflect refunds for this message. If there was a complete   refund, the `total_cost` will be zero.   # noqa: E501

        :return: The total_cost of this Message.  # noqa: E501
        :rtype: str
        """
        return self._total_cost

    @total_cost.setter
    def total_cost(self, total_cost):
        """Sets the total_cost of this Message.

        Total cost deducted from your credits for this message - `total_cost` will reflect refunds for this message. If there was a complete   refund, the `total_cost` will be zero.   # noqa: E501

        :param total_cost: The total_cost of this Message.  # noqa: E501
        :type: str
        """

        self._total_cost = total_cost

    @property
    def refund(self):
        """Gets the refund of this Message.  # noqa: E501

        If a refund was processed for this message `refund` will be a non-null number  # noqa: E501

        :return: The refund of this Message.  # noqa: E501
        :rtype: str
        """
        return self._refund

    @refund.setter
    def refund(self, refund):
        """Sets the refund of this Message.

        If a refund was processed for this message `refund` will be a non-null number  # noqa: E501

        :param refund: The refund of this Message.  # noqa: E501
        :type: str
        """

        self._refund = refund

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
    def country(self):
        """Gets the country of this Message.  # noqa: E501

        ISO2 code of the country where the destination belongs to  # noqa: E501

        :return: The country of this Message.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Message.

        ISO2 code of the country where the destination belongs to  # noqa: E501

        :param country: The country of this Message.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def content_type(self):
        """Gets the content_type of this Message.  # noqa: E501

        Content type of the message. - Its value will correspond to the key present in the `content`.   # noqa: E501

        :return: The content_type of this Message.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this Message.

        Content type of the message. - Its value will correspond to the key present in the `content`.   # noqa: E501

        :param content_type: The content_type of this Message.  # noqa: E501
        :type: str
        """
        allowed_values = ["text", "location"]  # noqa: E501
        if content_type not in allowed_values:
            raise ValueError(
                "Invalid value for `content_type` ({0}), must be one of {1}"  # noqa: E501
                .format(content_type, allowed_values)
            )

        self._content_type = content_type

    @property
    def content(self):
        """Gets the content of this Message.  # noqa: E501


        :return: The content of this Message.  # noqa: E501
        :rtype: MessageContent
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Message.


        :param content: The content of this Message.  # noqa: E501
        :type: MessageContent
        """

        self._content = content

    @property
    def created_time(self):
        """Gets the created_time of this Message.  # noqa: E501

        Timestamp when the message was created  # noqa: E501

        :return: The created_time of this Message.  # noqa: E501
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Message.

        Timestamp when the message was created  # noqa: E501

        :param created_time: The created_time of this Message.  # noqa: E501
        :type: datetime
        """

        self._created_time = created_time

    @property
    def sent_time(self):
        """Gets the sent_time of this Message.  # noqa: E501

        Timestamp when message was sent to the selected channel  # noqa: E501

        :return: The sent_time of this Message.  # noqa: E501
        :rtype: datetime
        """
        return self._sent_time

    @sent_time.setter
    def sent_time(self, sent_time):
        """Sets the sent_time of this Message.

        Timestamp when message was sent to the selected channel  # noqa: E501

        :param sent_time: The sent_time of this Message.  # noqa: E501
        :type: datetime
        """

        self._sent_time = sent_time

    @property
    def delivered_time(self):
        """Gets the delivered_time of this Message.  # noqa: E501

        Timestamp when the message was delivered to the destination  # noqa: E501

        :return: The delivered_time of this Message.  # noqa: E501
        :rtype: datetime
        """
        return self._delivered_time

    @delivered_time.setter
    def delivered_time(self, delivered_time):
        """Sets the delivered_time of this Message.

        Timestamp when the message was delivered to the destination  # noqa: E501

        :param delivered_time: The delivered_time of this Message.  # noqa: E501
        :type: datetime
        """

        self._delivered_time = delivered_time

    @property
    def updated_time(self):
        """Gets the updated_time of this Message.  # noqa: E501

        Timestamp when the message status was last updated - If the current status is `read`, then this timestamp also represents   read time - If the current status is `undelivered` then this timestamp also represents   undelivered time   # noqa: E501

        :return: The updated_time of this Message.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this Message.

        Timestamp when the message status was last updated - If the current status is `read`, then this timestamp also represents   read time - If the current status is `undelivered` then this timestamp also represents   undelivered time   # noqa: E501

        :param updated_time: The updated_time of this Message.  # noqa: E501
        :type: datetime
        """

        self._updated_time = updated_time

    @property
    def status(self):
        """Gets the status of this Message.  # noqa: E501

        Current status of the message. Possible values: - `queued`: Message has been queued in Karix system             (for either `inbound` or `outbound` direction) - `sent`: The `outbound` message has been sent to carriers for delivery - `failed`: In case of `outbound` message, this means that Karix failed             to send the message to a carrier.             In case of `inbound` message, this means that Karix failed             to send the message to its webhook, if configured. - `delivered`: The `outbound` message was delivered to its receiver. - `read`: The outbound message was delivered and read by the the receiver.           Not supported by `sms` channel. - `undelivered`: The `outbound` message falied to be delivered to its receiver. - `rejected`: The `outbound` message was rejected by the chosen carrier.   # noqa: E501

        :return: The status of this Message.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Message.

        Current status of the message. Possible values: - `queued`: Message has been queued in Karix system             (for either `inbound` or `outbound` direction) - `sent`: The `outbound` message has been sent to carriers for delivery - `failed`: In case of `outbound` message, this means that Karix failed             to send the message to a carrier.             In case of `inbound` message, this means that Karix failed             to send the message to its webhook, if configured. - `delivered`: The `outbound` message was delivered to its receiver. - `read`: The outbound message was delivered and read by the the receiver.           Not supported by `sms` channel. - `undelivered`: The `outbound` message falied to be delivered to its receiver. - `rejected`: The `outbound` message was rejected by the chosen carrier.   # noqa: E501

        :param status: The status of this Message.  # noqa: E501
        :type: str
        """
        allowed_values = ["queued", "sent", "failed", "delivered", "read", "undelivered", "rejected"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
    def redact(self):
        """Gets the redact of this Message.  # noqa: E501

        If the message was redacted using redact message API, then `redact` will be `true`.   # noqa: E501

        :return: The redact of this Message.  # noqa: E501
        :rtype: bool
        """
        return self._redact

    @redact.setter
    def redact(self, redact):
        """Sets the redact of this Message.

        If the message was redacted using redact message API, then `redact` will be `true`.   # noqa: E501

        :param redact: The redact of this Message.  # noqa: E501
        :type: bool
        """

        self._redact = redact

    @property
    def channel_details(self):
        """Gets the channel_details of this Message.  # noqa: E501


        :return: The channel_details of this Message.  # noqa: E501
        :rtype: MessageChannelDetails
        """
        return self._channel_details

    @channel_details.setter
    def channel_details(self, channel_details):
        """Sets the channel_details of this Message.


        :param channel_details: The channel_details of this Message.  # noqa: E501
        :type: MessageChannelDetails
        """

        self._channel_details = channel_details

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
        if issubclass(Message, dict):
            for key, value in self.items():
                result[key] = value

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
