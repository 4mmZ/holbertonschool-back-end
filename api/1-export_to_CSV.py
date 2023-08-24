#!/usr/bin/python3
""" comments """

import csv
import requests
import sys
import json

if __name__ == '__main__':
    """ """

    "USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE"

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
            tasks.append([str(users_data['id']), users_data['username'], task_status, todo['title']])

    filename = f"{users_data['id']}.csv"

    with open(filename, mode="w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in tasks:
            writer.writerow(task)
