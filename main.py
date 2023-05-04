import utils, client, address

utils.create_main_files() # starts save files if they do not exist

# need to create interface

# address.create_address("street", "number", "city", "state", "country", "client_email")
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