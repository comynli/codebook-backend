"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.14.6
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import gitea
from gitea.model.commit_meta import CommitMeta
globals()['CommitMeta'] = CommitMeta
from gitea.model.tag import Tag


class TestTag(unittest.TestCase):
    """Tag unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTag(self):
        """Test Tag"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Tag()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()