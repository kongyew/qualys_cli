# coding: utf-8

"""
    Container Security API

    # Authentication You must authenticate to the Qualys Cloud Platform using Qualys account credentials (user name and password) and get the JSON Web Token (JWT) before you can start using the Container Security APIs. Use the Qualys Authentication API to get the JWT.  **Example Authentication Curl Request**:  curl -X POST https://gateway/auth -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=value1&password=passwordValue&token=true' where - gateway is the base URL to the Qualys API server where your account is located. - **username** and **password** are the credentials of the user account for which you want to fetch Container Security data. - **token** should be **true** - **Content-Type** should be **application/x-www-form-urlencoded**   # noqa: E501

    OpenAPI spec version: v1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PcControl(object):
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
        'statement': 'str',
        'criticality': 'str',
        'comments': 'str',
        'deprecated': 'str',
        'category': 'str',
        'sub_category': 'str',
        'technologies': 'list[ControlTechnology]'
    }

    attribute_map = {
        'id': 'id',
        'statement': 'statement',
        'criticality': 'criticality',
        'comments': 'comments',
        'deprecated': 'deprecated',
        'category': 'category',
        'sub_category': 'subCategory',
        'technologies': 'technologies'
    }

    def __init__(self, id=None, statement=None, criticality=None, comments=None, deprecated=None, category=None, sub_category=None, technologies=None):  # noqa: E501
        """PcControl - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._statement = None
        self._criticality = None
        self._comments = None
        self._deprecated = None
        self._category = None
        self._sub_category = None
        self._technologies = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if statement is not None:
            self.statement = statement
        if criticality is not None:
            self.criticality = criticality
        if comments is not None:
            self.comments = comments
        if deprecated is not None:
            self.deprecated = deprecated
        if category is not None:
            self.category = category
        if sub_category is not None:
            self.sub_category = sub_category
        if technologies is not None:
            self.technologies = technologies

    @property
    def id(self):
        """Gets the id of this PcControl.  # noqa: E501


        :return: The id of this PcControl.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PcControl.


        :param id: The id of this PcControl.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def statement(self):
        """Gets the statement of this PcControl.  # noqa: E501


        :return: The statement of this PcControl.  # noqa: E501
        :rtype: str
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        """Sets the statement of this PcControl.


        :param statement: The statement of this PcControl.  # noqa: E501
        :type: str
        """

        self._statement = statement

    @property
    def criticality(self):
        """Gets the criticality of this PcControl.  # noqa: E501


        :return: The criticality of this PcControl.  # noqa: E501
        :rtype: str
        """
        return self._criticality

    @criticality.setter
    def criticality(self, criticality):
        """Sets the criticality of this PcControl.


        :param criticality: The criticality of this PcControl.  # noqa: E501
        :type: str
        """

        self._criticality = criticality

    @property
    def comments(self):
        """Gets the comments of this PcControl.  # noqa: E501


        :return: The comments of this PcControl.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this PcControl.


        :param comments: The comments of this PcControl.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def deprecated(self):
        """Gets the deprecated of this PcControl.  # noqa: E501


        :return: The deprecated of this PcControl.  # noqa: E501
        :rtype: str
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """Sets the deprecated of this PcControl.


        :param deprecated: The deprecated of this PcControl.  # noqa: E501
        :type: str
        """

        self._deprecated = deprecated

    @property
    def category(self):
        """Gets the category of this PcControl.  # noqa: E501


        :return: The category of this PcControl.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this PcControl.


        :param category: The category of this PcControl.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def sub_category(self):
        """Gets the sub_category of this PcControl.  # noqa: E501


        :return: The sub_category of this PcControl.  # noqa: E501
        :rtype: str
        """
        return self._sub_category

    @sub_category.setter
    def sub_category(self, sub_category):
        """Sets the sub_category of this PcControl.


        :param sub_category: The sub_category of this PcControl.  # noqa: E501
        :type: str
        """

        self._sub_category = sub_category

    @property
    def technologies(self):
        """Gets the technologies of this PcControl.  # noqa: E501


        :return: The technologies of this PcControl.  # noqa: E501
        :rtype: list[ControlTechnology]
        """
        return self._technologies

    @technologies.setter
    def technologies(self, technologies):
        """Sets the technologies of this PcControl.


        :param technologies: The technologies of this PcControl.  # noqa: E501
        :type: list[ControlTechnology]
        """

        self._technologies = technologies

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
        if issubclass(PcControl, dict):
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
        if not isinstance(other, PcControl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
