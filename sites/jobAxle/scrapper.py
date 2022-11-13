import requests

url = "https://jobaxle.com/search"


def search(
    search_text: str, category_id: str = None, job_location_id: str = None
) -> requests.Response:
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

    response = requests.request(
        "POST",
        url,
        headers=headers,
        data=payload.format(search_text, category_id, job_location_id),
    )
    if response.status_code == 200:
        return response


def check_job_found(response: requests.Response) -> bool:
    # return False is the search page have empty jobs
    found = True
    message = "There are no listings matching your search"
    if message in response.text:
        found = False
    return found


if __name__ == "__main__":
    a = search("asdadjdjd", "a", "c")
    # print(a.text)
    print(check_job_found(a))
