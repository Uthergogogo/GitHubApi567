"""
HW04a
@Author: Zeyu Wu
Date: 2020-02-18 16:34:55
"""
import requests


def parsing_link(user_name):
    """ parse the given link"""
    link_repo = "https://api.github.com/users/{}/repos".format(user_name)
    repo_name = []
    result = []
    r = requests.get(link_repo).json()
    if type(r) == dict:
        if "message" in r.keys():
            if r["message"] == "Not Found":
                print("Invalid Id entered!")
                exit()
    if len(r) == 0:
        print("The user doesn't have any repository")
        exit()
    for i in range(len(r)):
        repo_name.append(r[i]["name"])
    for item in repo_name:
        link_commit = "https://api.github.com/repos/{}/{}/commits".format(user_name, item)
        result.append(f"Repo: {item} Number of commits: {len(requests.get(link_commit).json())}")
        print(f"Repo: {item} Number of commits: {len(requests.get(link_commit).json())}")
    return result


def main():
    """ run the code """
    user_name = input("Please enter the ID:")
    parsing_link(user_name)


if __name__ == '__main__':
    main()
