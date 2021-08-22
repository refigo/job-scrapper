import requests
from bs4 import BeautifulSoup


def get_jobs(word):
  url = f"https://remoteok.io/remote-dev+{word}-jobs"
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
  r_rmt = requests.get(url, headers=headers)
  soup_rmt = BeautifulSoup(r_rmt.text, "html.parser")
  jobs_rmt = soup_rmt.find("table", {"id":"jobsboard"}).find_all("tr", {"class":"job"})
  jobs = []
  for job in jobs_rmt:
    job_company = job["data-company"]
    job_link = f"https://remoteok.io{job['data-href']}"
    job_title = job.find("td", {"class":"position"}).find("h2", {"itemprop":"title"}).get_text()
    jobs.append({"title":job_title, "company":job_company, "link":job_link})
  return jobs

def init():
  get_jobs("python")
