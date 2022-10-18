#!/usr/bin/python3
"""Obtains TODO list using this 'https://jsonplaceholder.typicode.com'
REST API and prints to csv file
"""

from sys import argv
import csv
from ast import literal_eval
from urllib.request import urlopen, Request
from urllib.parse import urlencode

if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/'
    try:
        employee_id = {'id': int(argv[1])}
    except (ValueError, IndexError):
        pass
    else:
        employee_id = urlencode(employee_id)
        full_url = url + 'users/' + '?' + employee_id
        req = Request(full_url)
        with urlopen(req) as resp:
            body = resp.read().decode('utf-8')
        body = literal_eval(body)
        name = body[0].get('name')
        employee_id = {'userId': int(argv[1])}
        employee_id = urlencode(employee_id)
        full_url = url + 'todos/' + '?' + employee_id
        req = Request(full_url)
        with urlopen(req) as resp:
            body1 = resp.read().decode('utf-8')
        body1 = body1.replace('false', 'False').replace('true', 'True')
        body1 = literal_eval(body1)

        username = body[0].get('username')
        id = argv[1]
        with open("{}.csv".format(id), 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            [writer.writerow([id, username, task.get('completed'),
                              task.get('title')]) for task in body1]
