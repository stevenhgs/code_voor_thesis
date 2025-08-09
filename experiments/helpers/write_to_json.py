import json
import os.path


def write_to_json(data, path):
    new_path = path
    counter = 0
    while os.path.isfile(new_path):
        counter += 1
        new_path = '.'.join(path.split('.')[:-1]) + str(counter) + '.' + path.split('.')[-1]
    os.makedirs(os.path.dirname(new_path), exist_ok=True)
    with open(new_path, 'w') as file:
        json.dump(data, file, indent=4)
