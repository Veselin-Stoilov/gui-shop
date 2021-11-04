import json

import os

from global_constants import *


def register(username, password, firs_name, last_name):

    users_path = os.path.join(DB_FOLDER_NAME, USERS_FILE_NAME)

    with open(users_path, 'r+') as file:
        for user_line in file:
            user = json.loads(user_line.strip())['username']
            if user == username:
                return False

        user_obj = {
            'username': username,
            'password': password,
            'firstName': firs_name,
            'lastName': last_name,
        }

        file.write(json.dumps(user_obj))
        file.write('\n')
        return True


def login(username, password):
    users_path = os.path.join(DB_FOLDER_NAME, USERS_FILE_NAME)
    current_user_path = os.path.join(DB_FOLDER_NAME, SESSION_FILE_NAME)

    with open(users_path, 'r') as users, open(os.path.join(current_user_path), 'w') as session:
        for user_line in users:
            user = json.loads(user_line.strip())['username']
            user_password = json.loads(user_line.strip())['password']
            if user == username and user_password == password:
                session.write(user_line)
                return True

        return False
