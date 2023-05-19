from PySimpleGUI import PySimpleGUI as sg
import  modules.address as address
import windows.main_windows as all_pages_windows

def main_address():
    #layout
    sg.theme('TanBlue')

    layout_address = [
        [sg.Text("Add Client Address:")],
        [sg.Button('Add Client Address')],
        [sg.Text("Edit Client Address:")],
        [sg.Button('Edit Client Address')],
        [sg.Text("Add Client Address:")],
        [sg.Button('Delete Client Address')],
        [sg.Text("If want go back:")],
        [sg.Button('Back')]
    ]
    #window
    Windows = sg.Window('Address Screen',layout_address,size=(300,600))

    #read events

    while True:
        event, values = Windows.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Add Client Address':
            Windows.Close()
            address_create_window()
        elif event == 'Edit Client Address':
            Windows.Close()
            address_create_window
            #address_edit_window()
        elif event == 'Delete Client Address':
            Windows.Close()
            address_delete_window()
        elif event == 'Back':
            Windows.close()
            all_pages_windows.main_window()



def address_create_window():
    #layout
    sg.theme('TanBlue')

    layout_client = [
        [sg.Text("Client mail")],
        [sg.InputText(key = "client_mail")],
        [sg.Text("Street")],
        [sg.InputText(key = "street")],
        [sg.Text("number")],
        [sg.InputText(key = "number")],
        [sg.Text("city")],
        [sg.InputText(key = "city")],
        [sg.Text("state")],
        [sg.InputText(key = "state")],
        [sg.Text("country")],
        [sg.InputText(key = "country")],
        [sg.Button('Add Address')],
        [sg.Text("",key="address_response")],
        [sg.Button('Back')],
    ]
    #window
    Windows = sg.Window('Client Screen',layout_client)

    #read events

    while True:
        event, values = Windows.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Add Address':
            response = address.create_address(values['street'],values['number'],values['city'],values['state'],values['country'], values['client_mail'])
            Windows["address_response"].update(response)
            if response == "address created":
                Windows["address_response"].update(response)
                Windows["client_mail"].update("")
                Windows["street"].update("")
                Windows["number"].update("")
                Windows["city"].update("")
                Windows["state"].update("")
                Windows["country"].update("")
        elif event == 'Back':
            Windows.close()
            main_address()


def address_delete_window():
    #layout
    sg.theme('TanBlue')
    addresses = []
    lst = sg.Listbox(addresses, size=(30, 4), expand_y=True, enable_events=True, key='list')

    layout_client = [
        [sg.Text("Client mail")],
        [sg.InputText(key = "client_mail")],
        [sg.Button('Search')],
        [lst],
        [sg.Button('Delete')],
        [sg.Text("",key="address_response")],
        [sg.Button('Back')],
    ]
    #window
    Windows = sg.Window('Client Screen',layout_client)

    #read events

    while True:
        event, values = Windows.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Search':
            addresses = address.get_client_addresses(values['client_mail'])
            if addresses == []:
                Windows['list'].update(addresses)
                Windows["address_response"].update("No addresses found for this email")
            elif addresses == "client does not exist":
                addresses = []
                Windows['list'].update(addresses)
                Windows["address_response"].update("User does not exist")
            else:
                Windows['list'].update(addresses)
                Windows["address_response"].update("Addresses found. Select an address to delete")
        
        elif event == 'Delete':
            if Windows['list'].get() != []:
                delete = addresses.index(Windows['list'].get()[0])
                response = address.delete_client_address(values['client_mail'], delete)
                Windows["address_response"].update(response)
                addresses = address.get_client_addresses(values['client_mail'])
                Windows['list'].update(addresses)
            else:
                Windows["address_response"].update("select an address to delete")
            

        elif event == 'Back':
            Windows.close()
            main_address()