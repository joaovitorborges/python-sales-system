import modules.utils as utils
import csv

productsFile = "products.csv"
stockFile = "stock.csv"


def increment_stock(code_product:str,quantity: int):
    if str(utils.get_single_object(code_product, productsFile, column=0)) != []:         # can create only if client exists
        all_items = utils.get_all_objects(stockFile)
        for product in all_items:
            if(product[0] == code_product):
                product[1] = int(product[1]) + quantity
                utils.update_all_objects(stockFile,all_items)
                break
        else:
            print("product doesnt exist on stock, use create product on stock")
    else:
        print(f"product {code_product} doesnt exist")
        

def insert_product_stock(code_product:str, quantity:int):
    if utils.get_single_object(code_product, productsFile, column=0) != []:         # can create only if client exists

        if(utils.get_single_object(code_product, stockFile, column=0) != []):
            print("Item already on stock, use increment instead")
            return
        utils.write_to_csv([code_product, quantity], stockFile)
        print(f"product {code_product} created on stock")
    else:
        print(f"product {code_product} related to stock not found")



def get_product_quantity(code_product:str):
    if utils.get_single_object(code_product, productsFile, column=0) != []:
        item = utils.get_single_object(code_product,stockFile, column=0)
        if item == []:
            print("Item not on stock.")
            return
        else:
            name = utils.get_single_object(code_product,productsFile,column=0)[1]
            print(f"{name} {item[1]}")
    else:
        print("Product does not exist")
        return []

