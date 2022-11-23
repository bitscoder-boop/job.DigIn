import requests
from bs4 import BeautifulSoup
from data.data_file import JobData

url = "https://jobaxle.com/search"


def search(
    search_text: str, category_id: str = None, job_location_id: str = None
):
    # return the response object when status code == 200
    payload = "search_text={}&cat_id={}&job_location_id={}"

    headers = {
        "authority": "jobaxle.com",
        "accept-language": "en-US,en;q=0.6",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://jobaxle.com",
        "referer": "https://jobaxle.com/search",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "sec-gpc": "1",
    }

    response = requests.post(
        url,
        headers=headers,
        data=payload.format(search_text, category_id, job_location_id),
    )
    if response.status_code == 200:
        return response


def check_job_found(response_text: requests.Response.text,
                    message: str) -> bool:
    found = True
    if not message:
        message = "There are no listings matching your search"
    if message in response_text:
        found = False
    return found


def get_id_list_of_jobs(response_text: requests.Response.text) -> list:
    id_of_jobs = []
    soup = BeautifulSoup(response_text, 'html.parser')
    job_block = soup.find('div', {'id': 'srch_output'})
    job_ids_block = job_block.find_all(
        'a', {'class': 'show_detail btn_jobview'})
    for i in job_ids_block:
        id_of_jobs.append(i.attrs['data-job_id'])
    return id_of_jobs


def take_id_give_response_text(id: str) -> requests.Response:
    constructed_url = "https://jobaxle.com/jobs/anything-goes-here/" + str(id)
    response = requests.get(constructed_url)
    if response.status_code == 200:
        return response
    return None


def get_job_data(response_text: requests.Response.text) -> JobData:
    soup = BeautifulSoup(response_text, 'html.parser')
    company_name = soup.find(
        'div',
        {'class': "company_description details-content"}).find('h3').text
    job_summary_block = soup.find('ul', {'id': 'jsummary'})
    job_summary_list = job_summary_block.find_all('li')
    no_of_vacancy = job_summary_list[0].span.text.lstrip().rstrip()
    job_type = job_summary_list[1].span.text.lstrip().rstrip()
    offered_salary = job_summary_list[2].span.text.lstrip().rstrip()
    career_level = job_summary_list[4].span.text.lstrip().rstrip()
    # experience = job_summary_list[6].span.text.lstrip().rstrip()
    location = job_summary_list[7].span.text.lstrip().rstrip()
    apply_before = job_summary_list[8].span.text.lstrip().rstrip()
    data = {
        "apply_before": apply_before,
        "company_name": company_name,
        "job_type": job_type,
        "level": career_level,
        "location": location,
        "no_of_vacancy": no_of_vacancy,
        "offered_salary": offered_salary,
        # "experience_required": experience

    }
    # return JobData(**data)
    return data
