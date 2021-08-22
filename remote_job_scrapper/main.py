import wwr
import remoteok
import so
from flask import Flask, render_template, request, redirect, send_file
from save import save_to_file


db = {}

app = Flask("JobScrapper")

@app.route("/export")
def export():
  try:
    word = request.args.get("word")
    print(word)
    if not word:
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    save_to_file(jobs)
    return send_file("jobs.csv", attachment_filename='jobs.csv', as_attachment=True)
  except:
    return redirect("/")

def get_jobs(word):
  if db.get(word):
    return db[word]
  jobs = []
  try:
    jobs += wwr.get_jobs(word)
    jobs += so.get_jobs(word)
    jobs += remoteok.get_jobs(word)
  except:
    pass
  db[word] = jobs
  return jobs

@app.route("/search")
def seach_jobs():
  word = request.args.get("term")
  if word:
    word = word.lower()
    jobs = get_jobs(word)
  else :
    return redirect("/")
  return render_template("search.html", word=word, count=len(jobs), jobs=jobs)

@app.route("/")
def home():
  return render_template("home.html")

app.run(host="0.0.0.0")
