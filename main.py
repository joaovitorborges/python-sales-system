import utils, client

utils.create_main_files() # starts save files if they do not exist

# need to create interface

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