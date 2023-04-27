# Analysis on Language Popularity on GitHub

## Table of Contents

- [Scope](#scope)
- [Tools](#tools)
- [Installation](#installation)
  - [Preparing Environment](#preparing-environment)
  - [Running The Code](#running-the-code)
- [Development](#development)
  - [Naming Conventions](#naming-conventions) 
  - [Important Note](#important-note)
- [Interactive Tool](#interactive-tool)
  - [Usage](#usage)

> **BEFORE running any code** make sure to read [Important Note](#important-note)

## Scope
1. Collect usage data from both the public and big corporations with open source projects such as Microsoft, Meta, and Twitter.
2. Analyze the collected data and identify trends on popular and non-popular languages over the years. Present the data in a digestible way, such as line graphs, to compare the usage trends of the public with big corporations.
3. Compile a report that will enable people and businesses to answer important questions when deciding on which languages/frameworks to use in their next projects or hiring plans.
4. Investigate which programming languages are growing in popularity and which ones are declining. Identify any significant hike up or decline in a language’s popularity. Investigation of the relationship between programming language popularity and other factors, such as
geographic location.
5. Development of visualizations and dashboards to present the findings of the analysis.

## Tools
1. [Python](https://www.python.org)
2. [PyGithub](https://github.com/PyGithub/PyGithub)
3. [Anaconda](https://www.anaconda.com)
4. [Jupyter](https://jupyter.org)
5. [Interact](https://ipywidgets.readthedocs.io/en/8.0.5/examples/Using%20Interact.html)

## Installation

> All files (notebooks & csv) **MUST** be in the same directory
> Omitting to do so will require you to modify the paths on the notebooks

### Preparing Environment
1. Create a local directory on your computer
2. Install anaconda on your system
3. Download all CSV files for general repos located at generic_repos/collect_data/
4. Download all CSV files for big corporations located at big_companies/collect_data/
5. Download desired statistical analysis from visualization_code/code/ (**NOTE** in [Development](#important-note))
6. generate .env file and place your personal access token.`cp .env.example .env`

### Running The Code
1. Navigate to anaconda and launch Jupyter Notebook
2. Navigate to the directory hosting all your files
3. Open the statistical notebook of your choice and run (**NOTE** in [Development](#important-note))

## Development

### Naming Conventions

All code in visualization_code/code/ has a naming convention. If the file name starts with "corp_" then the statistical notebook is meant to be used with big_companies data. Otherwise, the notebook is meant to be used with generic_repos data.

### Important Note

**Before** running **any** statistical notebook you **MUST** include the code that pulls and sanitizes the data.

- Generic Repos: method_data_processing_cleaning.ipynb
- Big Companies: corp_method_data_processing_cleaning.ipynb

The cells of these files must be **BEFORE** any code in the statistical notebooks provided in the directory.

## Interactive Tool

> **IMPORTANT NOTE** When selecting a year general repos have data for 2018-2022 **ONLY.** Big corporations, however, you can select from 2011 to 2023.

We used interact to an interactive tool to view different statistics on the dataset. For example, users can choose to view the most starred language in 2019. Users can choose to view the top language, top five, and top 10 languages of a specific category. Users also have the capability to view statistics for only general public repositories, big corporation repositories, or both at once. Users can also view data from a specific year or all years at once. Finally, users view data for a specific attribute of repositories. These are the available attribute options: stars, forks, watch count, network count, issue count, pull request count, projects count, branch count, and lastly contributor count. With this tool the main goal is to view quick statistical data either as a data frame or as a graph.

### Usage

1. Have the “data_analysis_interactive,” in your directory
2. Make sure all data set csv files are in the same directory (2018-2022; big companies CSVs)
3. Run all the cells above the interact function to pull and sanitize the data
4. Run interact cell and explore the different options

