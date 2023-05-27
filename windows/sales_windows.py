from PySimpleGUI import PySimpleGUI as sg
import  modules.sales as sales, windows.main_windows as all_pages_windows
import modules.product as product
import modules.client as client
import  modules.address as address

def main_sales():
    #layout
    sg.theme('TanBlue')

    layout_sales = [
        [sg.Text("Create Sales:")],
        [sg.Button('Create Sales')],
        [sg.Text("Search Client Sales:")],
        [sg.Button('Search Client Sales')],
        [sg.Text("Search Product Sales:")],
        [sg.Button('Search Product Sales')],
        [sg.Text("If want go back:")],
        [sg.Button('Back')]
    ]
    #window
    Windows = sg.Window('Sales Screen',layout_sales,size=(300,300))

    #read events

    while True:
        event, values = Windows.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Create Sales':
            Windows.Close()
            create_sales_window()
        elif event == 'Search Client Sales':
            Windows.Close()
            search_sales_client_windows()
        elif event == 'Search Product Sales':
            Windows.Close()
            search_sales_product_windows()
        elif event == 'Back':
            Windows.Close()
            all_pages_windows.main_window()

def create_sales_window():
        #layout
    sg.theme('TanBlue')
    addresses = []  
    lst = sg.Listbox(addresses, size=(60, 4), expand_y=True, enable_events=True, key='list')

    layout_sales = [
        [sg.Text("Product Code")],
        [sg.InputText(key = "product_code")],
        [sg.Button('See if Product exists')],
        [sg.Text(key = "product_exist")],
        [sg.Text("Client Email")],
        [sg.InputText(key = "client_email")],
        [sg.Button('See if Client exists')],
        [sg.Text(key = "client_exist")],
        [sg.Text("quantity")],
        [sg.InputText(key = "quantity")], 
        [sg.Text("adress")],
        [sg.Button('Search address')],
        [lst],
        [sg.Text("",key="address_response")],
        [sg.Button('create sales')],
        [sg.Text("",key="create_sales")],
        [sg.Button('back')]
    ]
    #window
    Windows = sg.Window('Sales Screen',layout_sales)

    #read events

    while True:
        event, values = Windows.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "See if Client exists":
            client_exist = client.search_client(values['client_email'])
            Windows["client_exist"].update(client_exist)
        elif event == 'See if Product exists':
            stock_product = product.search_product(values['product_code'])
            Windows["product_exist"].update(stock_product)
        elif event == 'Search address':
            addresses = address.get_client_addresses(values['client_email'])
            if addresses == []:
                Windows['list'].update(addresses)
                Windows["address_response"].update("No addresses found for this email")
            elif addresses == "client does not exist":
                addresses = []
                Windows['list'].update(addresses)
                Windows["address_response"].update("User does not exist")
            else:
                Windows['list'].update(addresses)
                Windows["address_response"].update("Addresses found")
        elif event == 'create sales':
            if Windows['list'].get() != []:
                addres = addresses.index(Windows['list'].get()[0])
                print(addres)
                response = sales.create_sale(values['product_code'],values['client_email'],int(values['quantity']),addres)
                Windows["create_sales"].update(response)
            else:
                Windows["create_sales"].update("select an address to make a sales")
        elif event == "back":
            Windows.Close()
            main_sales()
            

def search_sales_client_windows():
         #layout
    sg.theme('TanBlue')

    layout_sales = [
        [sg.Text("Client email address")],
        [sg.InputText(key = "client_email")],
        [sg.Button('See if Client exists')],
        [sg.Text(key = "client_exists")],
        [sg.Button('Search Sales for the client')],
        [sg.Text(key = "client_sales")],
        [sg.Button('back')]
    ]
    #window
    Windows = sg.Window('Sales Screen',layout_sales)

    #read events

    while True:
        event, values = Windows.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'See if Client exists':
            client_exists = client.search_client(values['client_email'])
            Windows['client_exists'].update(client_exists)
        elif event == 'Search Sales for the client':
            client_sales = sales.search_sale_client(values['client_email'])
            Windows['client_sales'].update(client_sales)
        elif event == "back":
            Windows.Close()
            main_sales()

def search_sales_product_windows():
         #layout
    sg.theme('TanBlue')

    layout_sales = [
        [sg.Text("Product Code")],
        [sg.InputText(key = "product_code")],
        [sg.Button('See if Product exists')],
        [sg.Text(key = "product_exists")],
        [sg.Button('Search Sales for the product')],
        [sg.Text(key = "product_sales")],
        [sg.Button('back')]
    ]
    #window
    Windows = sg.Window('Sales Screen',layout_sales)

    #read events

    while True:
        event, values = Windows.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'See if Product exists':
            product_exists = product.search_product(values['product_code'])
            Windows['product_exists'].update(product_exists)
        elif event == 'Search Sales for the product':
            product_sales = sales.search_sale_product(values['product_code'])
            Windows['product_sales'].update(product_sales)
        elif event == "back":
            Windows.Close()
            main_sales()
            
