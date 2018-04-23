# coding: utf-8

"""
    karix api

    # Overview  Karix API lets you interact with the Karix platform. It allows you to query your account, set up webhooks, send messages and buy phone numbers.  # API and Clients Versioning  Karix APIs are versioned using the format vX.Y where X is the major version number and Y is minor. All minor version changes are backwards compatible but major releases are not. Please be careful when upgrading.  A new user account is pinned to the latest version at the time of first request. By default every request sent Karix is processed using that version, even if there have been subsequent breaking changes. This is done to prevent existing user applications from breaking. You can change the pinned version for your account using the account dashboard. The default API version can be overridden by specifying the header `api-version`. Note: Specifying this value will not change your pinned version for other calls.  Karix also provides HTTP API clients for all major languages. Release versions of these clients correspond to their API Version supported. Client version vX.Y.Z supports API version vX.Y. HTTP Clients are configured to use `api-version` header for that client version. When using official Karix HTTP Clients only, you dont need to concern yourself with pinned version. To upgrade your API version simply update the client.  # Common Request Structures  All Karix APIs follow a common REST format with the following resources:   - account   - message   - webhook   - number  ## Creating a resource To create a resource send a `POST` request with the desired parameters in a JSON object to `/<resource>/` url. A successful response will contain the details of the single resource created with HTTP status code `201 Created`. Note: An exception to this is the `Create Message` API which is a bulk API and returns       a list of message records.  ## Fetching a resource To fetch a resource by its Unique ID send a `GET` request to `/<resource>/<uid>/` where `uid` is the Alphanumeric Unique ID of the resource. A successful response will contain the details of the single resource fetched with HTTP status code `200 OK`  ## Editing a resource To edit certain parameters of a resource send a `PATCH` request to `/<resource>/<uid>/` where `uid` is the Alphanumeric Unique ID of the resource, with a JSON object containing only the parameters which need to be updated. Edit resource APIs generally have no required parameters. A successful response will contain all the details of the single resource after editing.  ## Deleting a resource To delete a resource send a `DELETE` request to `/<resource>/<uid>/` where `uid` is the Alphanumeric Unique ID of the resource. A successful response will return HTTP status code `204 No Content` with no body.  ## Fetching a list of resources To fetch a list of resources send a `GET` request to `/<resource>/` with filters as GET parameters. A successful response will contain a list of filtered paginated objects with HTTP status code `200 OK`.  ### Pagination Pagination for list APIs are controlled using GET parameters:   - `limit`: Number of objects to be returned   - `offset`: Number of objects to skip before collecting the output list.  # Common Response Structures  All Karix APIs follow some common respose structures.  ## Success Responses  ### Single Resource Response  Responses returning a single object will have the following keys | Key           | Child Key     | Description                               | |:------------- |:------------- |:----------------------------------------- | | meta          |               | Meta Details about request and response   | |               | request_uuid  | Unique request identifier                 | | data          |               | Details of the object                     |  ### List Resource Response  Responses returning a list of objects will have the following keys | Key           | Child Key     | Description                               | |:------------- |:------------- |:----------------------------------------- | | meta          |               | Meta Details about request and response   | |               | request_uuid  | Unique request identifier                 | |               | previous      | Link to the previous page of the list     | |               | next          | Link to the next page of the list         | |               | count         | Total number of objects over all pages    | |               | limit         | Limit the API was requested with          | |               | offset        | Page Offset the API was requested with    | | objects       |               | List of objects with details              |  ## Error Responses  ### Validation Error Response  Responses for requests which failed due to validation errors will have the follwing keys: | Key           | Child Key     | Description                                | |:------------- |:------------- |:------------------------------------------ | | meta          |               | Meta Details about request and response    | |               | request_uuid  | Unique request identifier                  | | error         |               | Details for the error                      | |               | message       | Error message                              | |               | param         | (Optional) parameter this error relates to |  Validation error responses will return HTTP Status Code `400 Bad Request`  ### Insufficient Balance Response  Some requests will require to consume account credits. In case of insufficient balance the following keys will be returned: | Key           | Child Key     | Description                               | |:------------- |:------------- |:----------------------------------------- | | meta          |               | Meta Details about request and response   | |               | request_uuid  | Unique request identifier                 | | error         |               | Details for the error                     | |               | message       | `Insufficient Balance`                    |  Insufficient balance response will return HTTP Status Code `402 Payment Required`   # noqa: E501

    OpenAPI spec version: 1.0
    Contact: support@karix.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CreateMessage(object):
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
        'source': 'str',
        'destination': 'list[str]',
        'text': 'str',
        'notification_url': 'str',
        'notification_method': 'str'
    }

    attribute_map = {
        'source': 'source',
        'destination': 'destination',
        'text': 'text',
        'notification_url': 'notification_url',
        'notification_method': 'notification_method'
    }

    def __init__(self, source=None, destination=None, text=None, notification_url=None, notification_method=None):  # noqa: E501
        """CreateMessage - a model defined in Swagger"""  # noqa: E501

        self._source = None
        self._destination = None
        self._text = None
        self._notification_url = None
        self._notification_method = None
        self.discriminator = None

        self.source = source
        self.destination = destination
        self.text = text
        if notification_url is not None:
            self.notification_url = notification_url
        if notification_method is not None:
            self.notification_method = notification_method

    @property
    def source(self):
        """Gets the source of this CreateMessage.  # noqa: E501

        Sender ID for the message which will be displayed to the receiver. It should specification E.164 with international calling codes but without the `+` in front.   - When sending a message to US/Canada, the Sender ID must be a number     which belongs to your Karix Subaccount (or main account).   # noqa: E501

        :return: The source of this CreateMessage.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CreateMessage.

        Sender ID for the message which will be displayed to the receiver. It should specification E.164 with international calling codes but without the `+` in front.   - When sending a message to US/Canada, the Sender ID must be a number     which belongs to your Karix Subaccount (or main account).   # noqa: E501

        :param source: The source of this CreateMessage.  # noqa: E501
        :type: str
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def destination(self):
        """Gets the destination of this CreateMessage.  # noqa: E501

        The destination numbers for the message.   # noqa: E501

        :return: The destination of this CreateMessage.  # noqa: E501
        :rtype: list[str]
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this CreateMessage.

        The destination numbers for the message.   # noqa: E501

        :param destination: The destination of this CreateMessage.  # noqa: E501
        :type: list[str]
        """
        if destination is None:
            raise ValueError("Invalid value for `destination`, must not be `None`")  # noqa: E501

        self._destination = destination

    @property
    def text(self):
        """Gets the text of this CreateMessage.  # noqa: E501


        :return: The text of this CreateMessage.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this CreateMessage.


        :param text: The text of this CreateMessage.  # noqa: E501
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501
        if text is not None and len(text) < 1:
            raise ValueError("Invalid value for `text`, length must be greater than or equal to `1`")  # noqa: E501

        self._text = text

    @property
    def notification_url(self):
        """Gets the notification_url of this CreateMessage.  # noqa: E501

        URL on which message status change notifications will be sent  # noqa: E501

        :return: The notification_url of this CreateMessage.  # noqa: E501
        :rtype: str
        """
        return self._notification_url

    @notification_url.setter
    def notification_url(self, notification_url):
        """Sets the notification_url of this CreateMessage.

        URL on which message status change notifications will be sent  # noqa: E501

        :param notification_url: The notification_url of this CreateMessage.  # noqa: E501
        :type: str
        """

        self._notification_url = notification_url

    @property
    def notification_method(self):
        """Gets the notification_method of this CreateMessage.  # noqa: E501

        The HTTP method which be be used to send the notification. Defaults to POST if `notification_url` is specified.   # noqa: E501

        :return: The notification_method of this CreateMessage.  # noqa: E501
        :rtype: str
        """
        return self._notification_method

    @notification_method.setter
    def notification_method(self, notification_method):
        """Sets the notification_method of this CreateMessage.

        The HTTP method which be be used to send the notification. Defaults to POST if `notification_url` is specified.   # noqa: E501

        :param notification_method: The notification_method of this CreateMessage.  # noqa: E501
        :type: str
        """
        allowed_values = ["GET", "POST"]  # noqa: E501
        if notification_method not in allowed_values:
            raise ValueError(
                "Invalid value for `notification_method` ({0}), must be one of {1}"  # noqa: E501
                .format(notification_method, allowed_values)
            )

        self._notification_method = notification_method

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
        if not isinstance(other, CreateMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
