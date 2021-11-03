import json

import os


def register(username, password, firs_name, last_name):

    path = os.path.join('db', 'users.txt')

    with open(path, 'r+') as file:
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
