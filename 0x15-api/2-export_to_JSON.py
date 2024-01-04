#!/usr/bin/python3
"""
This script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
import sys

employeeId = sys.argv[1]
url = "https://jsonplaceholder.typicode.com/"
filename = "USER_ID.json"

if __name__ == "__main__":
    user = requests.get(url + "users/{}".format(employeeId)).json()
    todos = requests.get(url + "todos?userId={}".format(employeeId)).json()
    username = user.get("username")

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump({employeeId: [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username} for todo in todos]}, f)
