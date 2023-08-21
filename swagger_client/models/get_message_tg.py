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

class GetMessageTg(object):
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
        'name': 'str',
        'video_id': 'str',
        'text': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'video_id': 'video_id',
        'text': 'text'
    }

    def __init__(self, id=None, name=None, video_id=None, text=None):  # noqa: E501
        """GetMessageTg - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._video_id = None
        self._text = None
        self.discriminator = None
        self.id = id
        self.name = name
        self.video_id = video_id
        self.text = text

    @property
    def id(self):
        """Gets the id of this GetMessageTg.  # noqa: E501


        :return: The id of this GetMessageTg.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetMessageTg.


        :param id: The id of this GetMessageTg.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetMessageTg.  # noqa: E501


        :return: The name of this GetMessageTg.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetMessageTg.


        :param name: The name of this GetMessageTg.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def video_id(self):
        """Gets the video_id of this GetMessageTg.  # noqa: E501


        :return: The video_id of this GetMessageTg.  # noqa: E501
        :rtype: str
        """
        return self._video_id

    @video_id.setter
    def video_id(self, video_id):
        """Sets the video_id of this GetMessageTg.


        :param video_id: The video_id of this GetMessageTg.  # noqa: E501
        :type: str
        """
        if video_id is None:
            raise ValueError("Invalid value for `video_id`, must not be `None`")  # noqa: E501

        self._video_id = video_id

    @property
    def text(self):
        """Gets the text of this GetMessageTg.  # noqa: E501


        :return: The text of this GetMessageTg.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this GetMessageTg.


        :param text: The text of this GetMessageTg.  # noqa: E501
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

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
        if issubclass(GetMessageTg, dict):
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
        if not isinstance(other, GetMessageTg):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
