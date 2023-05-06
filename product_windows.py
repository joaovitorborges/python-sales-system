from PySimpleGUI import PySimpleGUI as sg
import  product

def product_create_window():
    #layout
    sg.theme('TanBlue')

    layout_produto = [
        [sg.Text("Product Code")],
        [sg.InputText(key = "product_code")],
        [sg.Text("Please give the product name")],
        [sg.InputText(key = "product_name")],
        [sg.Text("Please give the product price")],
        [sg.InputText(key = "product_price")],
        [sg.Button('Create product')]
    ]
    #window
    Windows = sg.Window('Product Screen',layout_produto)

    #read events

    while True:
        event, values = Windows.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Create product':
            product.create_products(values['product_code'], values['product_name'], values['product_price'])
            break

from PySimpleGUI import PySimpleGUI as sg
import  client

def client_create_window():
    #layout
    sg.theme('TanBlue')

    layout_client = [
        [sg.Text("Please give the client Email")],
        [sg.InputText(key = "client_email")],
        [sg.Text("Please give the client name")],
        [sg.InputText(key = "client_name")],
        [sg.Button('Create client')]
    ]
    #window
    Windows = sg.Window('Client Screen',layout_client)

    #read events

    while True:
        event, values = Windows.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Create client':
            client.create_client(values['client_name'],values['client_email'])
            break
