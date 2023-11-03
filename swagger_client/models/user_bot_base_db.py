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

class UserBotBaseDb(object):
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
        'user_id': 'int',
        'bot_token': 'str',
        'last_mess': 'int',
        'items': 'str',
        'new_user': 'bool',
        'subscribe_channel': 'bool',
        'utm_mark_id': 'int',
        'user': 'UserBaseDb',
        'bot': 'BotBase',
        'partner': 'PartnerBase',
        'utm_mark': 'UtmMarkBase',
        'orders': 'list[OrderBase]'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'user_id',
        'bot_token': 'bot_token',
        'last_mess': 'last_mess',
        'items': 'items',
        'new_user': 'new_user',
        'subscribe_channel': 'subscribe_channel',
        'utm_mark_id': 'utm_mark_id',
        'user': 'user',
        'bot': 'bot',
        'partner': 'partner',
        'utm_mark': 'utm_mark',
        'orders': 'orders'
    }

    def __init__(self, id=None, user_id=None, bot_token=None, last_mess=None, items=None, new_user=None, subscribe_channel=None, utm_mark_id=None, user=None, bot=None, partner=None, utm_mark=None, orders=None):  # noqa: E501
        """UserBotBaseDb - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._user_id = None
        self._bot_token = None
        self._last_mess = None
        self._items = None
        self._new_user = None
        self._subscribe_channel = None
        self._utm_mark_id = None
        self._user = None
        self._bot = None
        self._partner = None
        self._utm_mark = None
        self._orders = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if user_id is not None:
            self.user_id = user_id
        if bot_token is not None:
            self.bot_token = bot_token
        if last_mess is not None:
            self.last_mess = last_mess
        if items is not None:
            self.items = items
        if new_user is not None:
            self.new_user = new_user
        if subscribe_channel is not None:
            self.subscribe_channel = subscribe_channel
        if utm_mark_id is not None:
            self.utm_mark_id = utm_mark_id
        if user is not None:
            self.user = user
        if bot is not None:
            self.bot = bot
        if partner is not None:
            self.partner = partner
        if utm_mark is not None:
            self.utm_mark = utm_mark
        if orders is not None:
            self.orders = orders

    @property
    def id(self):
        """Gets the id of this UserBotBaseDb.  # noqa: E501


        :return: The id of this UserBotBaseDb.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserBotBaseDb.


        :param id: The id of this UserBotBaseDb.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this UserBotBaseDb.  # noqa: E501


        :return: The user_id of this UserBotBaseDb.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserBotBaseDb.


        :param user_id: The user_id of this UserBotBaseDb.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def bot_token(self):
        """Gets the bot_token of this UserBotBaseDb.  # noqa: E501


        :return: The bot_token of this UserBotBaseDb.  # noqa: E501
        :rtype: str
        """
        return self._bot_token

    @bot_token.setter
    def bot_token(self, bot_token):
        """Sets the bot_token of this UserBotBaseDb.


        :param bot_token: The bot_token of this UserBotBaseDb.  # noqa: E501
        :type: str
        """

        self._bot_token = bot_token

    @property
    def last_mess(self):
        """Gets the last_mess of this UserBotBaseDb.  # noqa: E501


        :return: The last_mess of this UserBotBaseDb.  # noqa: E501
        :rtype: int
        """
        return self._last_mess

    @last_mess.setter
    def last_mess(self, last_mess):
        """Sets the last_mess of this UserBotBaseDb.


        :param last_mess: The last_mess of this UserBotBaseDb.  # noqa: E501
        :type: int
        """

        self._last_mess = last_mess

    @property
    def items(self):
        """Gets the items of this UserBotBaseDb.  # noqa: E501


        :return: The items of this UserBotBaseDb.  # noqa: E501
        :rtype: str
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this UserBotBaseDb.


        :param items: The items of this UserBotBaseDb.  # noqa: E501
        :type: str
        """

        self._items = items

    @property
    def new_user(self):
        """Gets the new_user of this UserBotBaseDb.  # noqa: E501


        :return: The new_user of this UserBotBaseDb.  # noqa: E501
        :rtype: bool
        """
        return self._new_user

    @new_user.setter
    def new_user(self, new_user):
        """Sets the new_user of this UserBotBaseDb.


        :param new_user: The new_user of this UserBotBaseDb.  # noqa: E501
        :type: bool
        """

        self._new_user = new_user

    @property
    def subscribe_channel(self):
        """Gets the subscribe_channel of this UserBotBaseDb.  # noqa: E501


        :return: The subscribe_channel of this UserBotBaseDb.  # noqa: E501
        :rtype: bool
        """
        return self._subscribe_channel

    @subscribe_channel.setter
    def subscribe_channel(self, subscribe_channel):
        """Sets the subscribe_channel of this UserBotBaseDb.


        :param subscribe_channel: The subscribe_channel of this UserBotBaseDb.  # noqa: E501
        :type: bool
        """

        self._subscribe_channel = subscribe_channel

    @property
    def utm_mark_id(self):
        """Gets the utm_mark_id of this UserBotBaseDb.  # noqa: E501


        :return: The utm_mark_id of this UserBotBaseDb.  # noqa: E501
        :rtype: int
        """
        return self._utm_mark_id

    @utm_mark_id.setter
    def utm_mark_id(self, utm_mark_id):
        """Sets the utm_mark_id of this UserBotBaseDb.


        :param utm_mark_id: The utm_mark_id of this UserBotBaseDb.  # noqa: E501
        :type: int
        """

        self._utm_mark_id = utm_mark_id

    @property
    def user(self):
        """Gets the user of this UserBotBaseDb.  # noqa: E501


        :return: The user of this UserBotBaseDb.  # noqa: E501
        :rtype: UserBaseDb
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this UserBotBaseDb.


        :param user: The user of this UserBotBaseDb.  # noqa: E501
        :type: UserBaseDb
        """

        self._user = user

    @property
    def bot(self):
        """Gets the bot of this UserBotBaseDb.  # noqa: E501


        :return: The bot of this UserBotBaseDb.  # noqa: E501
        :rtype: BotBase
        """
        return self._bot

    @bot.setter
    def bot(self, bot):
        """Sets the bot of this UserBotBaseDb.


        :param bot: The bot of this UserBotBaseDb.  # noqa: E501
        :type: BotBase
        """

        self._bot = bot

    @property
    def partner(self):
        """Gets the partner of this UserBotBaseDb.  # noqa: E501


        :return: The partner of this UserBotBaseDb.  # noqa: E501
        :rtype: PartnerBase
        """
        return self._partner

    @partner.setter
    def partner(self, partner):
        """Sets the partner of this UserBotBaseDb.


        :param partner: The partner of this UserBotBaseDb.  # noqa: E501
        :type: PartnerBase
        """

        self._partner = partner

    @property
    def utm_mark(self):
        """Gets the utm_mark of this UserBotBaseDb.  # noqa: E501


        :return: The utm_mark of this UserBotBaseDb.  # noqa: E501
        :rtype: UtmMarkBase
        """
        return self._utm_mark

    @utm_mark.setter
    def utm_mark(self, utm_mark):
        """Sets the utm_mark of this UserBotBaseDb.


        :param utm_mark: The utm_mark of this UserBotBaseDb.  # noqa: E501
        :type: UtmMarkBase
        """

        self._utm_mark = utm_mark

    @property
    def orders(self):
        """Gets the orders of this UserBotBaseDb.  # noqa: E501


        :return: The orders of this UserBotBaseDb.  # noqa: E501
        :rtype: list[OrderBase]
        """
        return self._orders

    @orders.setter
    def orders(self, orders):
        """Sets the orders of this UserBotBaseDb.


        :param orders: The orders of this UserBotBaseDb.  # noqa: E501
        :type: list[OrderBase]
        """

        self._orders = orders

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
        if issubclass(UserBotBaseDb, dict):
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
        if not isinstance(other, UserBotBaseDb):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
