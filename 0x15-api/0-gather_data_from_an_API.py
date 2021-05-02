#!/usr/bin/python3
""" Task 0 """
import requests
from sys import argv


url_todo = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
    argv[1])
url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
todo_response = requests.get(url_todo)
user_response = requests.get(url_user)
todo_json = todo_response.json()
user_name = user_response.json().get('name')

done_list = []
done_count = 0
task_count = 0
for i in todo_json:
    task_count += 1
    if i.get('completed'):
        done_list.append(i.get('title'))
        done_count += 1

td = "{}/{}".format(done_count, task_count)

print("Employee {} is donde with tasks ({}):".format(user_name, td))
for task in done_list:
    print('\t {}'.format(task))
