# Cell contents for dataframe (Prelim)
| Column Name        | Description (Data Type) |
| ------------------ | ---------------------------- |
| RepoID             | RepoID    (Identity for DF) |
| Name               | Repo name (.full_name) |
| Type               | Is it an organization or nah (.raw_data['owner']['type']) |
| Topic              | Topics such as machine-learning, etc... (.topics) |
| Visibility         | Public or private (.visibility) |
| Language(s)        | Languages used in repo (.languages) |
| Published          | When was this repo publised to Github (.created_at) |
| Last Modified      | When was this repo last modified/active (.last_modified) |
| Stars              | How many people have starred this repo (.stargazers_count) |
| Forks              | How many people have forked this repo (.forks) |
| WatchCount         | How many people are watching this repo (.watchers_count) |
| NetworkCount       | How many repos does this repo owner have - *this* repo (.network_count) |
| IssueCount         | How many open issues does this repo have (.open_issues_count) |
| PRCount            | How many pull requests does this repo have (.get_pulls() returns pag PR | objs)
| ProjectsCount      | How many projects are open with this repo (.get_projects() returns pag | Project objs)
| BranchCount        | How many branches does this repo have? (.get_branches() returns pag | branch objs)
| DownloadCount      | How many downloads does this repo have? (.get_downloads() returns pag | project objs)
| ContributorCount   | How many contributors does this repo have? (.get_contributors() returns | objs)
| RepoURL            | Repo URL - Housekeeping (.url) |
