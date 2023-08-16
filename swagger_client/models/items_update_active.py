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

class ItemsUpdateActive(object):
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
        'all_items_in_db': 'list[object]',
        'active_articul': 'object'
    }

    attribute_map = {
        'all_items_in_db': 'all_items_in_db',
        'active_articul': 'active_articul'
    }

    def __init__(self, all_items_in_db=None, active_articul=None):  # noqa: E501
        """ItemsUpdateActive - a model defined in Swagger"""  # noqa: E501
        self._all_items_in_db = None
        self._active_articul = None
        self.discriminator = None
        self.all_items_in_db = all_items_in_db
        self.active_articul = active_articul

    @property
    def all_items_in_db(self):
        """Gets the all_items_in_db of this ItemsUpdateActive.  # noqa: E501


        :return: The all_items_in_db of this ItemsUpdateActive.  # noqa: E501
        :rtype: list[object]
        """
        return self._all_items_in_db

    @all_items_in_db.setter
    def all_items_in_db(self, all_items_in_db):
        """Sets the all_items_in_db of this ItemsUpdateActive.


        :param all_items_in_db: The all_items_in_db of this ItemsUpdateActive.  # noqa: E501
        :type: list[object]
        """
        if all_items_in_db is None:
            raise ValueError("Invalid value for `all_items_in_db`, must not be `None`")  # noqa: E501

        self._all_items_in_db = all_items_in_db

    @property
    def active_articul(self):
        """Gets the active_articul of this ItemsUpdateActive.  # noqa: E501


        :return: The active_articul of this ItemsUpdateActive.  # noqa: E501
        :rtype: object
        """
        return self._active_articul

    @active_articul.setter
    def active_articul(self, active_articul):
        """Sets the active_articul of this ItemsUpdateActive.


        :param active_articul: The active_articul of this ItemsUpdateActive.  # noqa: E501
        :type: object
        """
        if active_articul is None:
            raise ValueError("Invalid value for `active_articul`, must not be `None`")  # noqa: E501

        self._active_articul = active_articul

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
        if issubclass(ItemsUpdateActive, dict):
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
        if not isinstance(other, ItemsUpdateActive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other