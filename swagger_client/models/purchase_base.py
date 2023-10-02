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

class PurchaseBase(object):
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
        'created': 'datetime',
        'buyer': 'str',
        'code': 'str',
        'price': 'int',
        'delivery': 'str',
        'address': 'str',
        'phone': 'str',
        'checking': 'bool',
        'pod': 'int',
        'invoice': 'str',
        'comment': 'str',
        'status': 'int',
        'add_info': 'str',
        'user_id': 'int',
        'add_photo': 'str',
        'partner': 'bool',
        'paid': 'bool',
        'delivery_cdek_id': 'int',
        'approve_size': 'bool',
        'size_id': 'int',
        'bot_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'buyer': 'buyer',
        'code': 'code',
        'price': 'price',
        'delivery': 'delivery',
        'address': 'address',
        'phone': 'phone',
        'checking': 'checking',
        'pod': 'pod',
        'invoice': 'invoice',
        'comment': 'comment',
        'status': 'status',
        'add_info': 'add_info',
        'user_id': 'user_id',
        'add_photo': 'add_photo',
        'partner': 'partner',
        'paid': 'paid',
        'delivery_cdek_id': 'delivery_cdek_id',
        'approve_size': 'approve_size',
        'size_id': 'size_id',
        'bot_id': 'bot_id'
    }

    def __init__(self, id=None, created=None, buyer=None, code=None, price=None, delivery=None, address=None, phone=None, checking=None, pod=None, invoice=None, comment=None, status=None, add_info=None, user_id=None, add_photo=None, partner=None, paid=None, delivery_cdek_id=None, approve_size=None, size_id=None, bot_id=None):  # noqa: E501
        """PurchaseBase - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created = None
        self._buyer = None
        self._code = None
        self._price = None
        self._delivery = None
        self._address = None
        self._phone = None
        self._checking = None
        self._pod = None
        self._invoice = None
        self._comment = None
        self._status = None
        self._add_info = None
        self._user_id = None
        self._add_photo = None
        self._partner = None
        self._paid = None
        self._delivery_cdek_id = None
        self._approve_size = None
        self._size_id = None
        self._bot_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created is not None:
            self.created = created
        if buyer is not None:
            self.buyer = buyer
        if code is not None:
            self.code = code
        if price is not None:
            self.price = price
        if delivery is not None:
            self.delivery = delivery
        if address is not None:
            self.address = address
        if phone is not None:
            self.phone = phone
        if checking is not None:
            self.checking = checking
        if pod is not None:
            self.pod = pod
        if invoice is not None:
            self.invoice = invoice
        if comment is not None:
            self.comment = comment
        if status is not None:
            self.status = status
        if add_info is not None:
            self.add_info = add_info
        if user_id is not None:
            self.user_id = user_id
        if add_photo is not None:
            self.add_photo = add_photo
        if partner is not None:
            self.partner = partner
        if paid is not None:
            self.paid = paid
        if delivery_cdek_id is not None:
            self.delivery_cdek_id = delivery_cdek_id
        if approve_size is not None:
            self.approve_size = approve_size
        if size_id is not None:
            self.size_id = size_id
        if bot_id is not None:
            self.bot_id = bot_id

    @property
    def id(self):
        """Gets the id of this PurchaseBase.  # noqa: E501


        :return: The id of this PurchaseBase.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PurchaseBase.


        :param id: The id of this PurchaseBase.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def created(self):
        """Gets the created of this PurchaseBase.  # noqa: E501


        :return: The created of this PurchaseBase.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PurchaseBase.


        :param created: The created of this PurchaseBase.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def buyer(self):
        """Gets the buyer of this PurchaseBase.  # noqa: E501


        :return: The buyer of this PurchaseBase.  # noqa: E501
        :rtype: str
        """
        return self._buyer

    @buyer.setter
    def buyer(self, buyer):
        """Sets the buyer of this PurchaseBase.


        :param buyer: The buyer of this PurchaseBase.  # noqa: E501
        :type: str
        """

        self._buyer = buyer

    @property
    def code(self):
        """Gets the code of this PurchaseBase.  # noqa: E501


        :return: The code of this PurchaseBase.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this PurchaseBase.


        :param code: The code of this PurchaseBase.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def price(self):
        """Gets the price of this PurchaseBase.  # noqa: E501


        :return: The price of this PurchaseBase.  # noqa: E501
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this PurchaseBase.


        :param price: The price of this PurchaseBase.  # noqa: E501
        :type: int
        """

        self._price = price

    @property
    def delivery(self):
        """Gets the delivery of this PurchaseBase.  # noqa: E501


        :return: The delivery of this PurchaseBase.  # noqa: E501
        :rtype: str
        """
        return self._delivery

    @delivery.setter
    def delivery(self, delivery):
        """Sets the delivery of this PurchaseBase.


        :param delivery: The delivery of this PurchaseBase.  # noqa: E501
        :type: str
        """

        self._delivery = delivery

    @property
    def address(self):
        """Gets the address of this PurchaseBase.  # noqa: E501


        :return: The address of this PurchaseBase.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PurchaseBase.


        :param address: The address of this PurchaseBase.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def phone(self):
        """Gets the phone of this PurchaseBase.  # noqa: E501


        :return: The phone of this PurchaseBase.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this PurchaseBase.


        :param phone: The phone of this PurchaseBase.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def checking(self):
        """Gets the checking of this PurchaseBase.  # noqa: E501


        :return: The checking of this PurchaseBase.  # noqa: E501
        :rtype: bool
        """
        return self._checking

    @checking.setter
    def checking(self, checking):
        """Sets the checking of this PurchaseBase.


        :param checking: The checking of this PurchaseBase.  # noqa: E501
        :type: bool
        """

        self._checking = checking

    @property
    def pod(self):
        """Gets the pod of this PurchaseBase.  # noqa: E501


        :return: The pod of this PurchaseBase.  # noqa: E501
        :rtype: int
        """
        return self._pod

    @pod.setter
    def pod(self, pod):
        """Sets the pod of this PurchaseBase.


        :param pod: The pod of this PurchaseBase.  # noqa: E501
        :type: int
        """

        self._pod = pod

    @property
    def invoice(self):
        """Gets the invoice of this PurchaseBase.  # noqa: E501


        :return: The invoice of this PurchaseBase.  # noqa: E501
        :rtype: str
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        """Sets the invoice of this PurchaseBase.


        :param invoice: The invoice of this PurchaseBase.  # noqa: E501
        :type: str
        """

        self._invoice = invoice

    @property
    def comment(self):
        """Gets the comment of this PurchaseBase.  # noqa: E501


        :return: The comment of this PurchaseBase.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this PurchaseBase.


        :param comment: The comment of this PurchaseBase.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def status(self):
        """Gets the status of this PurchaseBase.  # noqa: E501


        :return: The status of this PurchaseBase.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PurchaseBase.


        :param status: The status of this PurchaseBase.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def add_info(self):
        """Gets the add_info of this PurchaseBase.  # noqa: E501


        :return: The add_info of this PurchaseBase.  # noqa: E501
        :rtype: str
        """
        return self._add_info

    @add_info.setter
    def add_info(self, add_info):
        """Sets the add_info of this PurchaseBase.


        :param add_info: The add_info of this PurchaseBase.  # noqa: E501
        :type: str
        """

        self._add_info = add_info

    @property
    def user_id(self):
        """Gets the user_id of this PurchaseBase.  # noqa: E501


        :return: The user_id of this PurchaseBase.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this PurchaseBase.


        :param user_id: The user_id of this PurchaseBase.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def add_photo(self):
        """Gets the add_photo of this PurchaseBase.  # noqa: E501


        :return: The add_photo of this PurchaseBase.  # noqa: E501
        :rtype: str
        """
        return self._add_photo

    @add_photo.setter
    def add_photo(self, add_photo):
        """Sets the add_photo of this PurchaseBase.


        :param add_photo: The add_photo of this PurchaseBase.  # noqa: E501
        :type: str
        """

        self._add_photo = add_photo

    @property
    def partner(self):
        """Gets the partner of this PurchaseBase.  # noqa: E501


        :return: The partner of this PurchaseBase.  # noqa: E501
        :rtype: bool
        """
        return self._partner

    @partner.setter
    def partner(self, partner):
        """Sets the partner of this PurchaseBase.


        :param partner: The partner of this PurchaseBase.  # noqa: E501
        :type: bool
        """

        self._partner = partner

    @property
    def paid(self):
        """Gets the paid of this PurchaseBase.  # noqa: E501


        :return: The paid of this PurchaseBase.  # noqa: E501
        :rtype: bool
        """
        return self._paid

    @paid.setter
    def paid(self, paid):
        """Sets the paid of this PurchaseBase.


        :param paid: The paid of this PurchaseBase.  # noqa: E501
        :type: bool
        """

        self._paid = paid

    @property
    def delivery_cdek_id(self):
        """Gets the delivery_cdek_id of this PurchaseBase.  # noqa: E501


        :return: The delivery_cdek_id of this PurchaseBase.  # noqa: E501
        :rtype: int
        """
        return self._delivery_cdek_id

    @delivery_cdek_id.setter
    def delivery_cdek_id(self, delivery_cdek_id):
        """Sets the delivery_cdek_id of this PurchaseBase.


        :param delivery_cdek_id: The delivery_cdek_id of this PurchaseBase.  # noqa: E501
        :type: int
        """

        self._delivery_cdek_id = delivery_cdek_id

    @property
    def approve_size(self):
        """Gets the approve_size of this PurchaseBase.  # noqa: E501


        :return: The approve_size of this PurchaseBase.  # noqa: E501
        :rtype: bool
        """
        return self._approve_size

    @approve_size.setter
    def approve_size(self, approve_size):
        """Sets the approve_size of this PurchaseBase.


        :param approve_size: The approve_size of this PurchaseBase.  # noqa: E501
        :type: bool
        """

        self._approve_size = approve_size

    @property
    def size_id(self):
        """Gets the size_id of this PurchaseBase.  # noqa: E501


        :return: The size_id of this PurchaseBase.  # noqa: E501
        :rtype: int
        """
        return self._size_id

    @size_id.setter
    def size_id(self, size_id):
        """Sets the size_id of this PurchaseBase.


        :param size_id: The size_id of this PurchaseBase.  # noqa: E501
        :type: int
        """

        self._size_id = size_id

    @property
    def bot_id(self):
        """Gets the bot_id of this PurchaseBase.  # noqa: E501


        :return: The bot_id of this PurchaseBase.  # noqa: E501
        :rtype: int
        """
        return self._bot_id

    @bot_id.setter
    def bot_id(self, bot_id):
        """Sets the bot_id of this PurchaseBase.


        :param bot_id: The bot_id of this PurchaseBase.  # noqa: E501
        :type: int
        """

        self._bot_id = bot_id

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
        if issubclass(PurchaseBase, dict):
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
        if not isinstance(other, PurchaseBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
