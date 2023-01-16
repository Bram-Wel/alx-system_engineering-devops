#!/usr/bin/python3
"""Dictionary"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    users = requests.get(
        "https://jsonplaceholder.typicode.com/users")
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos")

    users_json = users.json()
    todos_json = todos.json()
    data_list = {}

    for uid in users_json:
        data_list[str(uid['id'])] = []
        for data in todos_json:
            if uid['id'] == data['userId']:
                data_list[str(uid['id'])].append({"username": uid['username'],
                                                  "completed":
                                                  data['completed'],
                                                  "task":
                                                  data['title']})
    with open('todo_all_employees.json', 'w') as f:
        write = json.dump(data_list, f)
