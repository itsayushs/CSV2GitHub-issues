from csv import DictReader
from yaml import safe_load
from github import Github

with open('config.yml', 'r') as config_file:
    config=safe_load(config_file)

BASEURL = config['github_base_url']
TOKEN = config['github_token']
GITHUB_REPO_NAME = config['github_repo_name']

github_client = Github(base_url=BASEURL, login_or_token=TOKEN)

# TestConnection
'''
for repo in github_client.get_user().get_repos():
    print(repo.name)
'''

github_repo = github_client.get_repo(GITHUB_REPO_NAME)


def create_github_issue(issue_title, issue_body, assignee, label1):
    # TODO:Add a label checker 
    # label = github_repo.get_labels()
    # for i in label:
    #     print(i.name)
    return github_repo.create_issue(title=issue_title, body=issue_body, assignee=assignee, labels=[label1])


with open('datasheet.csv', newline='') as csvfile:
    reader = DictReader(csvfile)
    for row in reader:
        print(create_github_issue(row['issue_title'], row['issue_body'], row['assignee'], row['label1']))
        