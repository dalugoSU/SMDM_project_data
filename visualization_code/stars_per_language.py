import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# Env vars
CSV_PATH = "pulled_repos.csv"
SEP = ','
COL_NAMES = ["RepoID",
            "Name",
            "Type",
            "Topics",
            "Visibility",
            "Language",
            "Published",
            "Last_Modified",
            "Stars",
            "Forks",
            "WatchCount",
            "NetworkCount",
            "IssueCount",
            "PRCount",
            "ProjectsCount",
            "BranchCount",
            "DownloadCount",
            "ContributorCount",
            "RepoURL"]

# Pull CSV to DF
main_data = pd.read_csv(CSV_PATH, sep=SEP, names=COL_NAMES)

# SANITIZING $

# Remove duplicates
main_data = main_data.drop_duplicates()

# convert 'Published' column to datetime format
main_data['Published'] = pd.to_datetime(main_data['Published'])

# extract year from the 'Published' column
main_data['Published'] = main_data['Published'].dt.year

# Fill NaN's
main_data['Published'] = main_data['Published'].fillna(0).astype(int)
main_data['ProjectsCount'] = main_data['ProjectsCount'].fillna(0).astype(int)

# Drop rows with no language val since that is what we care about
main_data.dropna(subset=['Language'], inplace=True)

# NUMBER OF STARS PER LANGUAGE #

# group by 'Language' and sum up the 'Stars' column for each group
stars_per_language = main_data.groupby('Language')['Stars'].sum().reset_index().sort_values(by='Stars', ascending=False)

# create bar plot
fig, ax = plt.subplots(figsize=(25, 15))

ax.bar(stars_per_language['Language'], stars_per_language['Stars'])

# add labels and title
ax.set_xlabel('Language')
ax.set_ylabel('Number of stars')
ax.set_title('Number of stars per language')

# add bar values to the plot
for i, v in enumerate(stars_per_language['Stars']):
    ax.text(i, v, str(v), ha='center', va='bottom')
    
# rotate x-axis labels by 45 degrees
plt.xticks(rotation=60)

# display plot
plt.show()



