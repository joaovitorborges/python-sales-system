import modules.utils as utils
import csv

productsFile = "products.csv"

def create_products(code:str, name:str, price:float):
    if utils.get_single_object(code, productsFile, column=0) == []:        # if product doesn't exist, create product
        utils.write_to_csv([code, name, price], productsFile)
        print("Product created")
        return "Product created"
    else:
        print(f'This product with the code "{code}" already exists')
        return f'This product with the code "{code}" already exists'


def search_product(code:str):
    product = utils.get_single_object(code, productsFile, column=0)
    if product != []:
        print("product found:")
        print(f" - Price: {product[2]}")
        print(f" - Name: {product[1]}")
        print(f" - Code: {product[0]}")
        return "Code: " + product[0] + " | Name: " + product[1] + " | Price: " + product[2]
    else:
        print("Product with this code was not found.")
        return "Product with this code was not found."


def edit_product_for_interface(code:str, new_code:str, new_name:str, new_price:float):
    products = utils.get_all_objects(productsFile)
    for product in products:
        if product[0] == code:
            print("Current product information:")
            print(f" - Price: {product[2]}")
            print(f" - Name: {product[1]}")
            print(f" - Code: {product[0]}")

            if new_code != code:       # if user changed email, must validate if no other account has that email
                if utils.get_single_object(new_code, productsFile, column=0) != []:
                    print("Can not update , as account with that email already exists.")
                    return "Can not update , as account with that email already exists."

            if new_code == "":
                new_code = product[0]
            if new_name == "":
                new_name = product[1]
            if new_price == "":
                new_price = product[2]


            products[products.index(product)] = [new_code, new_name,new_price] # update line with new info
            break
    else:
            print(f"product {code} not found.")
            return  f"product {code} not found."    # stop function

    utils.update_all_objects(productsFile, products)
    print("Product information has been updated.")
    return "new email: " + new_code + " | new name: " + new_name + " | new price: " + new_price

def delete_product(code:str):
    products = utils.get_all_objects(productsFile)
    for product in products:
        if product[0] == code:
            products.remove(product)          # remove product from list
            break
    else:
        print(f"product with this code: {code} not found.")
        return f"product with this code: {code} not found."      # stop function

    utils.update_all_objects(productsFile, products)
    print(f"{code} has been deleted.")
    return f"product code: {code} has been deleted."