import csv
import os

from dotenv import load_dotenv
from github import Github

# Load environment variables
load_dotenv()

# using an access token
github_access_token = os.getenv("GITHUB_ACCESS_TOKEN")
g = Github(github_access_token)

query = 'is:public stars:>100 created:2021'

# continue from the breakpoint
for repo in g.search_repositories(query=query, sort='forks', order='desc')[0:]:

    repo_type = repo.raw_data['owner']['type']

    try:
        repo_pr_count = repo.get_pulls().totalCount
    except Exception as e:
        print(f"Pull Error occurred: {e}")
        repo_pr_count = -1

    try:
        repo_project_count = repo.get_projects().totalCount
    except Exception as e:
        print(f"Project Error occurred: {e}")
        repo_project_count = -1

    try:
        repo_branch_count = repo.get_branches().totalCount
    except Exception as e:
        print(f"Branch Error occurred: {e}")
        repo_branch_count = -1

    try:
        repo_download_count = repo.get_downloads().totalCount
    except Exception as e:
        print(f"Download Error occurred: {e}")
        repo_download_count = -1

    try:
        repo_contributor_count = repo.get_contributors().totalCount
    except Exception as e:
        print(f"Contributors Error occurred: {e}")
        repo_contributor_count = -1

    data = [repo.id,
            repo.full_name,
            repo_type,
            repo.topics,
            repo.visibility,
            repo.language,
            repo.languages_url,
            repo.created_at,
            repo.last_modified,
            repo.stargazers_count,
            repo.forks,
            repo.watchers_count,
            repo.network_count,
            repo.open_issues_count,
            repo_pr_count,
            repo_project_count,
            repo_branch_count,
            repo_download_count,
            repo_contributor_count,
            repo.url]
    # Write to CSV
    with open("collect_data/2021.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data)
