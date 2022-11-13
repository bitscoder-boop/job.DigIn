import unittest
from sites.jobAxle.scrapper import search, check_job_found


class TestSearch(unittest.TestCase):
    def test_search_return_status_code_200_on_giving_correct_data(self):
        keyword = "python"
        got = search(keyword)
        # retunr status code is 200
        self.assertEqual(got.status_code, 200)


class TestFormatResponse(unittest.TestCase):
    def setUp(self):
        self.response = search("python", '1', '1')

    def test_check_job_found_is_false_if_wrong_parameter_are_passed(self):
        got = check_job_found(self.response)
        want = False
        self.assertEqual(got, want)
