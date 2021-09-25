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

class ScheduleFilters(object):
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
        'days': 'int',
        'repo_tags': 'list[ScheduleRepoTags]'
    }

    attribute_map = {
        'days': 'days',
        'repo_tags': 'repoTags'
    }

    def __init__(self, days=None, repo_tags=None):  # noqa: E501
        """ScheduleFilters - a model defined in Swagger"""  # noqa: E501
        self._days = None
        self._repo_tags = None
        self.discriminator = None
        if days is not None:
            self.days = days
        if repo_tags is not None:
            self.repo_tags = repo_tags

    @property
    def days(self):
        """Gets the days of this ScheduleFilters.  # noqa: E501


        :return: The days of this ScheduleFilters.  # noqa: E501
        :rtype: int
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this ScheduleFilters.


        :param days: The days of this ScheduleFilters.  # noqa: E501
        :type: int
        """

        self._days = days

    @property
    def repo_tags(self):
        """Gets the repo_tags of this ScheduleFilters.  # noqa: E501


        :return: The repo_tags of this ScheduleFilters.  # noqa: E501
        :rtype: list[ScheduleRepoTags]
        """
        return self._repo_tags

    @repo_tags.setter
    def repo_tags(self, repo_tags):
        """Sets the repo_tags of this ScheduleFilters.


        :param repo_tags: The repo_tags of this ScheduleFilters.  # noqa: E501
        :type: list[ScheduleRepoTags]
        """

        self._repo_tags = repo_tags

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
        if issubclass(ScheduleFilters, dict):
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
        if not isinstance(other, ScheduleFilters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
