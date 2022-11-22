import requests
from bs4 import BeautifulSoup

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
