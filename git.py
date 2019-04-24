from github import Github
from subprocess import check_output
import os

g = Github('169302a41ea470dd78ff7c6cbc4adc5fe04e8b3a')
repo=g.get_repo("sahityasree/automation_coding_test")
print(repo.name)
pulls =list(repo.get_pulls(state='open', sort='created', base='master'))
print("pulls",pulls)
c=list(repo.get_branches())
print("branches",c)
if(pulls):
    p = list(pulls[0].get_commits())
    print("commits on pull requests",p)
    d=str(p[-1]).split("=")[1].strip("()")
    print("latest commit on pull request",d)
    os.env('GIT_COMMIT')=d
    os.env('GIT_BRANCH')=d
else:
    print("no pull requests raised")
