"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.14.6
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import gitea
from gitea.model.contents_response import ContentsResponse
from gitea.model.file_commit_response import FileCommitResponse
from gitea.model.payload_commit_verification import PayloadCommitVerification
globals()['ContentsResponse'] = ContentsResponse
globals()['FileCommitResponse'] = FileCommitResponse
globals()['PayloadCommitVerification'] = PayloadCommitVerification
from gitea.model.file_response import FileResponse


class TestFileResponse(unittest.TestCase):
    """FileResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFileResponse(self):
        """Test FileResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = FileResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()