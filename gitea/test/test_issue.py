"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.14.6
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import gitea
from gitea.model.label import Label
from gitea.model.milestone import Milestone
from gitea.model.pull_request_meta import PullRequestMeta
from gitea.model.repository_meta import RepositoryMeta
from gitea.model.user import User
globals()['Label'] = Label
globals()['Milestone'] = Milestone
globals()['PullRequestMeta'] = PullRequestMeta
globals()['RepositoryMeta'] = RepositoryMeta
globals()['User'] = User
from gitea.model.issue import Issue


class TestIssue(unittest.TestCase):
    """Issue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIssue(self):
        """Test Issue"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Issue()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()