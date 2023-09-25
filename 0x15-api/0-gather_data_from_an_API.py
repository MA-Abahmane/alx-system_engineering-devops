#!/usr/bin/python3
"""
    A Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
 """

import requests
from sys import argv


def get_TODO(userID):
    """
        A python function that takes in a
        worker id and returns his TODO list
    """

    # GET worker name uning his ID
    usersURL = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(usersURL + '/' + userID)
    userName = response.json().get('name')

    # GET workers mission list
    response = requests.get(usersURL + '/' + userID + '/todos')
    todoData = response.json()

    # GET the tasks completed by worker
    tasksCompleat = [task['title'] for task in todoData if task['completed']]

    # Print worker status
    tc = len(tasksCompleat)
    print(f'Employee {userName} is done with tasks({tc}/{len(todoData)}):')

    # Print titles of tasks completed by worker
    for task in tasksCompleat:
        print("\t " + task)


if __name__ == "__main__":
    """ Run only when the module is ran """

    get_TODO(argv[1])
