from PySimpleGUI import PySimpleGUI as sg
import  modules.sales as sales, windows.main_windows as all_pages_windows ,modules.sales as sales, modules.product as product

def main_sales():
    #layout
    sg.theme('TanBlue')

    layout_client = [
        [sg.Text("Create Sales:")],
        [sg.Button('Create Sales')],
        [sg.Text("Get product quantity on Stock:")],
        [sg.Button('Get product quantity on Stock')],
        [sg.Text("Increment Stock:")],
        [sg.Button('Increment Stock')],
        [sg.Text("If want go back:")],
        [sg.Button('Back')]
    ]
    #window
    Windows = sg.Window('Sales Screen',layout_client,size=(300,300))

    #read events

    while True:
        event, values = Windows.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Insert Stock':
            Windows.Close()
            create_sales_window()
        elif event == 'Increment Stock':
            Windows.Close()
        elif event == 'Get product quantity on Stock':
            Windows.Close()
        elif event == 'Back':
            Windows.Close()
            all_pages_windows.main_window()

def create_sales_window():
        #layout
    sg.theme('TanBlue')

    layout_stock = [
        [sg.Text("Product Code")],
        [sg.InputText(key = "product_code")],
        [sg.Button('See if Product exists')],
        [sg.InputText(key = "product_exist")],
        [sg.Text("Client Email")],
        [sg.InputText(key = "client_email")],
        [sg.Text("quantity")],
        [sg.InputText(key = "quantity")], 
        [sg.Text("adress")],
        [sg.InputText(key = "adress")], 
        [sg.Button('back')]
    ]
    #window
    Windows = sg.Window('Stock Screen',layout_stock)

    #read events

    while True:
        event, values = Windows.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'See if Product exists':
            stock_product = product.search_product(values['product_code'])
            Windows["product_exists"].update(stock_product)
        elif event == "back":
            Windows.Close()
            main_sales()
            
            
