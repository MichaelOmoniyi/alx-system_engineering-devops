#!/usr/bin/python3
"""
This script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

employeeId = sys.argv[1]
url = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":
    users = requests.get(url + "users/{}".format(employeeId)).json()
    todos = requests.get(url + "todos?userId={}".format(employeeId)).json()
    completed = [todo.get("title") for todo in todos if todo.get("completed") is True]
    todoLength = len(todos)
    print("Employee {} is done with tasks({}/{}):".format(
          users.get("name"), len(completed), todoLength))
    for complete in completed:
        print("\t {}".format(complete))
