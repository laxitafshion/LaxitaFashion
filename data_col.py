import os
import json

data_path = 'DATA'
file_names = [f for f in os.listdir(data_path) if os.path.isfile(os.path.join(data_path, f))]
with open('data.json', 'w') as file:
    json.dump(file_names, file)
