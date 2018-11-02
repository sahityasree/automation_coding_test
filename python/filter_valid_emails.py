import re

def check_valid(email):
    try:
        username, url = email.split("@")
        website, extension = url.split(".")
        li=["com","co.in"]
    except ValueError:
        return False
    
    if not username.replace("-", "").replace("_", "").replace(".","").isalnum():
        print("error:username has only .,-,_ charectors")
        return False
    elif len(username) < 4:
        print("error:length of username is atleast 4")
        return False
    elif website.isalnum() is False:
        print("error:website has only letters")
        return False
    elif (extension not in li):
        print("error:extension not valld")
        return False
    elif len(extension) > 3:
        print("error:length of extenson is only 3")
        return False
    elif re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
        return True
       
print("enter count of emails,enter mails untill count")
n = int(input())
emails = [input() for email in range(n)]

valid = list(filter(check_valid, emails))
print("list of valid emails")
print(sorted(valid))