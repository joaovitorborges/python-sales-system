from PySimpleGUI import PySimpleGUI as sg
import  modules.stock as stock, windows.main_windows as all_pages_windows,modules.product as product


def main_stock():
    #layout
    sg.theme('TanBlue')

    layout_client = [
        [sg.Text("Insert Stock:")],
        [sg.Button('Insert Stock')],
        [sg.Text("Get product quantity on Stock:")],
        [sg.Button('Get product quantity on Stock')],
        [sg.Text("Increment Stock:")],
        [sg.Button('Increment Stock')],
        [sg.Text("If want go back:")],
        [sg.Button('Back')]
    ]
    #window
    Windows = sg.Window('Stock Screen',layout_client,size=(300,300))

    #read events

    while True:
        event, values = Windows.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Insert Stock':
            Windows.Close()
            stock_insert_product_window()
        elif event == 'Increment Stock':
            Windows.Close()
            stock_increment_stock_window()
        elif event == 'Get product quantity on Stock':
            Windows.Close()
            stock_get_product_quantity_window()
        elif event == 'Back':
            Windows.Close()
            all_pages_windows.main_window()


def stock_increment_stock_window():
    #layout
    sg.theme('TanBlue')

    layout_stock = [
        [sg.Text("Product Code")],
        [sg.InputText(key = "product_code")],
        [sg.Button('product on stock')],
        [sg.Text("",key="stock_has_product_response")],
        [sg.Text("Please give the product quantity")],
        [sg.InputText(key = "product_quantity")],
        [sg.Text("",key="stock_response")],
        [sg.Button('Increment product')],[sg.Button('back')]
    ]
    #window
    Windows = sg.Window('Stock Screen',layout_stock)

    #read events

    while True:
        event, values = Windows.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'product on stock':
            stock_product = stock.get_product_quantity(values['product_code'])
            Windows["stock_has_product_response"].update(stock_product)
        elif event == 'Increment product':
            increment_stock = stock.increment_stock(values['product_code'], values['product_quantity'])
            print(f"testando {increment_stock}")
            Windows["stock_response"].update(increment_stock)
        elif event == "back":
            Windows.Close()
            main_stock()
            
def stock_insert_product_window():
    #layout
    sg.theme('TanBlue')

    layout_produto = [
        [sg.Text("Product Code")],
        [sg.InputText(key = "product_code")],
        [sg.Button('See if Product exists')],
        [sg.Text("",key="product_exists")],
        [sg.Text("Product quantity")],
        [sg.InputText(key = "product_quantity")],
        [sg.Text("",key="stock_response")],
        [sg.Button('Insert Product')],
        [sg.Button("back")]
    ]
    #window
    Windows = sg.Window('Stock Screen',layout_produto)

    #read events

    while True:
        event, values = Windows.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'See if Product exists':
            stock_product = product.search_product(values['product_code'])
            Windows["product_exists"].update(stock_product)
        elif event == 'Insert Product':
            stock_response = stock.insert_product_stock(values['product_code'],values['product_quantity'])
            print(f"testando {stock_response}")
            Windows["stock_response"].update(stock_response)
        elif event == "back":
            Windows.Close()
            main_stock() 

def stock_get_product_quantity_window():
    #layout
    sg.theme('TanBlue')

    layout_produto = [
        [sg.Text("Product Code")],
        [sg.InputText(key = "product_code")],
        [sg.Button('See the quantity of the product')],
        [sg.Text("",key="stock_response")],
        [sg.Button("back")]
    ]
    #window
    Windows = sg.Window('Stock Screen',layout_produto)

    #read events

    while True:
        event, values = Windows.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'See the quantity of the product':
            stock_product = stock.get_product_quantity(values['product_code'])
            Windows["stock_response"].update(stock_product)
        elif event == "back":
            Windows.Close()
            main_stock()  


