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

class Sensor(object):
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
        'activation_uuid': 'str',
        'binary_version': 'str',
        'configuration_profile': 'str',
        'container_ipv4': 'str',
        'container_ipv6': 'str',
        'container_mac_address': 'str',
        'created': 'str',
        'customer_uuid': 'str',
        'docker_version': 'str',
        'host_uuid': 'str',
        'hostname': 'str',
        'image_id': 'str',
        'image_sha': 'str',
        'ipv4': 'str',
        'ipv6': 'str',
        'label': 'BulkContainerDetailsLabel',
        'last_checked_in': 'str',
        'mac_address': 'str',
        'name': 'str',
        'os': 'str',
        'platform': 'str',
        'privileged': 'str',
        'registry': 'str',
        'sensor_id': 'str',
        'sensor_type': 'str',
        'sensor_version': 'str',
        'sha': 'str',
        'status': 'str',
        'uuid': 'str',
        'vuln_sig_version': 'str',
        'cluster': 'Cluster'
    }

    attribute_map = {
        'activation_uuid': 'activationUuid',
        'binary_version': 'binaryVersion',
        'configuration_profile': 'configurationProfile',
        'container_ipv4': 'containerIpv4',
        'container_ipv6': 'containerIpv6',
        'container_mac_address': 'containerMacAddress',
        'created': 'created',
        'customer_uuid': 'customerUuid',
        'docker_version': 'dockerVersion',
        'host_uuid': 'hostUuid',
        'hostname': 'hostname',
        'image_id': 'imageId',
        'image_sha': 'imageSha',
        'ipv4': 'ipv4',
        'ipv6': 'ipv6',
        'label': 'label',
        'last_checked_in': 'lastCheckedIn',
        'mac_address': 'macAddress',
        'name': 'name',
        'os': 'os',
        'platform': 'platform',
        'privileged': 'privileged',
        'registry': 'registry',
        'sensor_id': 'sensorId',
        'sensor_type': 'sensorType',
        'sensor_version': 'sensorVersion',
        'sha': 'sha',
        'status': 'status',
        'uuid': 'uuid',
        'vuln_sig_version': 'vulnSigVersion',
        'cluster': 'cluster'
    }

    def __init__(self, activation_uuid=None, binary_version=None, configuration_profile=None, container_ipv4=None, container_ipv6=None, container_mac_address=None, created=None, customer_uuid=None, docker_version=None, host_uuid=None, hostname=None, image_id=None, image_sha=None, ipv4=None, ipv6=None, label=None, last_checked_in=None, mac_address=None, name=None, os=None, platform=None, privileged=None, registry=None, sensor_id=None, sensor_type=None, sensor_version=None, sha=None, status=None, uuid=None, vuln_sig_version=None, cluster=None):  # noqa: E501
        """Sensor - a model defined in Swagger"""  # noqa: E501
        self._activation_uuid = None
        self._binary_version = None
        self._configuration_profile = None
        self._container_ipv4 = None
        self._container_ipv6 = None
        self._container_mac_address = None
        self._created = None
        self._customer_uuid = None
        self._docker_version = None
        self._host_uuid = None
        self._hostname = None
        self._image_id = None
        self._image_sha = None
        self._ipv4 = None
        self._ipv6 = None
        self._label = None
        self._last_checked_in = None
        self._mac_address = None
        self._name = None
        self._os = None
        self._platform = None
        self._privileged = None
        self._registry = None
        self._sensor_id = None
        self._sensor_type = None
        self._sensor_version = None
        self._sha = None
        self._status = None
        self._uuid = None
        self._vuln_sig_version = None
        self._cluster = None
        self.discriminator = None
        if activation_uuid is not None:
            self.activation_uuid = activation_uuid
        if binary_version is not None:
            self.binary_version = binary_version
        if configuration_profile is not None:
            self.configuration_profile = configuration_profile
        if container_ipv4 is not None:
            self.container_ipv4 = container_ipv4
        if container_ipv6 is not None:
            self.container_ipv6 = container_ipv6
        if container_mac_address is not None:
            self.container_mac_address = container_mac_address
        if created is not None:
            self.created = created
        if customer_uuid is not None:
            self.customer_uuid = customer_uuid
        if docker_version is not None:
            self.docker_version = docker_version
        if host_uuid is not None:
            self.host_uuid = host_uuid
        if hostname is not None:
            self.hostname = hostname
        if image_id is not None:
            self.image_id = image_id
        if image_sha is not None:
            self.image_sha = image_sha
        if ipv4 is not None:
            self.ipv4 = ipv4
        if ipv6 is not None:
            self.ipv6 = ipv6
        if label is not None:
            self.label = label
        if last_checked_in is not None:
            self.last_checked_in = last_checked_in
        if mac_address is not None:
            self.mac_address = mac_address
        if name is not None:
            self.name = name
        if os is not None:
            self.os = os
        if platform is not None:
            self.platform = platform
        if privileged is not None:
            self.privileged = privileged
        if registry is not None:
            self.registry = registry
        if sensor_id is not None:
            self.sensor_id = sensor_id
        if sensor_type is not None:
            self.sensor_type = sensor_type
        if sensor_version is not None:
            self.sensor_version = sensor_version
        if sha is not None:
            self.sha = sha
        if status is not None:
            self.status = status
        if uuid is not None:
            self.uuid = uuid
        if vuln_sig_version is not None:
            self.vuln_sig_version = vuln_sig_version
        if cluster is not None:
            self.cluster = cluster

    @property
    def activation_uuid(self):
        """Gets the activation_uuid of this Sensor.  # noqa: E501


        :return: The activation_uuid of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._activation_uuid

    @activation_uuid.setter
    def activation_uuid(self, activation_uuid):
        """Sets the activation_uuid of this Sensor.


        :param activation_uuid: The activation_uuid of this Sensor.  # noqa: E501
        :type: str
        """

        self._activation_uuid = activation_uuid

    @property
    def binary_version(self):
        """Gets the binary_version of this Sensor.  # noqa: E501


        :return: The binary_version of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._binary_version

    @binary_version.setter
    def binary_version(self, binary_version):
        """Sets the binary_version of this Sensor.


        :param binary_version: The binary_version of this Sensor.  # noqa: E501
        :type: str
        """

        self._binary_version = binary_version

    @property
    def configuration_profile(self):
        """Gets the configuration_profile of this Sensor.  # noqa: E501


        :return: The configuration_profile of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._configuration_profile

    @configuration_profile.setter
    def configuration_profile(self, configuration_profile):
        """Sets the configuration_profile of this Sensor.


        :param configuration_profile: The configuration_profile of this Sensor.  # noqa: E501
        :type: str
        """

        self._configuration_profile = configuration_profile

    @property
    def container_ipv4(self):
        """Gets the container_ipv4 of this Sensor.  # noqa: E501


        :return: The container_ipv4 of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._container_ipv4

    @container_ipv4.setter
    def container_ipv4(self, container_ipv4):
        """Sets the container_ipv4 of this Sensor.


        :param container_ipv4: The container_ipv4 of this Sensor.  # noqa: E501
        :type: str
        """

        self._container_ipv4 = container_ipv4

    @property
    def container_ipv6(self):
        """Gets the container_ipv6 of this Sensor.  # noqa: E501


        :return: The container_ipv6 of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._container_ipv6

    @container_ipv6.setter
    def container_ipv6(self, container_ipv6):
        """Sets the container_ipv6 of this Sensor.


        :param container_ipv6: The container_ipv6 of this Sensor.  # noqa: E501
        :type: str
        """

        self._container_ipv6 = container_ipv6

    @property
    def container_mac_address(self):
        """Gets the container_mac_address of this Sensor.  # noqa: E501


        :return: The container_mac_address of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._container_mac_address

    @container_mac_address.setter
    def container_mac_address(self, container_mac_address):
        """Sets the container_mac_address of this Sensor.


        :param container_mac_address: The container_mac_address of this Sensor.  # noqa: E501
        :type: str
        """

        self._container_mac_address = container_mac_address

    @property
    def created(self):
        """Gets the created of this Sensor.  # noqa: E501


        :return: The created of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Sensor.


        :param created: The created of this Sensor.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def customer_uuid(self):
        """Gets the customer_uuid of this Sensor.  # noqa: E501


        :return: The customer_uuid of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._customer_uuid

    @customer_uuid.setter
    def customer_uuid(self, customer_uuid):
        """Sets the customer_uuid of this Sensor.


        :param customer_uuid: The customer_uuid of this Sensor.  # noqa: E501
        :type: str
        """

        self._customer_uuid = customer_uuid

    @property
    def docker_version(self):
        """Gets the docker_version of this Sensor.  # noqa: E501


        :return: The docker_version of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._docker_version

    @docker_version.setter
    def docker_version(self, docker_version):
        """Sets the docker_version of this Sensor.


        :param docker_version: The docker_version of this Sensor.  # noqa: E501
        :type: str
        """

        self._docker_version = docker_version

    @property
    def host_uuid(self):
        """Gets the host_uuid of this Sensor.  # noqa: E501


        :return: The host_uuid of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._host_uuid

    @host_uuid.setter
    def host_uuid(self, host_uuid):
        """Sets the host_uuid of this Sensor.


        :param host_uuid: The host_uuid of this Sensor.  # noqa: E501
        :type: str
        """

        self._host_uuid = host_uuid

    @property
    def hostname(self):
        """Gets the hostname of this Sensor.  # noqa: E501


        :return: The hostname of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this Sensor.


        :param hostname: The hostname of this Sensor.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def image_id(self):
        """Gets the image_id of this Sensor.  # noqa: E501


        :return: The image_id of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this Sensor.


        :param image_id: The image_id of this Sensor.  # noqa: E501
        :type: str
        """

        self._image_id = image_id

    @property
    def image_sha(self):
        """Gets the image_sha of this Sensor.  # noqa: E501


        :return: The image_sha of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._image_sha

    @image_sha.setter
    def image_sha(self, image_sha):
        """Sets the image_sha of this Sensor.


        :param image_sha: The image_sha of this Sensor.  # noqa: E501
        :type: str
        """

        self._image_sha = image_sha

    @property
    def ipv4(self):
        """Gets the ipv4 of this Sensor.  # noqa: E501


        :return: The ipv4 of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._ipv4

    @ipv4.setter
    def ipv4(self, ipv4):
        """Sets the ipv4 of this Sensor.


        :param ipv4: The ipv4 of this Sensor.  # noqa: E501
        :type: str
        """

        self._ipv4 = ipv4

    @property
    def ipv6(self):
        """Gets the ipv6 of this Sensor.  # noqa: E501


        :return: The ipv6 of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._ipv6

    @ipv6.setter
    def ipv6(self, ipv6):
        """Sets the ipv6 of this Sensor.


        :param ipv6: The ipv6 of this Sensor.  # noqa: E501
        :type: str
        """

        self._ipv6 = ipv6

    @property
    def label(self):
        """Gets the label of this Sensor.  # noqa: E501


        :return: The label of this Sensor.  # noqa: E501
        :rtype: BulkContainerDetailsLabel
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Sensor.


        :param label: The label of this Sensor.  # noqa: E501
        :type: BulkContainerDetailsLabel
        """

        self._label = label

    @property
    def last_checked_in(self):
        """Gets the last_checked_in of this Sensor.  # noqa: E501


        :return: The last_checked_in of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._last_checked_in

    @last_checked_in.setter
    def last_checked_in(self, last_checked_in):
        """Sets the last_checked_in of this Sensor.


        :param last_checked_in: The last_checked_in of this Sensor.  # noqa: E501
        :type: str
        """

        self._last_checked_in = last_checked_in

    @property
    def mac_address(self):
        """Gets the mac_address of this Sensor.  # noqa: E501


        :return: The mac_address of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this Sensor.


        :param mac_address: The mac_address of this Sensor.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def name(self):
        """Gets the name of this Sensor.  # noqa: E501


        :return: The name of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Sensor.


        :param name: The name of this Sensor.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def os(self):
        """Gets the os of this Sensor.  # noqa: E501


        :return: The os of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this Sensor.


        :param os: The os of this Sensor.  # noqa: E501
        :type: str
        """

        self._os = os

    @property
    def platform(self):
        """Gets the platform of this Sensor.  # noqa: E501


        :return: The platform of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this Sensor.


        :param platform: The platform of this Sensor.  # noqa: E501
        :type: str
        """

        self._platform = platform

    @property
    def privileged(self):
        """Gets the privileged of this Sensor.  # noqa: E501


        :return: The privileged of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._privileged

    @privileged.setter
    def privileged(self, privileged):
        """Sets the privileged of this Sensor.


        :param privileged: The privileged of this Sensor.  # noqa: E501
        :type: str
        """

        self._privileged = privileged

    @property
    def registry(self):
        """Gets the registry of this Sensor.  # noqa: E501


        :return: The registry of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._registry

    @registry.setter
    def registry(self, registry):
        """Sets the registry of this Sensor.


        :param registry: The registry of this Sensor.  # noqa: E501
        :type: str
        """

        self._registry = registry

    @property
    def sensor_id(self):
        """Gets the sensor_id of this Sensor.  # noqa: E501


        :return: The sensor_id of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._sensor_id

    @sensor_id.setter
    def sensor_id(self, sensor_id):
        """Sets the sensor_id of this Sensor.


        :param sensor_id: The sensor_id of this Sensor.  # noqa: E501
        :type: str
        """

        self._sensor_id = sensor_id

    @property
    def sensor_type(self):
        """Gets the sensor_type of this Sensor.  # noqa: E501


        :return: The sensor_type of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._sensor_type

    @sensor_type.setter
    def sensor_type(self, sensor_type):
        """Sets the sensor_type of this Sensor.


        :param sensor_type: The sensor_type of this Sensor.  # noqa: E501
        :type: str
        """

        self._sensor_type = sensor_type

    @property
    def sensor_version(self):
        """Gets the sensor_version of this Sensor.  # noqa: E501


        :return: The sensor_version of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._sensor_version

    @sensor_version.setter
    def sensor_version(self, sensor_version):
        """Sets the sensor_version of this Sensor.


        :param sensor_version: The sensor_version of this Sensor.  # noqa: E501
        :type: str
        """

        self._sensor_version = sensor_version

    @property
    def sha(self):
        """Gets the sha of this Sensor.  # noqa: E501


        :return: The sha of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this Sensor.


        :param sha: The sha of this Sensor.  # noqa: E501
        :type: str
        """

        self._sha = sha

    @property
    def status(self):
        """Gets the status of this Sensor.  # noqa: E501


        :return: The status of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Sensor.


        :param status: The status of this Sensor.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def uuid(self):
        """Gets the uuid of this Sensor.  # noqa: E501


        :return: The uuid of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Sensor.


        :param uuid: The uuid of this Sensor.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def vuln_sig_version(self):
        """Gets the vuln_sig_version of this Sensor.  # noqa: E501


        :return: The vuln_sig_version of this Sensor.  # noqa: E501
        :rtype: str
        """
        return self._vuln_sig_version

    @vuln_sig_version.setter
    def vuln_sig_version(self, vuln_sig_version):
        """Sets the vuln_sig_version of this Sensor.


        :param vuln_sig_version: The vuln_sig_version of this Sensor.  # noqa: E501
        :type: str
        """

        self._vuln_sig_version = vuln_sig_version

    @property
    def cluster(self):
        """Gets the cluster of this Sensor.  # noqa: E501


        :return: The cluster of this Sensor.  # noqa: E501
        :rtype: Cluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this Sensor.


        :param cluster: The cluster of this Sensor.  # noqa: E501
        :type: Cluster
        """

        self._cluster = cluster

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
        if issubclass(Sensor, dict):
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
        if not isinstance(other, Sensor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
