#!/usr/bin/python3
""" export data in the CSV format. """
import requests
import sys

employeeId = sys.argv[1]
url = "https://jsonplaceholder.typicode.com/"
filename = "USER_ID.csv"

if __name__ == "__main__":
    user = requests.get(url + "users/{}".format(employeeId)).json()
    todos = requests.get(url + "todos?userId={}".format(employeeId)).json()
    with open(filename, 'w', encoding="utf-8") as f:
        for task in todos:
            line = "\"{}\",\"{}\",\"{}\",\"{}\"\n".format(task.get("userId"),
                                                          user.get("username"),
                                                          task.get(
                                                              "completed"),
                                                          task.get("title"))
            f.write(line)
