import json
import os
from global_constants import *


def get_all_products():
    products = []
    products_path = os.path.join(DB_FOLDER_NAME, PRODUCTS_FILE_NAME)
    with open(products_path, 'r') as file:
        for line in file:
            products.append(json.loads(line.strip()))
        return products
