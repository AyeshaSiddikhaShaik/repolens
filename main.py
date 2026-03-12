from github_data import get_repo_data

repo = input("Enter GitHub repository (owner/repo): ")

data = get_repo_data(repo)

if data is None:
    print("Repository not found.")
    exit()

print("\nRepository Information")
print("----------------------")
print("Name:", data["name"])
print("Owner:", data["owner"])
print("Stars:", data["stars"])
print("Forks:", data["forks"])
print("Language:", data["language"])
print("Open Issues:", data["issues"])

print("\nProject Insight")
print("----------------")

if data["stars"] > 50000:
    print("This is a very popular open-source project.")
elif data["stars"] > 10000:
    print("This project has strong community support.")
else:
    print("This is a smaller or growing repository.")
