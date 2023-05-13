from PySimpleGUI import PySimpleGUI as sg
import  modules.product as product, windows.main_windows as all_pages_windows


def main_product():
    #layout
    sg.theme('TanBlue')

    layout_client = [
        [sg.Text("Create Product:")],
        [sg.Button('Create Product')],
        [sg.Text("Search Product:")],
        [sg.Button('Search Product')],
        [sg.Text("Edit Product:")],
        [sg.Button('Edit Product')],
        [sg.Text("Delete Product:")],
        [sg.Button('Delete Product')],
        [sg.Text("If want go back:")],
        [sg.Button('Back')]
    ]
    #window
    Windows = sg.Window('Product Screen',layout_client,size=(300,300))

    #read events

    while True:
        event, values = Windows.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Create Product':
            Windows.Close()
            product_create_window()
        elif event == 'Search Product':
            Windows.Close()
            product_search_window()
        elif event == 'Edit Product':
            Windows.Close()
            product_edit_window()
        elif event == 'Delete Product':
            Windows.Close()
            product_delete_window()
        elif event == 'Back':
            Windows.Close()
            all_pages_windows.main_window()


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
        [sg.Text("",key="product_response")],
        [sg.Button('Create product')],[sg.Button('back')]
    ]
    #window
    Windows = sg.Window('Product Screen',layout_produto)

    #read events

    while True:
        event, values = Windows.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Create product':
            product_create = product.create_products(values['product_code'], values['product_name'], values['product_price'])
            print(f"testando {product_create}")
            Windows["product_response"].update(product_create)
        elif event == "back":
            Windows.Close()
            main_product()
            


def product_search_window():
    #layout
    sg.theme('TanBlue')

    layout_produto = [
        [sg.Text("Product Code")],
        [sg.InputText(key = "product_code")],
        [sg.Text("",key="product_response")],
        [sg.Button('Search Product')],
        [sg.Button("back")]
    ]
    #window
    Windows = sg.Window('Product Screen',layout_produto)

    #read events

    while True:
        event, values = Windows.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Search Product':
            product_response = product.search_product(values['product_code'])
            print(f"testando {product_response}")
            Windows["product_response"].update(product_response)
        elif event == "back":
            Windows.Close()
            main_product() 

def product_edit_window():
    #layout
    sg.theme('TanBlue')

    layout_produto = [
       [sg.Text("Please give the product code that you want to edit")],
        [sg.InputText(key = "product_code_old")],
        [sg.Text("",key="old_product_code_data")],
        [sg.Button("find product")],
        [sg.Text('Please give the new product code that you want to edit (blank to keep current value)')],
        [sg.InputText(key = "product_code_new")],
        [sg.Text('Please give  the new product name that you want to edit (blank to keep current value)')],
        [sg.InputText(key = "product_name_new")],
        [sg.Text('Please give  the new product price that you want to edit (blank to keep current value)')],
        [sg.InputText(key = "product_price_new")],
        [sg.Text("",key="new_product_data")],
        [sg.Button("edit product")],[sg.Button("back")],
    ]
    #window
    Windows = sg.Window('Product Screen',layout_produto)

    #read events

    while True:
        event, values = Windows.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'find product':
            product_old_data = product.search_product(values['product_code_old'])
            Windows["old_product_code_data"].update(product_old_data)
        elif event == 'edit product':
            product_new_data = product.edit_product_for_interface(values['product_code_old'],values['product_code_new'],values['product_name_new'],values['product_price_new'])
            Windows["new_product_data"].update(product_new_data)
        elif event == "back":
            Windows.Close()
            main_product()
    
def product_delete_window():
    #layout
    sg.theme('TanBlue')

    layout_produto = [
       [sg.Text("Please give the product code that you want to delete")],
        [sg.InputText(key = "product_code")],
        [sg.Text("",key="product_data")],
        [sg.Button("delete product")],[sg.Button("back")],
    ]
    #window
    Windows = sg.Window('Product Screen',layout_produto)

    #read events

    while True:
        event, values = Windows.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'delete product':
            product_new_data = product.delete_product(values['product_code'])
            Windows["product_data"].update(product_new_data)
        elif event == "back":
            Windows.Close()
            main_product()


