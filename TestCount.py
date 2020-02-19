from HW04a import parsing_link
import unittest


class TestCount(unittest.TestCase):
    """ class to test the number of commit """
    def test_number(self):
        """ test whether get the correct amount of the commit """
        self.assertEqual(parsing_link("Uthergogogo"), ['Repo: GitHubApi567 Number of commits: 6', 'Repo: SSW-567 Number of commits: 2', 'Repo: SSW-810 Number of commits: 1', 'Repo: Uther567 Number of commits: 8', 'Repo: UtherTree Number of commits: 2'])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
