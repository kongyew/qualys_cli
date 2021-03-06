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

class PortMapping(object):
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
        'host_ip': 'str',
        'host_port': 'int',
        'port': 'int',
        'protocol': 'str'
    }

    attribute_map = {
        'host_ip': 'hostIp',
        'host_port': 'hostPort',
        'port': 'port',
        'protocol': 'protocol'
    }

    def __init__(self, host_ip=None, host_port=None, port=None, protocol=None):  # noqa: E501
        """PortMapping - a model defined in Swagger"""  # noqa: E501
        self._host_ip = None
        self._host_port = None
        self._port = None
        self._protocol = None
        self.discriminator = None
        if host_ip is not None:
            self.host_ip = host_ip
        if host_port is not None:
            self.host_port = host_port
        if port is not None:
            self.port = port
        if protocol is not None:
            self.protocol = protocol

    @property
    def host_ip(self):
        """Gets the host_ip of this PortMapping.  # noqa: E501


        :return: The host_ip of this PortMapping.  # noqa: E501
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this PortMapping.


        :param host_ip: The host_ip of this PortMapping.  # noqa: E501
        :type: str
        """

        self._host_ip = host_ip

    @property
    def host_port(self):
        """Gets the host_port of this PortMapping.  # noqa: E501


        :return: The host_port of this PortMapping.  # noqa: E501
        :rtype: int
        """
        return self._host_port

    @host_port.setter
    def host_port(self, host_port):
        """Sets the host_port of this PortMapping.


        :param host_port: The host_port of this PortMapping.  # noqa: E501
        :type: int
        """

        self._host_port = host_port

    @property
    def port(self):
        """Gets the port of this PortMapping.  # noqa: E501


        :return: The port of this PortMapping.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this PortMapping.


        :param port: The port of this PortMapping.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this PortMapping.  # noqa: E501


        :return: The protocol of this PortMapping.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this PortMapping.


        :param protocol: The protocol of this PortMapping.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

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
        if issubclass(PortMapping, dict):
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
        if not isinstance(other, PortMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
