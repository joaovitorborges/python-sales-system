import modules.utils as utils
import modules.stock as stock
from datetime import datetime


clientsFile = "clients.csv"
productsFile = "products.csv"
stockFile = "stock.csv"
salesFile = "sales.csv"


def create_sale(product_id:str, client_email:str, quantity:int):
    if utils.get_single_object(client_email, clientsFile, column=0) == []:        # if client doesn't exist
        print("client does not exist")
        return   
    
    product = utils.get_single_object(product_id, productsFile, column=0)
    if product == []:        # if product doesn't exist
        print("product does not exist")
        return 
    
    if int(utils.get_single_object(product_id, stockFile, column=0)[1]) < quantity:
        print("Not enough items in stock")
        return
    else:
        total_price = quantity*float(product[2])
        utils.write_to_csv([datetime.now(), client_email, product_id, quantity, total_price], salesFile)
        stock.increment_stock(product_id, -quantity)


def search_sale(param:str, column):
    sales = utils.get_multiple_objects(param, salesFile, column)
    if sales != []:
        print("sales:")
        print(sales)

    else:
        print("no sale found for this parameter")

def search_sale_client(email:str):
    search_sale(email, 1)

def search_sale_product(email:str):
    search_sale(email, 2)