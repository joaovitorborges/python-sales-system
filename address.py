import utils
import csv

clientsFile = "clients.csv"
addressFile = "address.csv"

def create_address(street:str, number:int, city:str, state:str, country:str, client_mail:str):
    if utils.get_single_object(client_mail, clientsFile, column=0) != []:         # can create only if client exists
        utils.write_to_csv([client_mail, street, number, city, state, country], addressFile)
        print("address created")
    else:
        print("Client related to address not found")

def get_client_addresses(client_mail:str):
    if utils.get_single_object(client_mail, clientsFile, column=0) != []:
        addresses = utils.get_multiple_objects(client_mail,addressFile, column=0)
        if len(addresses) == 0:
            print("Client does not have any address registered.")
            return []
        else:
            print("Client addresses:")
            c = 1
            for adr in addresses:
                print(f"{c} - {adr[1]} {adr[2]}, {adr[3]}, {adr[4]}, {adr[5]}")
                c+=1
            return addresses
    else:
        print("Client does not exist")
        return []

def delete_client_address(client_mail:str):
    if utils.get_single_object(client_mail, clientsFile, column=0) != []:
        addresses = utils.get_all_objects(addressFile)
        c = 1
        client_addresses = []
        for adr in addresses:
            if adr[0] == client_mail:
                print(f"{c} - {adr[1]} {adr[2]}, {adr[3]}, {adr[4]}, {adr[5]}")
                client_addresses.append(adr)
                c+=1
        if client_addresses != []:
            delete = int(input("type the number of the address you want to delete(0 to cancel): "))
            while delete not in range(1,len(client_addresses)):
                if delete == 0:
                    return
                delete = int(input("please insert a valid range(0 to cancel): "))

            addresses.pop(addresses.index(client_addresses[delete-1]))
            utils.update_all_objects(addressFile, addresses)
        else:
            print("user has no addresses registered.")
    else:
        print("user not found.")


def edit_client_address(client_mail:str):
    if utils.get_single_object(client_mail, clientsFile, column=0) != []:
        addresses = utils.get_all_objects(addressFile)
        c = 1
        client_addresses = []
        for adr in addresses:
            if adr[0] == client_mail:
                print(f"{c} - {adr[1]} {adr[2]}, {adr[3]}, {adr[4]}, {adr[5]}")
                client_addresses.append(adr)
                c+=1
        if client_addresses != []:
            edit = int(input("type the number of the address you want to edit: "))
            addr_edit = addresses[addresses.index(client_addresses[edit-1])]
            print(f"address being edited: {addr_edit}")
            while edit not in range(1,len(client_addresses)):
                if edit == 0:
                    return
                edit = int(input("please insert a valid range: "))
            
            new_street = input("Enter street (blank to keep current value): ").strip()
            new_number = input("Enter number (blank to keep current value): ").strip()

            if new_street == "":
                new_street = addr_edit[1]
            if new_number == "":
                new_number = addr_edit[2]
            
            addr_edit[1] = new_street
            addr_edit[2] = new_number
            addresses[addresses.index(client_addresses[edit-1])] = addr_edit
            utils.update_all_objects(addressFile, addresses)
        else:
            print("user has no addresses registered.")
    else:
        print("user not found.")