#!/usr/bin/python3
"""
This script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    filename = "todo_all_employees.json"
    users = requests.get(url + "users/").json()

    with open(filename, "w", encoding="utf-8") as jsonFile:
        json.dump({user.get("id"): [{
            "username": user.get("username"),
            "task": todo.get("title"),
            "completed": todo.get("completed")
            } for todo in requests.get(url + "todos?userId={}".format(
                                       user.get("id"))).json()
            ] for user in users}, jsonFile)
