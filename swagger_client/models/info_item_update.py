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

class InfoItemUpdate(object):
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
        'code': 'str',
        'photo_tg_id': 'str'
    }

    attribute_map = {
        'code': 'code',
        'photo_tg_id': 'photo_tg_id'
    }

    def __init__(self, code=None, photo_tg_id=None):  # noqa: E501
        """InfoItemUpdate - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._photo_tg_id = None
        self.discriminator = None
        self.code = code
        if photo_tg_id is not None:
            self.photo_tg_id = photo_tg_id

    @property
    def code(self):
        """Gets the code of this InfoItemUpdate.  # noqa: E501


        :return: The code of this InfoItemUpdate.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this InfoItemUpdate.


        :param code: The code of this InfoItemUpdate.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def photo_tg_id(self):
        """Gets the photo_tg_id of this InfoItemUpdate.  # noqa: E501


        :return: The photo_tg_id of this InfoItemUpdate.  # noqa: E501
        :rtype: str
        """
        return self._photo_tg_id

    @photo_tg_id.setter
    def photo_tg_id(self, photo_tg_id):
        """Sets the photo_tg_id of this InfoItemUpdate.


        :param photo_tg_id: The photo_tg_id of this InfoItemUpdate.  # noqa: E501
        :type: str
        """

        self._photo_tg_id = photo_tg_id

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
        if issubclass(InfoItemUpdate, dict):
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
        if not isinstance(other, InfoItemUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other