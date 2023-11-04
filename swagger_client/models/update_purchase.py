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

class UpdatePurchase(object):
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
        'purchase_id': 'int',
        'add_info': 'str',
        'add_photo': 'str',
        'status': 'int'
    }

    attribute_map = {
        'purchase_id': 'purchase_id',
        'add_info': 'add_info',
        'add_photo': 'add_photo',
        'status': 'status'
    }

    def __init__(self, purchase_id=None, add_info=None, add_photo=None, status=None):  # noqa: E501
        """UpdatePurchase - a model defined in Swagger"""  # noqa: E501
        self._purchase_id = None
        self._add_info = None
        self._add_photo = None
        self._status = None
        self.discriminator = None
        self.purchase_id = purchase_id
        if add_info is not None:
            self.add_info = add_info
        if add_photo is not None:
            self.add_photo = add_photo
        if status is not None:
            self.status = status

    @property
    def purchase_id(self):
        """Gets the purchase_id of this UpdatePurchase.  # noqa: E501


        :return: The purchase_id of this UpdatePurchase.  # noqa: E501
        :rtype: int
        """
        return self._purchase_id

    @purchase_id.setter
    def purchase_id(self, purchase_id):
        """Sets the purchase_id of this UpdatePurchase.


        :param purchase_id: The purchase_id of this UpdatePurchase.  # noqa: E501
        :type: int
        """
        if purchase_id is None:
            raise ValueError("Invalid value for `purchase_id`, must not be `None`")  # noqa: E501

        self._purchase_id = purchase_id

    @property
    def add_info(self):
        """Gets the add_info of this UpdatePurchase.  # noqa: E501


        :return: The add_info of this UpdatePurchase.  # noqa: E501
        :rtype: str
        """
        return self._add_info

    @add_info.setter
    def add_info(self, add_info):
        """Sets the add_info of this UpdatePurchase.


        :param add_info: The add_info of this UpdatePurchase.  # noqa: E501
        :type: str
        """

        self._add_info = add_info

    @property
    def add_photo(self):
        """Gets the add_photo of this UpdatePurchase.  # noqa: E501


        :return: The add_photo of this UpdatePurchase.  # noqa: E501
        :rtype: str
        """
        return self._add_photo

    @add_photo.setter
    def add_photo(self, add_photo):
        """Sets the add_photo of this UpdatePurchase.


        :param add_photo: The add_photo of this UpdatePurchase.  # noqa: E501
        :type: str
        """

        self._add_photo = add_photo

    @property
    def status(self):
        """Gets the status of this UpdatePurchase.  # noqa: E501


        :return: The status of this UpdatePurchase.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdatePurchase.


        :param status: The status of this UpdatePurchase.  # noqa: E501
        :type: int
        """

        self._status = status

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
        if issubclass(UpdatePurchase, dict):
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
        if not isinstance(other, UpdatePurchase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
