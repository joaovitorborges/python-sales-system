import modules.utils as utils
import csv

clientsFile = "clients.csv"

def create_client(name:str, email:str):
    if utils.get_single_object(email, clientsFile, column=0) == []:        # if client doesn't exist, create client
        utils.write_to_csv([email, name], clientsFile)
        print("client created")
    else:
        print("client with this email already exists")


def search_client(email:str):
    client = utils.get_single_object(email, clientsFile, column=0)
    if client != []:
        print("client found:")
        print(f" - name: {client[1]}")
        print(f" - email: {client[0]}")
        return "email: " + client[0] + " | name: " + client[1]

    else:
        print("client with this email not found.")


def edit_client(email:str):
    clients = utils.get_all_objects(clientsFile)
    for client in clients:
        if client[0] == email:
            print("Current client information:")
            print(f" - name: {client[1]}")
            print(f" - email: {client[0]}")

            new_name = input("Enter name (blank to keep current value): ").strip()
            new_email = input("Enter email (blank to keep current value): ").strip()

            if new_email != email:       # if user changed email, must validate if no other account has that email
                if utils.get_single_object(new_email, clientsFile, column=0) != []:
                    print("Can not update to new email, as account with that email already exists.")
                    return

            if new_name == "":
                new_name = client[1]
            if new_email == "":
                new_email = client[0]

            clients[clients.index(client)] = [new_email, new_name] # update line with new info
            break
    else:
        print(f"client {email} not found.")
        return      # stop function

    utils.update_all_objects(clientsFile, clients)
    print("Client information has been updated.")

#test for interface (delete after or change to this one, because work on the interface)
def edit_client_test_inteface(email:str, new_email:str,new_name:str):
    clients = utils.get_all_objects(clientsFile)
    for client in clients:
        if client[0] == email:
            print("Current client information:")
            print(f" - name: {client[1]}")
            print(f" - email: {client[0]}")

            if new_email != email:       # if user changed email, must validate if no other account has that email
                if utils.get_single_object(new_email, clientsFile, column=0) != []:
                    print("Can not update to new email, as account with that email already exists.")
                    return

            if new_name == "":
                new_name = client[1]
            if new_email == "":
                new_email = client[0]

            clients[clients.index(client)] = [new_email, new_name] # update line with new info
            break
        
    else:
        print(f"client {email} not found.")
        return  f"client {email} not found."     # stop function
    
    utils.update_all_objects(clientsFile, clients)
    print("Client information has been updated.")
    return "new email: " + new_email + " | new name: " + new_name


def delete_client(email:str):
    clients = utils.get_all_objects(clientsFile)
    for client in clients:
        if client[0] == email:
            clients.remove(client)          # remove client from list
            break
    else:
        print(f"client {email} not found.")
        return      # stop function

    utils.update_all_objects(clientsFile, clients)
    print(f"{email} has been deleted.")
    return f"{email} has been deleted."