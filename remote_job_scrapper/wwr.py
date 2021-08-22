import requests
from bs4 import BeautifulSoup


def get_jobs(word):
  url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
  r_wwr = requests.get(url, headers=headers)
  soup_wwr = BeautifulSoup(r_wwr.text, "html.parser")
  job_sections = soup_wwr.find("div", {"class":"jobs-container"}).find_all("section", {"class":"jobs"})
  jobs = []
  for section in job_sections:
    job_lis = section.find("ul").find_all("li")
    for job_li in job_lis:
      """
      if job_li["class"]:
        if job_li["class"][0] == "view-all":
          continue
      """
      try:
        job_a = job_li.find_all("a", href=True)[1]
      except:
        continue
      job_title = job_a.find("span", {"class":"title"}).get_text()
      job_company = job_a.find("span", {"class":"company"}).get_text()
      job_link = f"https://weworkremotely.com{job_a['href']}"
      jobs.append({"title":job_title, "company":job_company, "link":job_link})
  return jobs
  
def init():
  get_jobs("python")
