# coding: utf-8

"""
    Container Security API

    # Authentication You must authenticate to the Qualys Cloud Platform using Qualys account credentials (user name and password) and get the JSON Web Token (JWT) before you can start using the Container Security APIs. Use the Qualys Authentication API to get the JWT.  **Example Authentication Curl Request**:  curl -X POST https://gateway/auth -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=value1&password=passwordValue&token=true' where - gateway is the base URL to the Qualys API server where your account is located. - **username** and **password** are the credentials of the user account for which you want to fetch Container Security data. - **token** should be **true** - **Content-Type** should be **application/x-www-form-urlencoded**   # noqa: E501

    OpenAPI spec version: v1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.schedule_repo_tags import ScheduleRepoTags  # noqa: E501
from swagger_client.rest import ApiException


class TestScheduleRepoTags(unittest.TestCase):
    """ScheduleRepoTags unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testScheduleRepoTags(self):
        """Test ScheduleRepoTags"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.schedule_repo_tags.ScheduleRepoTags()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
