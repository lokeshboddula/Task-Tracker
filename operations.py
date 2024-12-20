import datetime
import os
import re
import json

curr_datetime = datetime.datetime.now()
file_path = 'data.json'
description_pattern = r"(['\"])(.*?)\1"
update_format_pattern = r"^update (\d+) \"(.*?)\"$"

def add(task):

    data = {}

    if not os.path.exists(file_path):
        # Create the file with some default data (e.g., an empty dictionary)
        with open(file_path, 'w') as file:
            json.dump([], file)

    with open(file_path, 'r') as file:
        file_data = json.load(file)

    data['id'] = len(file_data) + 1
    data['description'] = re.search(pattern, task).group()[1:-1]
    data['status'] = 'todo'
    data['createdAt'] = str(curr_datetime)
    data['updatedAt'] = str(curr_datetime)
    
    file_data.append(data)

    with open(file_path, 'w') as file:
        json.dump(file_data, file, indent=4)


def update(task):
    if not re.match(update_format_pattern, task):
        print("format error!, expected format: update <id> <description>")
        return

    parts = task.split(' ', 2)

    if len(parts) != 3:
        return "Invalid input format"

    task_id = int(parts[1])
    description = parts[2].strip('"')

    with open(file_path, 'r') as file:
        file_data = json.load(file)

    flag = False
    for dict_at_index in file_data:
        if dict_at_index['id'] == task_id:
            dict_at_index['description'] = description
            dict_at_index['updatedAt'] = str(curr_datetime)
            flag = True
            break

    if not flag:
        print("No data found for given Id :", task_id)

    with open(file_path, 'w') as file:
        json.dump(file_data, file, indent=4)