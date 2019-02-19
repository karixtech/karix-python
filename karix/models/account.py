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

from karix.models.edit_account import EditAccount  # noqa: F401,E501


class Account(object):
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
        'name': 'str',
        'status': 'str',
        'uid': 'str',
        'token': 'str',
        'is_parent': 'bool',
        'created_time': 'datetime',
        'updated_time': 'datetime',
        'account_type': 'str',
        'credit_balance': 'str',
        'auto_recharge': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'uid': 'uid',
        'token': 'token',
        'is_parent': 'is_parent',
        'created_time': 'created_time',
        'updated_time': 'updated_time',
        'account_type': 'account_type',
        'credit_balance': 'credit_balance',
        'auto_recharge': 'auto_recharge'
    }

    def __init__(self, name=None, status=None, uid=None, token=None, is_parent=None, created_time=None, updated_time=None, account_type=None, credit_balance=None, auto_recharge=None):  # noqa: E501
        """Account - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._status = None
        self._uid = None
        self._token = None
        self._is_parent = None
        self._created_time = None
        self._updated_time = None
        self._account_type = None
        self._credit_balance = None
        self._auto_recharge = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if uid is not None:
            self.uid = uid
        if token is not None:
            self.token = token
        if is_parent is not None:
            self.is_parent = is_parent
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time
        if account_type is not None:
            self.account_type = account_type
        if credit_balance is not None:
            self.credit_balance = credit_balance
        if auto_recharge is not None:
            self.auto_recharge = auto_recharge

    @property
    def name(self):
        """Gets the name of this Account.  # noqa: E501

        Name of the account. Must be unique within the parent account.   # noqa: E501

        :return: The name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Account.

        Name of the account. Must be unique within the parent account.   # noqa: E501

        :param name: The name of this Account.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 200:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `200`")  # noqa: E501

        self._name = name

    @property
    def status(self):
        """Gets the status of this Account.  # noqa: E501

        Status of your account. Possible values are:   - enabled: Account is ready to be used   - suspended: Account has been temporarily suspended   - disabled: Account has been permanently disabled and             cannot be revived. All resources allocated             to the subaccount like phonenumbers are also             deleted.   # noqa: E501

        :return: The status of this Account.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Account.

        Status of your account. Possible values are:   - enabled: Account is ready to be used   - suspended: Account has been temporarily suspended   - disabled: Account has been permanently disabled and             cannot be revived. All resources allocated             to the subaccount like phonenumbers are also             deleted.   # noqa: E501

        :param status: The status of this Account.  # noqa: E501
        :type: str
        """
        allowed_values = ["enabled", "suspended", "disabled"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def uid(self):
        """Gets the uid of this Account.  # noqa: E501

        Alphanumeric user identification. Used as username for Basic Authentication   # noqa: E501

        :return: The uid of this Account.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this Account.

        Alphanumeric user identification. Used as username for Basic Authentication   # noqa: E501

        :param uid: The uid of this Account.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def token(self):
        """Gets the token of this Account.  # noqa: E501

        Token password for this account. Used as password in Basic Authentication   # noqa: E501

        :return: The token of this Account.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this Account.

        Token password for this account. Used as password in Basic Authentication   # noqa: E501

        :param token: The token of this Account.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def is_parent(self):
        """Gets the is_parent of this Account.  # noqa: E501

        There is generally only one parent account in list. Rest are child subaccounts. Possible values:   - `true`: If the account is a parent account   - `false`: If the account is a subaccount of the parent account   # noqa: E501

        :return: The is_parent of this Account.  # noqa: E501
        :rtype: bool
        """
        return self._is_parent

    @is_parent.setter
    def is_parent(self, is_parent):
        """Sets the is_parent of this Account.

        There is generally only one parent account in list. Rest are child subaccounts. Possible values:   - `true`: If the account is a parent account   - `false`: If the account is a subaccount of the parent account   # noqa: E501

        :param is_parent: The is_parent of this Account.  # noqa: E501
        :type: bool
        """

        self._is_parent = is_parent

    @property
    def created_time(self):
        """Gets the created_time of this Account.  # noqa: E501

        Date when this account was created  # noqa: E501

        :return: The created_time of this Account.  # noqa: E501
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Account.

        Date when this account was created  # noqa: E501

        :param created_time: The created_time of this Account.  # noqa: E501
        :type: datetime
        """

        self._created_time = created_time

    @property
    def updated_time(self):
        """Gets the updated_time of this Account.  # noqa: E501

        Date when this account was last updated  # noqa: E501

        :return: The updated_time of this Account.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this Account.

        Date when this account was last updated  # noqa: E501

        :param updated_time: The updated_time of this Account.  # noqa: E501
        :type: datetime
        """

        self._updated_time = updated_time

    @property
    def account_type(self):
        """Gets the account_type of this Account.  # noqa: E501

        Signifies whether the account is prepaid, postpaid or trial   # noqa: E501

        :return: The account_type of this Account.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this Account.

        Signifies whether the account is prepaid, postpaid or trial   # noqa: E501

        :param account_type: The account_type of this Account.  # noqa: E501
        :type: str
        """
        allowed_values = ["prepaid", "postpaid", "trial"]  # noqa: E501
        if account_type not in allowed_values:
            raise ValueError(
                "Invalid value for `account_type` ({0}), must be one of {1}"  # noqa: E501
                .format(account_type, allowed_values)
            )

        self._account_type = account_type

    @property
    def credit_balance(self):
        """Gets the credit_balance of this Account.  # noqa: E501

        Account's credit balance in US dollars.   - For postpaid accounts this value will be `null`.   - For subaccounts this value will reflect balance of parent account   # noqa: E501

        :return: The credit_balance of this Account.  # noqa: E501
        :rtype: str
        """
        return self._credit_balance

    @credit_balance.setter
    def credit_balance(self, credit_balance):
        """Sets the credit_balance of this Account.

        Account's credit balance in US dollars.   - For postpaid accounts this value will be `null`.   - For subaccounts this value will reflect balance of parent account   # noqa: E501

        :param credit_balance: The credit_balance of this Account.  # noqa: E501
        :type: str
        """

        self._credit_balance = credit_balance

    @property
    def auto_recharge(self):
        """Gets the auto_recharge of this Account.  # noqa: E501

        Whether auto-recharge has been enabled.   # noqa: E501

        :return: The auto_recharge of this Account.  # noqa: E501
        :rtype: bool
        """
        return self._auto_recharge

    @auto_recharge.setter
    def auto_recharge(self, auto_recharge):
        """Sets the auto_recharge of this Account.

        Whether auto-recharge has been enabled.   # noqa: E501

        :param auto_recharge: The auto_recharge of this Account.  # noqa: E501
        :type: bool
        """

        self._auto_recharge = auto_recharge

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
        if issubclass(Account, dict):
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
        if not isinstance(other, Account):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
