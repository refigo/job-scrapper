import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}&radius=25"

def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class":"pagination"})
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page

def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page):
    result = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all('a', {"class":"tapItem"})
    for result in results:
        spans = result.find_all("span")
        i = 0
        if spans[0].string == "new": i = i + 1
        title = spans[i].string
        print(title, end=' # ')
        company = spans[i + 1].string
        print(company, end=' # ')
        location = result.find("div", {"class":"companyLocation"}).string
        print(location)
    return jobs

        
