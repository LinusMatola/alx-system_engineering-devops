#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    tasks = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    for i in data2:
        if i.get('id') == int(argv[1]):
            EMPLOYEE_NAME = i.get('name')

    for i in data:
        if i.get('userId') == int(argv[1]):
            TOTAL_NUMBER_OF_TASKS += 1

            if i.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                tasks.append(i.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUMBER_OF_TASKS))

    for i in tasks:
        print("\t {}".format(i))
