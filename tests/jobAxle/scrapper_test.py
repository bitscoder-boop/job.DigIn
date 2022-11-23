import unittest
from sites.jobAxle.scrapper import search, check_job_found, get_id_list_of_jobs, take_id_give_response_text, get_job_data
from unittest.mock import patch
from data.data_file import JobData


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
        response_text = "This is the test response message"
        message = "This"
        mock_check_job_found.return_value = False
        got = check_job_found(response_text, message)
        self.assertEqual(False, got)

    @patch('sites.jobAxle.scrapper.get_id_list_of_jobs')
    def test_get_id_list_of_jobs(self, mock_object):
        response_text = open("data/jobAxle/response_text.html")
        want = ["6515", "6567", "6621", "6627"]
        mock_object.return_value = want
        got = get_id_list_of_jobs(response_text)
        self.assertEqual(got, want)
    # // get the data those pages

    @patch('sites.jobAxle.scrapper.requests')
    def test_take_id_give_response_text(self, mock_requests):
        response_text = open("data/jobAxle/specific_job.html")
        mock_requests.get.return_value.status_code = 200
        mock_requests.get.return_value.text = response_text
        got = take_id_give_response_text("6515")
        self.assertEqual(got.status_code, 200)
        self.assertEqual(got.text, response_text)

    @patch('sites.jobAxle.scrapper.get_job_data')
    def test_get_job_data(self, mock_objects):
        response_text = open("data/jobAxle/specific_job.html")
        print(response_text)
        data = {"apply_before": "2022-11-25 (1 Days Left)",
                "company_name": "COTIVITI NEPAL",
                "job_type": "Full Time",
                "level": "Mid Level",
                "location": "Kathmandu",
                "no_of_vacancy": "3",
                "offered_salary": "Negotiable"
                }
        # want = JobData(**data)
        mock_objects.return_value = data
        got = get_job_data(response_text)
        self.assertEqual(got, data)
