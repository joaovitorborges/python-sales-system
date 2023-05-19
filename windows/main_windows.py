from PySimpleGUI import PySimpleGUI as sg
import windows.product_windows as product_windows
import windows.client_windows as client_windows
import windows.stock_windows as stock_windows
import windows.address_windows as address_windows

def main_window():
    #layout
    sg.theme('TanBlue')

    layout_main = [
       [sg.Text("what did you want to do?")],
       [sg.Button("Client Page")],
       [sg.Button("Address Page")],
       [sg.Button("Product Page")],
       [sg.Button("Stock Page")],
       [sg.Button("Exit")]
    ]
    #window
    Windows = sg.Window('Main Screen',layout_main ,size=(300, 300))

    #read events

    while True:
        event, values = Windows.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Client Page':
            Windows.Close()
            client_windows.main_client()
        elif event == 'Address Page':
            Windows.Close()
            address_windows.main_address()
        elif event == 'Product Page':
            Windows.Close()
            product_windows.main_product()
        elif event == 'Stock Page':
            Windows.Close()
            stock_windows.main_stock()
        elif event == 'Exit':
            Windows.close()
