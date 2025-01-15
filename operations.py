import datetime
import os
import re
import json

from pyparsing import empty

curr_datetime = datetime.datetime.now()
file_path = 'data.json'

def add():

    data = {}

    if not os.path.exists(file_path):
        # Create the file with some default data (e.g., an empty dictionary)
        with open(file_path, 'w') as file:
            json.dump([], file)

    with open(file_path, 'r') as file:
        file_data = json.load(file)

    description = input("Enter task description: ").strip()

    data['id'] = len(file_data) + 1
    data['description'] = description
    data['status'] = 'todo'
    data['createdAt'] = str(curr_datetime)
    data['updatedAt'] = str(curr_datetime)
    
    file_data.append(data)
    print("Task added!")
    with open(file_path, 'w') as file:
        json.dump(file_data, file, indent=4)


def update():
    task_id = int(input("Enter task ID to update: "))

    with open(file_path, 'r') as file:
        file_data = json.load(file)

    flag = False
    temp = {}
    for dict_at_index in file_data:
        if dict_at_index['id'] == task_id:
            description = input("Enter the new description: ")
            status = input("Enter new status (todo, in-progress, done): ").strip().lower()

            dict_at_index['description'] = description
            temp['description'] = dict_at_index['description']
            dict_at_index['status'] = status
            temp['status'] = dict_at_index['status']
            dict_at_index['updatedAt'] = str(curr_datetime)
            flag = True
            break

    if not flag:
        print("No data found for given Id :", task_id)
    else:
        print("updated task : ", temp)
    with open(file_path, 'w') as file:
        json.dump(file_data, file, indent=4)


def list_tasks():

    status = input("Enter status to filter by (all, todo, in-progress, done): ").strip().lower()

    with open(file_path, 'r') as file:
        file_data = json.load(file)

    tasks = file_data
    if status:
        tasks = [t for t in tasks if t['status'] == status]
    else:
        tasks = [t for t in tasks]

    if not tasks:
        print("[]")
        return

    for task in tasks:
        print(f"ID: {task['id']}, Status: {task['status']}, Description: {task['description']}")



def delete():

    task_id = int(input("Enter task ID to delete: "))

    with open(file_path, 'r') as file:
        file_data = json.load(file)

    flag = False
    for i, dict_at_index in enumerate(file_data):
        if dict_at_index['id'] == task_id:
            del file_data[i]
            flag = True
            break

    if not flag:
        print("task with id : ", task_id, "not found!")
    else:
        with open(file_path, 'w') as file:
            json.dump(file_data, file, indent=4)
        print(f"Task with id {task_id} deleted successfully.")
