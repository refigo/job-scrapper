import requests
from bs4 import BeautifulSoup

LIMIT = 50

def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class":"pagination"})
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page

def extract_job(html):
    spans = html.find_all("span")
    i = 0
    if spans[0].string == "new": i = i + 1
    title = spans[i].string
    company = spans[i + 1].string
    location = html.find("div", {"class":"companyLocation"}).string
    job_id = html["data-jk"]
    return {
        'title': title, 
        'company': company, 
        'location': location,
        'link': f"https://kr.indeed.com/viewjob?jk={job_id}"
        }

def extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping indeed: Page {page+1}")
        result = requests.get(f"{url}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all('a', {"class":"tapItem"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs(word):
    url = f"https://kr.indeed.com/jobs?q={word}&limit={LIMIT}&radius=25"
    last_page = get_last_page(url)
    jobs = extract_jobs(last_page, url)
    return jobs
        
