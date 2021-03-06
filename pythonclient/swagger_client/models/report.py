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

class Report(object):
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
        'created_at': 'str',
        'description': 'str',
        'file_format': 'str',
        'report_uuid': 'str',
        'filter': 'str',
        'display_columns': 'list[str]',
        'report_name': 'str',
        'report_type': 'str',
        'status': 'str',
        'template_name': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'description': 'description',
        'file_format': 'fileFormat',
        'report_uuid': 'reportUuid',
        'filter': 'filter',
        'display_columns': 'displayColumns',
        'report_name': 'reportName',
        'report_type': 'reportType',
        'status': 'status',
        'template_name': 'templateName'
    }

    def __init__(self, created_at=None, description=None, file_format=None, report_uuid=None, filter=None, display_columns=None, report_name=None, report_type=None, status=None, template_name=None):  # noqa: E501
        """Report - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._description = None
        self._file_format = None
        self._report_uuid = None
        self._filter = None
        self._display_columns = None
        self._report_name = None
        self._report_type = None
        self._status = None
        self._template_name = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if file_format is not None:
            self.file_format = file_format
        if report_uuid is not None:
            self.report_uuid = report_uuid
        if filter is not None:
            self.filter = filter
        if display_columns is not None:
            self.display_columns = display_columns
        if report_name is not None:
            self.report_name = report_name
        if report_type is not None:
            self.report_type = report_type
        if status is not None:
            self.status = status
        if template_name is not None:
            self.template_name = template_name

    @property
    def created_at(self):
        """Gets the created_at of this Report.  # noqa: E501


        :return: The created_at of this Report.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Report.


        :param created_at: The created_at of this Report.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this Report.  # noqa: E501


        :return: The description of this Report.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Report.


        :param description: The description of this Report.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def file_format(self):
        """Gets the file_format of this Report.  # noqa: E501


        :return: The file_format of this Report.  # noqa: E501
        :rtype: str
        """
        return self._file_format

    @file_format.setter
    def file_format(self, file_format):
        """Sets the file_format of this Report.


        :param file_format: The file_format of this Report.  # noqa: E501
        :type: str
        """

        self._file_format = file_format

    @property
    def report_uuid(self):
        """Gets the report_uuid of this Report.  # noqa: E501


        :return: The report_uuid of this Report.  # noqa: E501
        :rtype: str
        """
        return self._report_uuid

    @report_uuid.setter
    def report_uuid(self, report_uuid):
        """Sets the report_uuid of this Report.


        :param report_uuid: The report_uuid of this Report.  # noqa: E501
        :type: str
        """

        self._report_uuid = report_uuid

    @property
    def filter(self):
        """Gets the filter of this Report.  # noqa: E501


        :return: The filter of this Report.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this Report.


        :param filter: The filter of this Report.  # noqa: E501
        :type: str
        """

        self._filter = filter

    @property
    def display_columns(self):
        """Gets the display_columns of this Report.  # noqa: E501

        Provide parameter values in the format shown under Example Value.  # noqa: E501

        :return: The display_columns of this Report.  # noqa: E501
        :rtype: list[str]
        """
        return self._display_columns

    @display_columns.setter
    def display_columns(self, display_columns):
        """Sets the display_columns of this Report.

        Provide parameter values in the format shown under Example Value.  # noqa: E501

        :param display_columns: The display_columns of this Report.  # noqa: E501
        :type: list[str]
        """

        self._display_columns = display_columns

    @property
    def report_name(self):
        """Gets the report_name of this Report.  # noqa: E501


        :return: The report_name of this Report.  # noqa: E501
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        """Sets the report_name of this Report.


        :param report_name: The report_name of this Report.  # noqa: E501
        :type: str
        """

        self._report_name = report_name

    @property
    def report_type(self):
        """Gets the report_type of this Report.  # noqa: E501


        :return: The report_type of this Report.  # noqa: E501
        :rtype: str
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """Sets the report_type of this Report.


        :param report_type: The report_type of this Report.  # noqa: E501
        :type: str
        """

        self._report_type = report_type

    @property
    def status(self):
        """Gets the status of this Report.  # noqa: E501


        :return: The status of this Report.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Report.


        :param status: The status of this Report.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def template_name(self):
        """Gets the template_name of this Report.  # noqa: E501


        :return: The template_name of this Report.  # noqa: E501
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this Report.


        :param template_name: The template_name of this Report.  # noqa: E501
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
        if issubclass(Report, dict):
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
        if not isinstance(other, Report):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
