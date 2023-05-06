#========================================= testing client module
import client

print("creating clients:")
client.create_client("joao", "321")
client.create_client("Lucca", "123")

client.create_client("Josias", "123") # error, cannot create with same email

print("")
print("editing client:")
client.edit_client("123") 


print("")
print("searching client:")
client.search_client("123")

#client.delete_client("321")


#====================================== testing address module

import client, address

address.create_address("tavares de lyra", "1053", "sjp", "pr", "br", "123")

client.create_client("joao", "123")

address.create_address("tavares de lyra", "1053", "sjp", "pr", "br", "123")
address.create_address("rua blabla", "123123", "sjp", "bh", "br", "123")
address.create_address("rua xxxxx", "9999", "sjp", "bh", "br", "123")

print("")
print("searching a client address")
address.get_client_addresses("123")

print("")
print("deleting a client address")

address.delete_client_address("123")

print("")
print("editing client address")

address.edit_client_address("123")

#===================================== testing product module

import product

print("creating products:")
product.create_products("12", "banana", 2.50)
product.create_products("13", "maca", 3.50)

product.create_products("12", "ventilador", 150.99) # error, cannot create with same email

print("")
print("editing product:")
product.edit_product("12") 


print("")
print("searching product:")
product.search_product("12")

# product.delete_product("12")

#===================================== testing product module

import stock

print("creating stock item:")
stock.insert_product_stock("12", 40)
stock.insert_product_stock("13", "20")

print("increment stock item:")
stock.increment_stock("12", 10) 

print("")
print("searching product quantity:")
stock.get_product_quantity("12") 
stock.get_product_quantity("13") 


