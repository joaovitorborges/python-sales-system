import utils
import csv

productsFile = "products.csv"

def create_products(code:str, name:str):
    if utils.get_single_object(code, productsFile, column=0) == []:        # if product doesn't exist, create product
        utils.write_to_csv([code, name], productsFile)
        print("Product created")
    else:
        print(f'This product with the "{code}" already exists')


def search_product(code:str):
    product = utils.get_single_object(code, productsFile, column=0)
    if product != []:
        print("product found:")
        print(f" - Name: {product[1]}")
        print(f" - Code: {product[0]}")

    else:
        print("Product with this code was not found.")


def edit_product(code:str):
    products = utils.get_all_objects(productsFile)
    for product in products:
        if product[0] == code:
            print("Current product information:")
            print(f" - Name: {product[1]}")
            print(f" - Code: {product[0]}")

            new_code = (input("Enter code (blank to keep current value): ")).strip()
            new_name = (input("Enter item name (blank to keep current value): ")).strip()

            if new_code != code:       # if user changed email, must validate if no other account has that email
                if utils.get_single_object(new_code, productsFile, column=0) != []:
                    print("Can not update , as account with that email already exists.")
                    return

            if new_code == "":
                new_code = product[0]
            if new_name == "":
                new_name = product[1]


            products[products.index(product)] = [new_code, new_name] # update line with new info
            break
    else:
        print(f"product {code} not found.")
        return      # stop function

    utils.update_all_objects(productsFile, products)
    print("Product information has been updated.")


def delete_product(code:str):

    products = utils.get_all_objects(productsFile)
    for product in products:
        if product[0] == code:
            products.remove(product)          # remove product from list
            break
    else:
        print(f"product with this code: {code} not found.")
        return      # stop function

    utils.update_all_objects(productsFile, products)
    print(f"{code} has been deleted.")