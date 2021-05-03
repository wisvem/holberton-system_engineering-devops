#!/usr/bin/python3
""" Task 2 """
import requests
from sys import argv
from json import dump

if __name__ == "__main__":
    url_todo = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        argv[1])
    url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    todo_response = requests.get(url_todo)
    user_response = requests.get(url_user)
    todo_json = todo_response.json()
    username = user_response.json().get('username')

    task_list = []
    todo_dict = {}

    for i in todo_json:
        task_dict = {}
        task_dict['task'] = i.get('title')
        task_dict['completed'] = i.get('completed')
        task_dict['username'] = username
        task_list.append(task_dict)

    todo_dict[argv[1]] = task_list

    with open('{}.json'.format(argv[1]), 'w') as f:
        dump(todo_dict, f)
