#!/usr/bin/python3
"""
    A Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
 """

from sys import argv
import requests


def get_TODO_csv(userID):
    """
        A python function that takes in a worker id
        and saves all his info to a .csv file
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

    # Manage records, save to string then set to .csv file
    with open(f'{userID}.csv', 'w') as Fl:
        line = ''
        for task in todoData:
            line += f'"{userID}","{userName}",\
                "{task["completed"]}","{task["title"]}"\n'
        Fl.write(line)


if __name__ == "__main__":
    """ Run only when the module is ran """

    get_TODO_csv(argv[1])
