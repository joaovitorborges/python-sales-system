import os
import csv

def create_csv_file(filename:str, header:list):
    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)       # add header row


def create_main_files():
    create_csv_file("clients.csv", ["name", "email"])


def write_to_csv(info:list, filename:str):           # used to insert a new object to a file, such as a client
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(info)


def get_object(ID:str, filename:str):            # used to return an object from a file, such as a client
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        for row in rows:
            if row[1] == ID:
                return row
    return []
