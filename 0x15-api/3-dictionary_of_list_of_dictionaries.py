#!/usr/bin/python3
""" Task 3 """
from json import dump
import requests


if __name__ == "__main__":
    users_url = 'https://jsonplaceholder.typicode.com/users'
    users_response = requests.get(users_url).json()

    todo_dict = {}
    for i in users_response:
        user_id = i.get('id')
        username = i.get('username')
        url_todo = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            user_id)
        todo_response = requests.get(url_todo)
        todo_json = todo_response.json()

        task_list = []

        for j in todo_json:
            task_dict = {}
            task_dict['task'] = j.get('title')
            task_dict['completed'] = j.get('completed')
            task_dict['username'] = username
            task_list.append(task_dict)

        todo_dict[user_id] = task_list

    with open('todo_all_employees.json', 'w') as f:
        dump(todo_dict, f)
