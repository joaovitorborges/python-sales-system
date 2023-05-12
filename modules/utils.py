import os
import csv

def create_csv_file(filename:str, header:list):
    if not os.path.exists('data/'):
        os.makedirs('data/')
    if not os.path.exists(filename):
        with open('data/'+filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)       # add header row


def create_main_files():
    create_csv_file("clients.csv", ["email", "name"])
    create_csv_file("address.csv", ["client_mail", "street", "number", "city", "state", "country"])
    create_csv_file("products.csv", ["code","name","price"])
    create_csv_file("stock.csv", ["code_product","quantity"])
    create_csv_file("sales.csv", ["date", "client_email", "product_id", "quantity", "total_price"])
    


def write_to_csv(info:list, filename:str):           # used to insert a new object to a file, such as a client
    with open('data/'+filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(info)


def get_single_object(parameter:str, filename:str, column:int):            # used to return an object from a file, such as a client
    with open('data/'+filename, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        for row in rows:
            if row[column] == parameter:
                return row
    return []


def get_multiple_objects(parameter:str, filename:str, column:int):
    with open('data/'+filename, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        results = []
        for row in rows:
            if row[column] == parameter:
                results.append(row)
    return results


def get_all_objects(filename:str):
    with open('data/'+filename, mode='r') as file:
        reader = csv.reader(file)
        return list(reader)
    

def update_all_objects(filename:str, objects:list):
    with open('data/'+filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(objects)