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

class ReportRequest(object):
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
        'description': 'str',
        'name': 'str',
        'filter': 'str',
        'display_columns': 'list[str]',
        'template_name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'filter': 'filter',
        'display_columns': 'displayColumns',
        'template_name': 'templateName'
    }

    def __init__(self, description=None, name=None, filter=None, display_columns=None, template_name=None):  # noqa: E501
        """ReportRequest - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._name = None
        self._filter = None
        self._display_columns = None
        self._template_name = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if filter is not None:
            self.filter = filter
        if display_columns is not None:
            self.display_columns = display_columns
        if template_name is not None:
            self.template_name = template_name

    @property
    def description(self):
        """Gets the description of this ReportRequest.  # noqa: E501


        :return: The description of this ReportRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ReportRequest.


        :param description: The description of this ReportRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this ReportRequest.  # noqa: E501


        :return: The name of this ReportRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReportRequest.


        :param name: The name of this ReportRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def filter(self):
        """Gets the filter of this ReportRequest.  # noqa: E501


        :return: The filter of this ReportRequest.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ReportRequest.


        :param filter: The filter of this ReportRequest.  # noqa: E501
        :type: str
        """

        self._filter = filter

    @property
    def display_columns(self):
        """Gets the display_columns of this ReportRequest.  # noqa: E501

        Provide parameter values in the format shown under Example Value.  # noqa: E501

        :return: The display_columns of this ReportRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._display_columns

    @display_columns.setter
    def display_columns(self, display_columns):
        """Sets the display_columns of this ReportRequest.

        Provide parameter values in the format shown under Example Value.  # noqa: E501

        :param display_columns: The display_columns of this ReportRequest.  # noqa: E501
        :type: list[str]
        """

        self._display_columns = display_columns

    @property
    def template_name(self):
        """Gets the template_name of this ReportRequest.  # noqa: E501


        :return: The template_name of this ReportRequest.  # noqa: E501
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this ReportRequest.


        :param template_name: The template_name of this ReportRequest.  # noqa: E501
        :type: str
        """

        self._template_name = template_name

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
        if issubclass(ReportRequest, dict):
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
        if not isinstance(other, ReportRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
