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

class ImageDetails(object):
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
        'created': 'str',
        'updated': 'str',
        'author': 'str',
        'repo': 'list[Repo]',
        'repo_digests': 'list[RepoDigest]',
        'label': 'list[BulkContainerDetailsLabel]',
        'uuid': 'str',
        'sha': 'str',
        'operating_system': 'str',
        'customer_uuid': 'str',
        'docker_version': 'str',
        'size': 'int',
        'layers': 'list[Layer]',
        'host': 'list[Host]',
        'architecture': 'str',
        'image_id': 'str',
        'registry_uuid': 'list[str]',
        'source': 'list[str]',
        'total_vuln_count': 'int',
        'users': 'list[str]',
        'instrumentation_state': 'str',
        'instrumented_from': 'str',
        'is_docker_hub_official': 'bool',
        'is_instrumented': 'bool',
        'scan_type': 'str',
        'scan_error_code': 'str',
        'scan_status': 'str',
        'last_found_on_host': 'Host'
    }

    attribute_map = {
        'created': 'created',
        'updated': 'updated',
        'author': 'author',
        'repo': 'repo',
        'repo_digests': 'repoDigests',
        'label': 'label',
        'uuid': 'uuid',
        'sha': 'sha',
        'operating_system': 'operatingSystem',
        'customer_uuid': 'customerUuid',
        'docker_version': 'dockerVersion',
        'size': 'size',
        'layers': 'layers',
        'host': 'host',
        'architecture': 'architecture',
        'image_id': 'imageId',
        'registry_uuid': 'registryUuid',
        'source': 'source',
        'total_vuln_count': 'totalVulnCount',
        'users': 'users',
        'instrumentation_state': 'instrumentationState',
        'instrumented_from': 'instrumentedFrom',
        'is_docker_hub_official': 'isDockerHubOfficial',
        'is_instrumented': 'isInstrumented',
        'scan_type': 'scanType',
        'scan_error_code': 'scanErrorCode',
        'scan_status': 'scanStatus',
        'last_found_on_host': 'lastFoundOnHost'
    }

    def __init__(self, created=None, updated=None, author=None, repo=None, repo_digests=None, label=None, uuid=None, sha=None, operating_system=None, customer_uuid=None, docker_version=None, size=None, layers=None, host=None, architecture=None, image_id=None, registry_uuid=None, source=None, total_vuln_count=None, users=None, instrumentation_state=None, instrumented_from=None, is_docker_hub_official=None, is_instrumented=None, scan_type=None, scan_error_code=None, scan_status=None, last_found_on_host=None):  # noqa: E501
        """ImageDetails - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._updated = None
        self._author = None
        self._repo = None
        self._repo_digests = None
        self._label = None
        self._uuid = None
        self._sha = None
        self._operating_system = None
        self._customer_uuid = None
        self._docker_version = None
        self._size = None
        self._layers = None
        self._host = None
        self._architecture = None
        self._image_id = None
        self._registry_uuid = None
        self._source = None
        self._total_vuln_count = None
        self._users = None
        self._instrumentation_state = None
        self._instrumented_from = None
        self._is_docker_hub_official = None
        self._is_instrumented = None
        self._scan_type = None
        self._scan_error_code = None
        self._scan_status = None
        self._last_found_on_host = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if author is not None:
            self.author = author
        if repo is not None:
            self.repo = repo
        if repo_digests is not None:
            self.repo_digests = repo_digests
        if label is not None:
            self.label = label
        if uuid is not None:
            self.uuid = uuid
        if sha is not None:
            self.sha = sha
        if operating_system is not None:
            self.operating_system = operating_system
        if customer_uuid is not None:
            self.customer_uuid = customer_uuid
        if docker_version is not None:
            self.docker_version = docker_version
        if size is not None:
            self.size = size
        if layers is not None:
            self.layers = layers
        if host is not None:
            self.host = host
        if architecture is not None:
            self.architecture = architecture
        if image_id is not None:
            self.image_id = image_id
        if registry_uuid is not None:
            self.registry_uuid = registry_uuid
        if source is not None:
            self.source = source
        if total_vuln_count is not None:
            self.total_vuln_count = total_vuln_count
        if users is not None:
            self.users = users
        if instrumentation_state is not None:
            self.instrumentation_state = instrumentation_state
        if instrumented_from is not None:
            self.instrumented_from = instrumented_from
        if is_docker_hub_official is not None:
            self.is_docker_hub_official = is_docker_hub_official
        if is_instrumented is not None:
            self.is_instrumented = is_instrumented
        if scan_type is not None:
            self.scan_type = scan_type
        if scan_error_code is not None:
            self.scan_error_code = scan_error_code
        if scan_status is not None:
            self.scan_status = scan_status
        if last_found_on_host is not None:
            self.last_found_on_host = last_found_on_host

    @property
    def created(self):
        """Gets the created of this ImageDetails.  # noqa: E501


        :return: The created of this ImageDetails.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ImageDetails.


        :param created: The created of this ImageDetails.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this ImageDetails.  # noqa: E501


        :return: The updated of this ImageDetails.  # noqa: E501
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ImageDetails.


        :param updated: The updated of this ImageDetails.  # noqa: E501
        :type: str
        """

        self._updated = updated

    @property
    def author(self):
        """Gets the author of this ImageDetails.  # noqa: E501


        :return: The author of this ImageDetails.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this ImageDetails.


        :param author: The author of this ImageDetails.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def repo(self):
        """Gets the repo of this ImageDetails.  # noqa: E501


        :return: The repo of this ImageDetails.  # noqa: E501
        :rtype: list[Repo]
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        """Sets the repo of this ImageDetails.


        :param repo: The repo of this ImageDetails.  # noqa: E501
        :type: list[Repo]
        """

        self._repo = repo

    @property
    def repo_digests(self):
        """Gets the repo_digests of this ImageDetails.  # noqa: E501


        :return: The repo_digests of this ImageDetails.  # noqa: E501
        :rtype: list[RepoDigest]
        """
        return self._repo_digests

    @repo_digests.setter
    def repo_digests(self, repo_digests):
        """Sets the repo_digests of this ImageDetails.


        :param repo_digests: The repo_digests of this ImageDetails.  # noqa: E501
        :type: list[RepoDigest]
        """

        self._repo_digests = repo_digests

    @property
    def label(self):
        """Gets the label of this ImageDetails.  # noqa: E501


        :return: The label of this ImageDetails.  # noqa: E501
        :rtype: list[BulkContainerDetailsLabel]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ImageDetails.


        :param label: The label of this ImageDetails.  # noqa: E501
        :type: list[BulkContainerDetailsLabel]
        """

        self._label = label

    @property
    def uuid(self):
        """Gets the uuid of this ImageDetails.  # noqa: E501


        :return: The uuid of this ImageDetails.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ImageDetails.


        :param uuid: The uuid of this ImageDetails.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def sha(self):
        """Gets the sha of this ImageDetails.  # noqa: E501


        :return: The sha of this ImageDetails.  # noqa: E501
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this ImageDetails.


        :param sha: The sha of this ImageDetails.  # noqa: E501
        :type: str
        """

        self._sha = sha

    @property
    def operating_system(self):
        """Gets the operating_system of this ImageDetails.  # noqa: E501


        :return: The operating_system of this ImageDetails.  # noqa: E501
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this ImageDetails.


        :param operating_system: The operating_system of this ImageDetails.  # noqa: E501
        :type: str
        """

        self._operating_system = operating_system

    @property
    def customer_uuid(self):
        """Gets the customer_uuid of this ImageDetails.  # noqa: E501


        :return: The customer_uuid of this ImageDetails.  # noqa: E501
        :rtype: str
        """
        return self._customer_uuid

    @customer_uuid.setter
    def customer_uuid(self, customer_uuid):
        """Sets the customer_uuid of this ImageDetails.


        :param customer_uuid: The customer_uuid of this ImageDetails.  # noqa: E501
        :type: str
        """

        self._customer_uuid = customer_uuid

    @property
    def docker_version(self):
        """Gets the docker_version of this ImageDetails.  # noqa: E501


        :return: The docker_version of this ImageDetails.  # noqa: E501
        :rtype: str
        """
        return self._docker_version

    @docker_version.setter
    def docker_version(self, docker_version):
        """Sets the docker_version of this ImageDetails.


        :param docker_version: The docker_version of this ImageDetails.  # noqa: E501
        :type: str
        """

        self._docker_version = docker_version

    @property
    def size(self):
        """Gets the size of this ImageDetails.  # noqa: E501


        :return: The size of this ImageDetails.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ImageDetails.


        :param size: The size of this ImageDetails.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def layers(self):
        """Gets the layers of this ImageDetails.  # noqa: E501


        :return: The layers of this ImageDetails.  # noqa: E501
        :rtype: list[Layer]
        """
        return self._layers

    @layers.setter
    def layers(self, layers):
        """Sets the layers of this ImageDetails.


        :param layers: The layers of this ImageDetails.  # noqa: E501
        :type: list[Layer]
        """

        self._layers = layers

    @property
    def host(self):
        """Gets the host of this ImageDetails.  # noqa: E501


        :return: The host of this ImageDetails.  # noqa: E501
        :rtype: list[Host]
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ImageDetails.


        :param host: The host of this ImageDetails.  # noqa: E501
        :type: list[Host]
        """

        self._host = host

    @property
    def architecture(self):
        """Gets the architecture of this ImageDetails.  # noqa: E501


        :return: The architecture of this ImageDetails.  # noqa: E501
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this ImageDetails.


        :param architecture: The architecture of this ImageDetails.  # noqa: E501
        :type: str
        """

        self._architecture = architecture

    @property
    def image_id(self):
        """Gets the image_id of this ImageDetails.  # noqa: E501


        :return: The image_id of this ImageDetails.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ImageDetails.


        :param image_id: The image_id of this ImageDetails.  # noqa: E501
        :type: str
        """

        self._image_id = image_id

    @property
    def registry_uuid(self):
        """Gets the registry_uuid of this ImageDetails.  # noqa: E501


        :return: The registry_uuid of this ImageDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._registry_uuid

    @registry_uuid.setter
    def registry_uuid(self, registry_uuid):
        """Sets the registry_uuid of this ImageDetails.


        :param registry_uuid: The registry_uuid of this ImageDetails.  # noqa: E501
        :type: list[str]
        """

        self._registry_uuid = registry_uuid

    @property
    def source(self):
        """Gets the source of this ImageDetails.  # noqa: E501


        :return: The source of this ImageDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ImageDetails.


        :param source: The source of this ImageDetails.  # noqa: E501
        :type: list[str]
        """

        self._source = source

    @property
    def total_vuln_count(self):
        """Gets the total_vuln_count of this ImageDetails.  # noqa: E501


        :return: The total_vuln_count of this ImageDetails.  # noqa: E501
        :rtype: int
        """
        return self._total_vuln_count

    @total_vuln_count.setter
    def total_vuln_count(self, total_vuln_count):
        """Sets the total_vuln_count of this ImageDetails.


        :param total_vuln_count: The total_vuln_count of this ImageDetails.  # noqa: E501
        :type: int
        """

        self._total_vuln_count = total_vuln_count

    @property
    def users(self):
        """Gets the users of this ImageDetails.  # noqa: E501


        :return: The users of this ImageDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this ImageDetails.


        :param users: The users of this ImageDetails.  # noqa: E501
        :type: list[str]
        """

        self._users = users

    @property
    def instrumentation_state(self):
        """Gets the instrumentation_state of this ImageDetails.  # noqa: E501


        :return: The instrumentation_state of this ImageDetails.  # noqa: E501
        :rtype: str
        """
        return self._instrumentation_state

    @instrumentation_state.setter
    def instrumentation_state(self, instrumentation_state):
        """Sets the instrumentation_state of this ImageDetails.


        :param instrumentation_state: The instrumentation_state of this ImageDetails.  # noqa: E501
        :type: str
        """

        self._instrumentation_state = instrumentation_state

    @property
    def instrumented_from(self):
        """Gets the instrumented_from of this ImageDetails.  # noqa: E501


        :return: The instrumented_from of this ImageDetails.  # noqa: E501
        :rtype: str
        """
        return self._instrumented_from

    @instrumented_from.setter
    def instrumented_from(self, instrumented_from):
        """Sets the instrumented_from of this ImageDetails.


        :param instrumented_from: The instrumented_from of this ImageDetails.  # noqa: E501
        :type: str
        """

        self._instrumented_from = instrumented_from

    @property
    def is_docker_hub_official(self):
        """Gets the is_docker_hub_official of this ImageDetails.  # noqa: E501


        :return: The is_docker_hub_official of this ImageDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_docker_hub_official

    @is_docker_hub_official.setter
    def is_docker_hub_official(self, is_docker_hub_official):
        """Sets the is_docker_hub_official of this ImageDetails.


        :param is_docker_hub_official: The is_docker_hub_official of this ImageDetails.  # noqa: E501
        :type: bool
        """

        self._is_docker_hub_official = is_docker_hub_official

    @property
    def is_instrumented(self):
        """Gets the is_instrumented of this ImageDetails.  # noqa: E501


        :return: The is_instrumented of this ImageDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_instrumented

    @is_instrumented.setter
    def is_instrumented(self, is_instrumented):
        """Sets the is_instrumented of this ImageDetails.


        :param is_instrumented: The is_instrumented of this ImageDetails.  # noqa: E501
        :type: bool
        """

        self._is_instrumented = is_instrumented

    @property
    def scan_type(self):
        """Gets the scan_type of this ImageDetails.  # noqa: E501


        :return: The scan_type of this ImageDetails.  # noqa: E501
        :rtype: str
        """
        return self._scan_type

    @scan_type.setter
    def scan_type(self, scan_type):
        """Sets the scan_type of this ImageDetails.


        :param scan_type: The scan_type of this ImageDetails.  # noqa: E501
        :type: str
        """

        self._scan_type = scan_type

    @property
    def scan_error_code(self):
        """Gets the scan_error_code of this ImageDetails.  # noqa: E501


        :return: The scan_error_code of this ImageDetails.  # noqa: E501
        :rtype: str
        """
        return self._scan_error_code

    @scan_error_code.setter
    def scan_error_code(self, scan_error_code):
        """Sets the scan_error_code of this ImageDetails.


        :param scan_error_code: The scan_error_code of this ImageDetails.  # noqa: E501
        :type: str
        """

        self._scan_error_code = scan_error_code

    @property
    def scan_status(self):
        """Gets the scan_status of this ImageDetails.  # noqa: E501


        :return: The scan_status of this ImageDetails.  # noqa: E501
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        """Sets the scan_status of this ImageDetails.


        :param scan_status: The scan_status of this ImageDetails.  # noqa: E501
        :type: str
        """

        self._scan_status = scan_status

    @property
    def last_found_on_host(self):
        """Gets the last_found_on_host of this ImageDetails.  # noqa: E501


        :return: The last_found_on_host of this ImageDetails.  # noqa: E501
        :rtype: Host
        """
        return self._last_found_on_host

    @last_found_on_host.setter
    def last_found_on_host(self, last_found_on_host):
        """Sets the last_found_on_host of this ImageDetails.


        :param last_found_on_host: The last_found_on_host of this ImageDetails.  # noqa: E501
        :type: Host
        """

        self._last_found_on_host = last_found_on_host

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
        if issubclass(ImageDetails, dict):
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
        if not isinstance(other, ImageDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
