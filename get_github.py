import os

from dotenv import load_dotenv
from github import Github

# Load environment variables
load_dotenv()

# using an access token
github_access_token = os.getenv("GITHUB_ACCESS_TOKEN")
g = Github(github_access_token)

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)