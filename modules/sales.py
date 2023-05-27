import modules.utils as utils
import modules.stock as stock
from datetime import datetime


clientsFile = "clients.csv"
productsFile = "products.csv"
stockFile = "stock.csv"
salesFile = "sales.csv"


def create_sale(product_id:str, client_email:str, quantity:int, address:list):
    if utils.get_single_object(client_email, clientsFile, column=0) == []:        # if client doesn't exist
        print("client does not exist")
        return   "client does not exist"
    
    product = utils.get_single_object(product_id, productsFile, column=0)
    if product == []:        # if product doesn't exist
        print("product does not exist")
        return "product does not exist"
    
    if int(utils.get_single_object(product_id, stockFile, column=0)[1]) < int(quantity):
        print("Not enough items in stock")
        return "Not enough items in stock"
    else:
        total_price = quantity*float(product[2])
        utils.write_to_csv([datetime.now(), client_email, product_id, quantity, total_price, address], salesFile)
        stock.increment_stock(product_id, -quantity)
        return "created sales successfully"


def search_sale(param:str, column):
    sales = utils.get_multiple_objects(param, salesFile, column)
    if sales != []:
        print("sales:")
        print(sales)
        return sales

    else:
        print("no sale found for this parameter")
        return "no sale found for this {param}"

def search_sale_client(email:str):
    return search_sale(email, 1)

def search_sale_product(product:str):
    return search_sale(product, 2)