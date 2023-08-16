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

class DeliveryCdekUpdate(object):
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
        'delivery_cdek_id': 'int',
        'status_delivery': 'str',
        'photo_tg_file_id': 'str',
        'invoice_tg_file_id': 'str'
    }

    attribute_map = {
        'delivery_cdek_id': 'delivery_cdek_id',
        'status_delivery': 'status_delivery',
        'photo_tg_file_id': 'photo_tg_file_id',
        'invoice_tg_file_id': 'invoice_tg_file_id'
    }

    def __init__(self, delivery_cdek_id=None, status_delivery=None, photo_tg_file_id=None, invoice_tg_file_id=None):  # noqa: E501
        """DeliveryCdekUpdate - a model defined in Swagger"""  # noqa: E501
        self._delivery_cdek_id = None
        self._status_delivery = None
        self._photo_tg_file_id = None
        self._invoice_tg_file_id = None
        self.discriminator = None
        self.delivery_cdek_id = delivery_cdek_id
        if status_delivery is not None:
            self.status_delivery = status_delivery
        if photo_tg_file_id is not None:
            self.photo_tg_file_id = photo_tg_file_id
        if invoice_tg_file_id is not None:
            self.invoice_tg_file_id = invoice_tg_file_id

    @property
    def delivery_cdek_id(self):
        """Gets the delivery_cdek_id of this DeliveryCdekUpdate.  # noqa: E501


        :return: The delivery_cdek_id of this DeliveryCdekUpdate.  # noqa: E501
        :rtype: int
        """
        return self._delivery_cdek_id

    @delivery_cdek_id.setter
    def delivery_cdek_id(self, delivery_cdek_id):
        """Sets the delivery_cdek_id of this DeliveryCdekUpdate.


        :param delivery_cdek_id: The delivery_cdek_id of this DeliveryCdekUpdate.  # noqa: E501
        :type: int
        """
        if delivery_cdek_id is None:
            raise ValueError("Invalid value for `delivery_cdek_id`, must not be `None`")  # noqa: E501

        self._delivery_cdek_id = delivery_cdek_id

    @property
    def status_delivery(self):
        """Gets the status_delivery of this DeliveryCdekUpdate.  # noqa: E501


        :return: The status_delivery of this DeliveryCdekUpdate.  # noqa: E501
        :rtype: str
        """
        return self._status_delivery

    @status_delivery.setter
    def status_delivery(self, status_delivery):
        """Sets the status_delivery of this DeliveryCdekUpdate.


        :param status_delivery: The status_delivery of this DeliveryCdekUpdate.  # noqa: E501
        :type: str
        """

        self._status_delivery = status_delivery

    @property
    def photo_tg_file_id(self):
        """Gets the photo_tg_file_id of this DeliveryCdekUpdate.  # noqa: E501


        :return: The photo_tg_file_id of this DeliveryCdekUpdate.  # noqa: E501
        :rtype: str
        """
        return self._photo_tg_file_id

    @photo_tg_file_id.setter
    def photo_tg_file_id(self, photo_tg_file_id):
        """Sets the photo_tg_file_id of this DeliveryCdekUpdate.


        :param photo_tg_file_id: The photo_tg_file_id of this DeliveryCdekUpdate.  # noqa: E501
        :type: str
        """

        self._photo_tg_file_id = photo_tg_file_id

    @property
    def invoice_tg_file_id(self):
        """Gets the invoice_tg_file_id of this DeliveryCdekUpdate.  # noqa: E501


        :return: The invoice_tg_file_id of this DeliveryCdekUpdate.  # noqa: E501
        :rtype: str
        """
        return self._invoice_tg_file_id

    @invoice_tg_file_id.setter
    def invoice_tg_file_id(self, invoice_tg_file_id):
        """Sets the invoice_tg_file_id of this DeliveryCdekUpdate.


        :param invoice_tg_file_id: The invoice_tg_file_id of this DeliveryCdekUpdate.  # noqa: E501
        :type: str
        """

        self._invoice_tg_file_id = invoice_tg_file_id

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
        if issubclass(DeliveryCdekUpdate, dict):
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
        if not isinstance(other, DeliveryCdekUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other