# coding: utf-8

"""
    Rest DB

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class YookassaPaymentBase(object):
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
        'id': 'int',
        'purchase_id': 'int',
        'payment_id': 'str',
        'status': 'str',
        'captured_at': 'str',
        'email': 'str'
    }

    attribute_map = {
        'id': 'id',
        'purchase_id': 'purchase_id',
        'payment_id': 'payment_id',
        'status': 'status',
        'captured_at': 'captured_at',
        'email': 'email'
    }

    def __init__(self, id=None, purchase_id=None, payment_id=None, status=None, captured_at=None, email=None):  # noqa: E501
        """YookassaPaymentBase - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._purchase_id = None
        self._payment_id = None
        self._status = None
        self._captured_at = None
        self._email = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if purchase_id is not None:
            self.purchase_id = purchase_id
        if payment_id is not None:
            self.payment_id = payment_id
        if status is not None:
            self.status = status
        if captured_at is not None:
            self.captured_at = captured_at
        if email is not None:
            self.email = email

    @property
    def id(self):
        """Gets the id of this YookassaPaymentBase.  # noqa: E501


        :return: The id of this YookassaPaymentBase.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this YookassaPaymentBase.


        :param id: The id of this YookassaPaymentBase.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def purchase_id(self):
        """Gets the purchase_id of this YookassaPaymentBase.  # noqa: E501


        :return: The purchase_id of this YookassaPaymentBase.  # noqa: E501
        :rtype: int
        """
        return self._purchase_id

    @purchase_id.setter
    def purchase_id(self, purchase_id):
        """Sets the purchase_id of this YookassaPaymentBase.


        :param purchase_id: The purchase_id of this YookassaPaymentBase.  # noqa: E501
        :type: int
        """

        self._purchase_id = purchase_id

    @property
    def payment_id(self):
        """Gets the payment_id of this YookassaPaymentBase.  # noqa: E501


        :return: The payment_id of this YookassaPaymentBase.  # noqa: E501
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """Sets the payment_id of this YookassaPaymentBase.


        :param payment_id: The payment_id of this YookassaPaymentBase.  # noqa: E501
        :type: str
        """

        self._payment_id = payment_id

    @property
    def status(self):
        """Gets the status of this YookassaPaymentBase.  # noqa: E501


        :return: The status of this YookassaPaymentBase.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this YookassaPaymentBase.


        :param status: The status of this YookassaPaymentBase.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def captured_at(self):
        """Gets the captured_at of this YookassaPaymentBase.  # noqa: E501


        :return: The captured_at of this YookassaPaymentBase.  # noqa: E501
        :rtype: str
        """
        return self._captured_at

    @captured_at.setter
    def captured_at(self, captured_at):
        """Sets the captured_at of this YookassaPaymentBase.


        :param captured_at: The captured_at of this YookassaPaymentBase.  # noqa: E501
        :type: str
        """

        self._captured_at = captured_at

    @property
    def email(self):
        """Gets the email of this YookassaPaymentBase.  # noqa: E501


        :return: The email of this YookassaPaymentBase.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this YookassaPaymentBase.


        :param email: The email of this YookassaPaymentBase.  # noqa: E501
        :type: str
        """

        self._email = email

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
        if issubclass(YookassaPaymentBase, dict):
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
        if not isinstance(other, YookassaPaymentBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
