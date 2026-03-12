import requests

def get_repo_data(repo):
    url = f"https://api.github.com/repos/{repo}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return None

    return {
        "name": data["name"],
        "owner": data["owner"]["login"],
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
        "language": data["language"],
        "issues": data["open_issues_count"]
    }