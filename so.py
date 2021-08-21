import requests
from bs4 import BeautifulSoup


def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class":"s-pagination"})
    pages = pagination.find_all('a')
    last_page = int(pages[-2].get_text(strip=True))
    return last_page

def extract_job(html):
    fl1 = html.find("div", {"class":"fl1"})
    title = fl1.find('a')["title"]
    mb4 = fl1.find("h3", {"class":"mb4"})
    company = mb4.find('span').string
    if company:
        company = company.strip()
    else : company = "None"
    location = mb4.find("span", {"class":"fc-black-500"}).string
    location = location.strip()
    job_id = html["data-jobid"]
    return {
        'title': title,
        'company': company,
        'location': location,
        'link': f"https://stackoverflow.com/jobs/{job_id}"
    }

def extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping SO: Page: {page+1}")
        result = requests.get(f"{url}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs(word):
    #url = f"https://stackoverflow.com/jobs?q={word}"
    url = f"https://stackoverflow.com/jobs?r=true&q={word}"
    last_page = get_last_page(url)
    jobs = extract_jobs(last_page, url)
    return jobs
