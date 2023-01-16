#!/usr/bin/python3
"""Fetch data from an API"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    users = requests.get(
        "https://jsonplaceholder.typicode.com/users?id=" + argv[1])
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1])

    users_json = users.json()
    todos_json = todos.json()
    data_list = {str(argv[1]): [], }
    employee_name = users_json[0]['username']

    with open(str(argv[1])+'.json', 'w') as f:
        for data in todos_json:
            data_list[str(argv[1])].append({"username": str(employee_name),
                                            "completed": data['completed'],
                                            "task": data['title']})
        write = json.dump(data_list, f)
