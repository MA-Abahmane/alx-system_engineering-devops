#!/usr/bin/python3
"""
    Using I did in the task #0, I will extend my Python
    script to export data in the JSON format.
 """

import json
import requests
from sys import argv


def get_TODO():
    """
        A python function that takes in a worker id
        and saves all his info to a .json file
    """

    # GET worker name uning his ID
    usersURL = "https://jsonplaceholder.typicode.com/users"

    i = 1
    while (i < 11):
        # looping trough users
        userID = str(i)

        response = requests.get(usersURL + '/' + userID)
        userName = response.json().get('username')

        # GET workers mission list
        response = requests.get(usersURL + '/' + userID + '/todos')
        todoData = response.json()

        # LOAD string from json file to a Python dictionary
        with open('todo_all_employees.json', 'r') as F:
            try:
                _dict = json.load(F)
            except Exception:
                _dict = {}

        # Manage records, save to dictionary and save to .json file
        with open('todo_all_employees.json', 'w') as Fl:
            _dict[userID] = []
            for task in todoData:
                _dict[userID].append({"username": f"{userName}",
                                      "task": f"{task['title']}",
                                      "completed": task['completed']})
            json.dump(_dict, Fl)

        i += 1


if __name__ == "__main__":
    """ Run only when the module is ran """

    get_TODO()
