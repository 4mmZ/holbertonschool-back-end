#!/usr/bin/python3
""" comments """

import csv
import json
import requests
import sys


if __name__ == '__main__':
    """ """

    full_api = requests.get("https://jsonplaceholder.typicode.com/todos/")

    users_api = requests.get(
        "https://jsonplaceholder.typicode.com/users/")

    text_full_api = full_api.text
    text_users_api = users_api.text
    full_data = json.loads(text_full_api)
    users_data = json.loads(text_users_api)

    all_dict = {}

    for users_id in users_data:
        tasks = []
        for todo in full_data:
            if todo['userId'] == users_id['id']:
                tasks.append({'username': users_id['username'],
                              'task': todo['title'],
                              'completed': todo['completed']})
        all_dict[users_id['id']] = tasks

    filename = "todo_all_employees.json"

    with open(filename, mode='w') as json_file:
        json.dump(all_dict, json_file)
