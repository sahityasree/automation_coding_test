from github import Github
from subprocess import check_output
# First create a Github instance:

# using username and password
g = Github("sahitya.sreebhashyam@gmail.com", "Sahitya@05")


for repo in g.get_user().get_repos():
    print(repo.name)
    if(repo.name=="automation_coding_test"):
        c=list(repo.get_branches())
        #print("repo",repo.append(c[1]))
        print(c)
        print("latest branch with pull request:",c[-1])
        pulls = list(repo.get_pulls())
        print(pulls)
        print("latest pull request with branch",pulls[0])
        p = list(pulls[0].get_commits())
        print("latest commit on branch",p[-1])
        env.GIT_BRANCH=c[-1]
