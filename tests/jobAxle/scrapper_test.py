import unittest
from sites.jobAxle.scrapper import search
# from mock import Mock, patch
# from mock import patch
from unittest.mock import patch


class TestSearch(unittest.TestCase):
    @patch('sites.jobAxle.scrapper.requests')
    def test_search_return_status_code_200_on_giving_correct_data(
            self, mock_requests):
        mock_requests.post.return_value.status_code = 200
        keyword = "python"
        response = search(keyword)
        self.assertEqual(response.status_code, 200)


# class TestFormatResponse(unittest.TestCase):
#     def setUp(self):
#         self.response = search("python", '1', '1')
#
#     def test_check_job_found_is_false_if_wrong_parameter_are_passed(self):
#         got = check_job_found(self.response)
#         want = False
#         self.assertEqual(got, want)
