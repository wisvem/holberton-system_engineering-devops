#!/usr/bin/python3
""" Task 1 """
import requests
from sys import argv

if __name__ == "__main__":
    url_todo = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        argv[1])
    url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    todo_response = requests.get(url_todo)
    user_response = requests.get(url_user)
    todo_json = todo_response.json()
    username = user_response.json().get('username')

    task_list = []

    for i in todo_json:
        tmp = "\"{}\",\"{}\",\"{}\",\"{}\"\n".format(
            i.get('userId'), username, i.get('completed'), i.get('title'))
        print(tmp)
        task_list.append(tmp)

    with open('USER_ID.csv', 'w') as f:
        for i in task_list:
            f.writelines(i)
