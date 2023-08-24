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
        "https://jsonplaceholder.typicode.com/users/{}/".format(sys.argv[1]))

    text_full_api = full_api.text
    text_users_api = users_api.text
    full_data = json.loads(text_full_api)
    users_data = json.loads(text_users_api)

    tasks = []

    for todo in full_data:
        if todo['userId'] == users_data['id']:
            task_status = "True" if todo['completed'] else "False"
            tasks.append({'task': todo['title'],
                          'completed': task_status,
                          'username': users_data['username']})

    all_dict = {users_data['id']: tasks}

    filename = f"{users_data['id']}.json"

    with open(filename, mode="w", newline='') as json_file:
        json.dump(all_dict, json_file)
