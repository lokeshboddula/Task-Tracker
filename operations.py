import datetime
import os
import re
import json

curr_datetime = datetime.datetime.now()
file_path = 'data.json'

def add(description):

    data = {}

    if not os.path.exists(file_path):
        # Create the file with some default data (e.g., an empty dictionary)
        with open(file_path, 'w') as file:
            json.dump([], file)

    with open(file_path, 'r') as file:
        file_data = json.load(file)

    data['id'] = len(file_data) + 1
    data['description'] = description
    data['status'] = 'todo'
    data['createdAt'] = str(curr_datetime)
    data['updatedAt'] = str(curr_datetime)
    
    file_data.append(data)

    with open(file_path, 'w') as file:
        json.dump(file_data, file, indent=4)


def update(task_id, status, description):

    with open(file_path, 'r') as file:
        file_data = json.load(file)

    flag = False
    for dict_at_index in file_data:
        if dict_at_index['id'] == task_id:
            dict_at_index['description'] = description
            dict_at_index['status'] = status
            dict_at_index['updatedAt'] = str(curr_datetime)
            flag = True
            break

    if not flag:
        print("No data found for given Id :", task_id)

    with open(file_path, 'w') as file:
        json.dump(file_data, file, indent=4)


def list_tasks(status=None):

    with open(file_path, 'r') as file:
        file_data = json.load(file)

    tasks = file_data
    if status:
        tasks = [t for t in tasks if t['status'] == status]
    for task in tasks:
        print(
            f"ID: {task['id']}, Status: {task['status']}, Description: {task['description']}")


def delete(task_id):

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
