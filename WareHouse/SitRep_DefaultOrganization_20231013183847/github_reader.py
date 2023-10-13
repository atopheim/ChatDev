import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read environment variables
github_access_token = os.getenv("GITHUB_ACCESS_TOKEN")
owner = os.getenv("GITHUB_OWNER")
repo = os.getenv("GITHUB_REPO")
email = os.getenv("GITHUB_USER_EMAIL")
name = os.getenv("GITHUB_USER_REAL_NAME")
username = os.getenv("GITHUB_USERNAME")

#  Check if any of the variables are missing
if not github_access_token or not owner or not repo:
    raise ValueError(
        "Please set the GITHUB_ACCESS_TOKEN, GITHUB_OWNER, and GITHUB_REPO environment variables in your .env file."
    )

# Set up the GitHub API request headers
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {github_access_token}",
    "X-GitHub-Api-Version": "2022-11-28",
}


def filter_username(commit, username, name, email):
    if email == commit["commit"]["author"]["email"]:
        return True
    if name.lower() == str(commit["commit"]["author"]["name"]).lower():
        return True
    if str(username) in commit["commit"]["author"]["email"]:
        return True  # sometimes 31770059+<username>@users.noreply.github.com


def get_open_pull_requests(owner, repo, headers):
    # Get a list of open pull requests
    pr_url = f"https://api.github.com/repos/{owner}/{repo}/pulls?state=open"
    response = requests.get(pr_url, headers=headers)

    if response.status_code != 200:
        raise Exception(
            f"Failed to retrieve open pull requests. Status code: {response.status_code}"
        )

    return response.json()


from datetime import datetime, timedelta


def filter_commits_by_date(commits, days):
    today = datetime.today()
    filtered_commits = []

    for commit in commits:
        commit_date = datetime.strptime(
            commit["commit"]["committer"]["date"], "%Y-%m-%dT%H:%M:%SZ"
        )
        if today - commit_date <= timedelta(days=days):
            filtered_commits.append(commit)

    return filtered_commits


def get_commit_messages(owner, repo, pr_number, headers):
    # Get the list of commits for the pull request
    commits_url = (
        f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/commits"
    )
    response = requests.get(commits_url, headers=headers)

    if response.status_code != 200:
        raise Exception(
            f"Failed to retrieve commits for PR #{pr_number}. Status code: {response.status_code}"
        )

    commits = response.json()
    # Filter commits from the last two weeks (14 days)
    last_two_weeks_commits = filter_commits_by_date(commits, days=14)
    return [
        commit["commit"]["message"]
        for commit in commits
        if filter_username(commit, username, name, email)
        and commit in last_two_weeks_commits
    ]


# Create an empty dictionary to store commit messages for open pull requests
pull_requests_commits = {}

# Get the list of open pull requests
open_pull_requests = get_open_pull_requests(owner, repo, headers)

# Iterate through the open pull requests
for pull_request in open_pull_requests:
    pull_request_number = pull_request["number"]
    _commit_msgs = get_commit_messages(owner, repo, pull_request_number, headers)
    if len(_commit_msgs) > 0:
        pull_requests_commits[pull_request_number] = _commit_msgs

# Print or use the dictionary as needed
for pr_number, commit_messages in pull_requests_commits.items():
    print(f"Pull Request #{pr_number} commits:")
    for i, message in enumerate(commit_messages, start=1):
        print(f"{i}. {message}")
    print()

# Now you have a dictionary with commit messages for open pull requests
