"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.14.6
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import gitea
from gitea.model.commit_date_options import CommitDateOptions
from gitea.model.identity import Identity
globals()['CommitDateOptions'] = CommitDateOptions
globals()['Identity'] = Identity
from gitea.model.update_file_options import UpdateFileOptions


class TestUpdateFileOptions(unittest.TestCase):
    """UpdateFileOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUpdateFileOptions(self):
        """Test UpdateFileOptions"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UpdateFileOptions()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
