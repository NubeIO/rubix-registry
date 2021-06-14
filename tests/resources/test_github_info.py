import unittest

from registry.models.model_github_info import GitHubInfoModel
from registry.resources.resource_github_info import get_github_info_dict, put_github_info


class TestUtils(unittest.TestCase):

    def test_put_github_info(self):
        github_info = put_github_info(GitHubInfoModel(token=""))
        print(github_info)

    def test_get_github_info(self):
        github_info = get_github_info_dict()
        print(github_info)
