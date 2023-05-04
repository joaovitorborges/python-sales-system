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