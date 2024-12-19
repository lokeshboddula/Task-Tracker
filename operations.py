import datetime
import re
import json

curr_datetime = datetime.datetime.now()
file_path = 'data.json'
pattern = r"(['\"])(.*?)\1"

def add(task):

    data = {}


    with open('data.json', 'r') as file:
        file_data = json.load(file)

    data['id'] = len(file_data) + 1
    data['description'] = re.search(pattern, task).group()[1:-1]
    data['status'] = 'todo'
    data['createdAt'] = str(curr_datetime)
    data['updatedAt'] = str(curr_datetime)
    
    file_data.append(data)

    with open(file_path, 'w') as file:
        json.dump(file_data, file, indent=4)
