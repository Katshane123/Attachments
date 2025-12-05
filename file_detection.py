# Python file detection 

import os 
 # relative file detection
file_path = "car.txt"

if os.path.exists(file_path):
    print(f'The location {file_path} exists')
else: 
    print('That location does not exist')
