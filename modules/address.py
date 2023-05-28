import modules.utils as utils

clientsFile = "clients.csv"
addressFile = "address.csv"

def create_address(street:str, number:int, city:str, state:str, country:str, client_mail:str):
    if utils.get_single_object(client_mail, clientsFile, column=0) != []:         # can create only if client exists
        utils.write_to_csv([client_mail, street, number, city, state, country], addressFile)
        return "address created"
    else:
        return "Client related to address not found"

def get_client_addresses(client_mail:str):
    if utils.get_single_object(client_mail, clientsFile, column=0) != []:
        addresses = utils.get_multiple_objects(client_mail,addressFile, column=0)
        if len(addresses) == 0:
            print("Client does not have any address registered.")
            return []
        else:
            #print("Client addresses:")
            c = 1
            for adr in addresses:
                #print(f"{c} - {adr[1]} {adr[2]}, {adr[3]}, {adr[4]}, {adr[5]}")
                c+=1
            return addresses
    else:
        print("Client does not exist")
        return "client does not exist"

def delete_client_address(client_mail:str, index:int):
    if utils.get_single_object(client_mail, clientsFile, column=0) != []:
        addresses = utils.get_all_objects(addressFile)
        c = 1
        client_addresses = []
        for adr in addresses:
            if adr[0] == client_mail:
                client_addresses.append(adr)
                c+=1
        if client_addresses != []:
            delete = index #int(input("type the number of the address you want to delete(0 to cancel): "))
            if delete not in range(0,len(client_addresses)):
                return "error on index"
            addresses.pop(addresses.index(client_addresses[delete]))
            utils.update_all_objects(addressFile, addresses)
            return "address deleted."
        else:
            return "user has no addresses registered."
    else:
        return "user not found."

def edit_client_address(client_mail:str, index:int, street:str, number:int, city:str, state:str, country:str ):
    if utils.get_single_object(client_mail, clientsFile, column=0) != []:
        addresses = utils.get_all_objects(addressFile)
        c = 1
        client_addresses = []
        for adr in addresses:
            if adr[0] == client_mail:
                client_addresses.append(adr)
                c+=1
                
        if client_addresses != []:
            edit = index
            addr_edit = addresses[addresses.index(client_addresses[edit])]
            print(f"address being edited: {addr_edit}")
            if edit not in range(0,len(client_addresses)):
                return "error on index"
            
            
            if street == "":
                return "Please insert all values"
            if number == "":
                return "Please insert all values"
            if city == "":
                return "Please insert all values"
            if state == "":
                return "Please insert all values"
            if country == "":
                return "Please insert all values"
            
            addr_edit[1] = street
            addr_edit[2] = number
            addr_edit[3] = city
            addr_edit[4] = state
            addr_edit[5] = country
            
            addresses[addresses.index(client_addresses[edit])] = addr_edit
            utils.update_all_objects(addressFile, addresses)
            return "address updated successfully"
        else:
            return "user has no addresses registered."
    else:
        return "user not found."