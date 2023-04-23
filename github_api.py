import pandas as pd

from github import Github
from csv import writer
from time import sleep


ACCESS_TOKEN = "YOUR ACCESS TOKEN"

# using an access token
g = Github(ACCESS_TOKEN)

count = 0         # Using for rate limit
util_counter = 0  # How many have we pulled?
util_counter_hr = 0
SLEEP_COUNT = 120 # Seconds (Two mins)
SLEEP_COUNT_HOUR = 3600


# Searching for repos created after on and after 2018 (last 5 years)
repo_gen = g.search_repositories(query='created:>2021-01-01')

"""
This loop will keep running until rate limit error
Change the query above in line 21 to change the constraint
I have to counters one counts to 100 and the other to 800
At 100: sleep for 2 mins
At 800: sleep for an hour
"""
while True:
    try:
        for repo in repo_gen:

            if count >= 100:
                sleep(SLEEP_COUNT)
                count = 0
            
            if util_counter_hr == 800:
                sleep(SLEEP_COUNT_HOUR)
                util_counter_hr = 0
            
            # These attributes are only avaiblae through these getters (95% sure)
            repo_type = repo.raw_data['owner']['type']
            repo_pr_count = len([_ for _ in repo.get_pulls()])
            repo_project_count = None
            try:
                repo_project_count = len([_ for _ in repo.get_projects()])
            except Exception as e:
                print("Projects disabled")
            repo_branch_count = len([_ for _ in repo.get_branches()])
            repo_download_count = len([_ for _ in repo.get_downloads()])
            repo_contributor_count = len([_ for _ in repo.get_contributors()])


            # Create a new line for the CSV File
            csv_line = [repo.id,
                        repo.full_name,
                        repo_type,
                        repo.topics,
                        repo.visibility,
                        repo.language,
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

            with open('pulled_repos.csv', 'a') as csv_f:

                # Pass this file object to csv.writer()
                # and get a writer object
                writer_object = writer(csv_f)

                # Pass the list as an argument into
                # the writerow()
                writer_object.writerow(csv_line)
            
            # Increment counters
            util_counter += 1
            util_counter_hr += 1
            count += 1

            print(f"[{util_counter}]: {csv_line}")
            
            # END FOR
        
    except Exception as e:
        print(f"Error occurred: {e}")
        break
