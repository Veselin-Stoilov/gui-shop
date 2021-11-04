import json
import os


def get_all_products():
    products = []
    products_path = os.path.join('db', 'products.txt')
    with open(products_path, 'r') as file:
        for line in file:
            products.append(json.loads(line.strip()))
        return products
