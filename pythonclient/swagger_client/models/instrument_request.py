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

class InstrumentRequest(object):
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
        'image_id': 'str',
        'pull_registry_uuid': 'str',
        'pull_repository': 'str',
        'pull_tag': 'str',
        'push_repository': 'str',
        'push_tag': 'str'
    }

    attribute_map = {
        'image_id': 'imageId',
        'pull_registry_uuid': 'pullRegistryUuid',
        'pull_repository': 'pullRepository',
        'pull_tag': 'pullTag',
        'push_repository': 'pushRepository',
        'push_tag': 'pushTag'
    }

    def __init__(self, image_id=None, pull_registry_uuid=None, pull_repository=None, pull_tag=None, push_repository=None, push_tag=None):  # noqa: E501
        """InstrumentRequest - a model defined in Swagger"""  # noqa: E501
        self._image_id = None
        self._pull_registry_uuid = None
        self._pull_repository = None
        self._pull_tag = None
        self._push_repository = None
        self._push_tag = None
        self.discriminator = None
        if image_id is not None:
            self.image_id = image_id
        if pull_registry_uuid is not None:
            self.pull_registry_uuid = pull_registry_uuid
        if pull_repository is not None:
            self.pull_repository = pull_repository
        if pull_tag is not None:
            self.pull_tag = pull_tag
        if push_repository is not None:
            self.push_repository = push_repository
        if push_tag is not None:
            self.push_tag = push_tag

    @property
    def image_id(self):
        """Gets the image_id of this InstrumentRequest.  # noqa: E501


        :return: The image_id of this InstrumentRequest.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this InstrumentRequest.


        :param image_id: The image_id of this InstrumentRequest.  # noqa: E501
        :type: str
        """

        self._image_id = image_id

    @property
    def pull_registry_uuid(self):
        """Gets the pull_registry_uuid of this InstrumentRequest.  # noqa: E501


        :return: The pull_registry_uuid of this InstrumentRequest.  # noqa: E501
        :rtype: str
        """
        return self._pull_registry_uuid

    @pull_registry_uuid.setter
    def pull_registry_uuid(self, pull_registry_uuid):
        """Sets the pull_registry_uuid of this InstrumentRequest.


        :param pull_registry_uuid: The pull_registry_uuid of this InstrumentRequest.  # noqa: E501
        :type: str
        """

        self._pull_registry_uuid = pull_registry_uuid

    @property
    def pull_repository(self):
        """Gets the pull_repository of this InstrumentRequest.  # noqa: E501


        :return: The pull_repository of this InstrumentRequest.  # noqa: E501
        :rtype: str
        """
        return self._pull_repository

    @pull_repository.setter
    def pull_repository(self, pull_repository):
        """Sets the pull_repository of this InstrumentRequest.


        :param pull_repository: The pull_repository of this InstrumentRequest.  # noqa: E501
        :type: str
        """

        self._pull_repository = pull_repository

    @property
    def pull_tag(self):
        """Gets the pull_tag of this InstrumentRequest.  # noqa: E501


        :return: The pull_tag of this InstrumentRequest.  # noqa: E501
        :rtype: str
        """
        return self._pull_tag

    @pull_tag.setter
    def pull_tag(self, pull_tag):
        """Sets the pull_tag of this InstrumentRequest.


        :param pull_tag: The pull_tag of this InstrumentRequest.  # noqa: E501
        :type: str
        """

        self._pull_tag = pull_tag

    @property
    def push_repository(self):
        """Gets the push_repository of this InstrumentRequest.  # noqa: E501


        :return: The push_repository of this InstrumentRequest.  # noqa: E501
        :rtype: str
        """
        return self._push_repository

    @push_repository.setter
    def push_repository(self, push_repository):
        """Sets the push_repository of this InstrumentRequest.


        :param push_repository: The push_repository of this InstrumentRequest.  # noqa: E501
        :type: str
        """

        self._push_repository = push_repository

    @property
    def push_tag(self):
        """Gets the push_tag of this InstrumentRequest.  # noqa: E501


        :return: The push_tag of this InstrumentRequest.  # noqa: E501
        :rtype: str
        """
        return self._push_tag

    @push_tag.setter
    def push_tag(self, push_tag):
        """Sets the push_tag of this InstrumentRequest.


        :param push_tag: The push_tag of this InstrumentRequest.  # noqa: E501
        :type: str
        """

        self._push_tag = push_tag

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
        if issubclass(InstrumentRequest, dict):
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
        if not isinstance(other, InstrumentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
