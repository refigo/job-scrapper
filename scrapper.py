from indeed import get_jobs as get_indeed_jobs 
from so import get_jobs as get_so_jobs
from save import save_to_file

def get_jobs(word):
    #indeed_jobs = get_indeed_jobs(word)
    so_jobs = get_so_jobs(word)
    #jobs = indeed_jobs + so_jobs
    jobs = so_jobs
    save_to_file(jobs)
    return jobs
