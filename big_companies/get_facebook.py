import csv
import os

from dotenv import load_dotenv
from github import Github

# Load environment variables
load_dotenv()

# using an access token
github_access_token = os.getenv("GITHUB_ACCESS_TOKEN")
g = Github(github_access_token)

org = g.get_organization("facebook")

for repo in org.get_repos():
    data = [repo.id, repo.name, repo.full_name, repo.raw_data['owner']['type'], repo.topics, repo.visibility,
            repo.language,
            repo.languages_url, repo.created_at, repo.last_modified, repo.stargazers_count, repo.forks,
            repo.watchers_count, repo.network_count, repo.open_issues_count, repo.url]
    # Write to CSV
    with open("collect_data/facebook.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data)
