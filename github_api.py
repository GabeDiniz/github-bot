import requests

from decouple import config

GITHUB_TOKEN = config('GITHUB_TOKEN')
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

def get_issues(repo):
  url = f"https://api.github.com/repos/{repo}/issues"
  response = requests.get(url, headers=HEADERS)
  if response.status_code == 200:
    return response.json()
  else:
    print(f"Error: {response.status_code} - {response.text}")
    return []

def get_closed_issues(repo):
  url = f"https://api.github.com/repos/{repo}/issues?state=closed"
  response = requests.get(url, headers=HEADERS)
  if response.status_code == 200:
    return response.json()
  else:
    print(f"Error: {response.status_code} - {response.text}")
    return []
