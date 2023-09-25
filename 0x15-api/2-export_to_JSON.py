#!/usr/bin/python3
"""
    Using I did in the task #0, I will extend my Python
    script to export data in the JSON format.
 """

import requests
import json
from sys import argv


def get_TODO_json(userID):
    """
        A python function that takes in a worker id
        and saves all his info to a .json file
    """

    # GET worker name uning his ID
    usersURL = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(usersURL + '/' + userID)
    userName = response.json().get('username')

    # GET workers mission list
    response = requests.get(usersURL + '/' + userID + '/todos')
    todoData = response.json()

    # GET the tasks completed by worker
    tasksCompleat = [task['title'] for task in todoData if task['completed']]

    # Manage records, save to dictionary and save to .json file
    with open(f'{userID}.json', 'w') as Fl:
        _dict = {userID: []}
        for task in todoData:
            _dict[userID].append({"task": f"{task['title']}",
                                  "completed": task['completed'],
                                  "username": f"{userName}"})
        json.dump(_dict, Fl)


if __name__ == "__main__":
    """ Run only when the module is ran """

    get_TODO_json(argv[1])
