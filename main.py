import modules.utils as utils, modules.client as client, modules.address as address, modules.stock as stock , modules.product as product, modules.sales as sales, windows.product_windows as product_windows, windows.client_windows as client_windows

utils.create_main_files() # starts save files if they do not exist


#address.create_address("tavares de lyra", "1053", "sjp", "pr", "br", "123")
#
#client.create_client("joao", "123")
#
#address.create_address("tavares de lyra", "1053", "sjp", "pr", "br", "123")
#address.create_address("rua blabla", "123123", "sjp", "bh", "br", "123")
#address.create_address("rua xxxxx", "9999", "sjp", "bh", "br", "123")
#
#print("")
#print("searching a client address")
#address.get_client_addresses("123")
#
#print("")
#print("deleting a client address")
#
#address.delete_client_address("123")
#
#print("")
#print("editing client address")
#
#address.edit_client_address("123")

# print("creating stock item:")
# stock.insert_product_stock("12", 40)
# stock.insert_product_stock("13", 20)


# stock.increment_stock("12", 10) #increment stock item

# print("")
# print("searching product quantity:")
# stock.get_product_quantity("12") 
# stock.get_product_quantity("13") 

# import product

# print("creating products:")
# product.create_products("12", "banana", 2.50)
# product.create_products("13", "maca", 3.50)

# product.create_products("12", "ventilador", 150.99) # error, cannot create with same email

# print("")
# print("editing product:")
# product.edit_product("12") 


# print("")
# print("searching product:")
# product.search_product("12")

# product.delete_product("12")


#interface

# #product
# product_windows.product_create_window()

#client
#client_windows.client_create_window() #create window to create client
#client_windows.client_search_window() #create window to search client
#client_windows.client_edit_window() #create window to edit client 
#client_windows.client_delete_window() #create window to delete client



#sales.create_sale(product_id="12345", client_email="123", quantity=10)