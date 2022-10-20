import requests

url = "https://jobaxle.com/search"

def search(search_text: str, category_id = '' , job_location_id = ''):
    payload='search_text={}&cat_id={}&job_location_id={}'
    response = requests.post(url, data=payload.format(search_text, category_id, job_location_id))
    if response.status_code == 200:
        print(response.text)


if __name__ == '__main__':
    search('python')
