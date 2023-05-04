import utils, client, address, stock , product

utils.create_main_files() # starts save files if they do not exist

# need to create interface

# address.create_address("street", "number", "city", "state", "country", "client_email")
# address.create_address("tavares de lyra", "1053", "sjp", "pr", "br", "123")

# client.create_client("joao", "123")

# address.create_address("tavares de lyra", "1053", "sjp", "pr", "br", "123")
# address.create_address("rua blabla", "123123", "sjp", "bh", "br", "123")
# address.create_address("rua xxxxx", "9999", "sjp", "bh", "br", "123")

# print("")
# print("searching a client address")
# address.get_client_addresses("123")

# print("")
# print("deleting a client address")

# address.delete_client_address("123")

# print("")
# print("editing client address")

# address.edit_client_address("123")

import stock

# print("creating stock item:")
# stock.insert_product_stock("12", 40)
# stock.insert_product_stock("13", 20)


# stock.increment_stock("12", 10) #increment stock item

print("")
print("searching product quantity:")
stock.get_product_quantity("12") 
stock.get_product_quantity("13") 

