import utils
import csv

clientsFile = "clients.csv"

def create_client(name:str, email:str):
    if utils.get_object(email, clientsFile) == []:        # if client doesnt exist, create client
        utils.write_to_csv([name, email], clientsFile)
        print("client created")
    else:
        print("client with this email already exists")


def search_client(email:str):
    client = utils.get_object(email, clientsFile)
    if client != []:
        print("client found:")
        print(f" - name: {client[0]}")
        print(f" - email: {client[1]}")
    else:
        print("client with this email not found.")


def edit_client(email:str):
    with open(clientsFile, mode='r') as file:
        reader = csv.reader(file)
        clients = list(reader)                  # get list of clients
        for client in clients:
            if client[1] == email:
                print("Current client information:")
                print(f" - name: {client[0]}")
                print(f" - email: {client[1]}")

                new_name = input("Enter name (blank to keep current value): ").strip()
                new_email = input("Enter email (blank to keep current value): ").strip()

                if new_email != email:       # if user changed email, must validate if no other account has that email
                    if utils.get_object(new_email, clientsFile) != []:
                        print("Can not update to new email, as account with that email already exists.")
                        return

                if new_name == "":
                    new_name = client[0]
                if new_email == "":
                    new_email = client[1]

                clients[clients.index(client)] = [new_name, new_email] # update line with new info
                break
        else:
            print(f"client {email} not found.")
            return      # stop function

    with open(clientsFile, mode='w', newline='') as file:     # write updated client list
        writer = csv.writer(file)
        writer.writerows(clients)
    print("Client information has been updated.")


def delete_client(email:str):
    with open(clientsFile, mode='r') as file:
        reader = csv.reader(file)
        clients = list(reader)                  # get list of clients
        for client in clients:
            if client[1] == email:
                clients.remove(client)          # remove client from list
                break
        else:
            print(f"client {email} not found.")
            return      # stop function

    with open(clientsFile, mode='w', newline='') as file:     # write updated client list
        writer = csv.writer(file)
        writer.writerows(clients)
    print(f"{email} has been deleted.")