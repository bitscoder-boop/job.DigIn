import unittest
from sites.jobAxle.scrapper import search, check_job_found
from unittest.mock import patch


class TestSearch(unittest.TestCase):

    @patch('sites.jobAxle.scrapper.requests')
    def test_search_return_status_code_200_on_giving_correct_data(
            self, mock_requests):
        mock_requests.post.return_value.status_code = 200
        keyword = "python"
        response = search(keyword)
        self.assertEqual(response.status_code, 200)


class TestFormatResponse(unittest.TestCase):

    @patch('sites.jobAxle.scrapper.check_job_found')
    def test_check_job_found_is_false(self, mock_check_job_found):
        # the return value s False when there are no jobs available
        response_text = "This is the test response message"
        # message is the keyword to detect, if it detect keyword
        # than there are no job available
        message = "there"
        mock_check_job_found.return_value = False
        got = check_job_found(response_text, message)
        self.assertEqual(False, got)
