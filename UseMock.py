"""
Learn to use Mock
@Author: Zeyu Wu
Date: 2020-02-24 16:46:40
"""
import unittest
import HW04a
from unittest import mock


class TestRepo(unittest.TestCase):
    """ test class for GitHub Repo """
    @mock.patch("requests.get")
    def test_repo(self, mock_repo):
        """ test case for correct value """
        mock_repo.return_value.json.return_value = [{"name": "GitHubApi567"}, {"name": "SSW-567"}, {"name": "SSW-810"}, {"name": "Uther567"}, {"name": "UtherTree"}]
        expect = ['Repo: GitHubApi567 Number of commits: 5', 'Repo: SSW-567 Number of commits: 5', 'Repo: SSW-810 Number of commits: 5', 'Repo: Uther567 Number of commits: 5', 'Repo: UtherTree Number of commits: 5']
        result = HW04a.parsing_link('Uthergogogo')
        self.assertEqual(result, expect)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)