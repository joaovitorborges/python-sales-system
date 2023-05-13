from PySimpleGUI import PySimpleGUI as sg
import  modules.client as client, windows.main_windows as all_pages_windows


def main_client():
    #layout
    sg.theme('TanBlue')

    layout_client = [
        [sg.Text("Create Client:")],
        [sg.Button('Create Client')],
        [sg.Text("Search Client:")],
        [sg.Button('Search Client')],
        [sg.Text("Edit Client:")],
        [sg.Button('Edit Client')],
        [sg.Text("Delete Client:")],
        [sg.Button('Delete Client')],
        [sg.Text("If want go back:")],
        [sg.Button('Back')]
    ]
    #window
    Windows = sg.Window('Client Screen',layout_client,size=(300,300))

    #read events

    while True:
        event, values = Windows.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Create Client':
            Windows.Close()
            client_create_window()
        elif event == 'Search Client':
            Windows.Close()
            client_search_window()
        elif event == 'Edit Client':
            Windows.Close()
            client_edit_window()
        elif event == 'Delete Client':
            Windows.Close()
            client_delete_window()
        elif event == 'Back':
            Windows.close()
            all_pages_windows.main_window()

def client_create_window():
    #layout
    sg.theme('TanBlue')

    layout_client = [
        [sg.Text("Please give the client Email")],
        [sg.InputText(key = "client_email")],
        [sg.Text("Please give the client name")],
        [sg.InputText(key = "client_name")],
        [sg.Button('Create client')],
        [sg.Button('Back')],
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
        elif event == 'Back':
            Windows.close()
            main_client()


def client_search_window():
    #layout
    sg.theme('TanBlue')

    layout_client = [
        [sg.Text("Please give the client Email")],
        [sg.InputText(key = "client_email")],
        [sg.Button('Found client')],
        [sg.Text("",key="email_found")],
        [sg.Button("back")],
    ]
    #window
    Windows = sg.Window('Client Screen',layout_client)

    #read events

    while True:
        event, values = Windows.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Found client':
            client_email = client.search_client(values['client_email'])
            print(f"client: {client_email}")
            Windows["email_found"].update(client_email)
        elif event == "back":
            Windows.Close()
            main_client()

def client_edit_window():
    #vamos ter que dar uma olhada, na funcao e mudar como vem o dados na funcao do edit_client 
    #para que esteja funcionando o edit do client na interface
    #layout
    sg.theme('TanBlue')

    layout_client = [
        [sg.Text("Please give the client email that you want to edit")],
        [sg.InputText(key = "client_email_old")],
        [sg.Text("",key="old_client_data")],
        [sg.Button("find client")],
        [sg.Text('Please give the new client email that you want to edit (blank to keep current value)')],
        [sg.InputText(key = "client_email_new")],
        [sg.Text('Please give  the new client name that you want to edit (blank to keep current value)')],
        [sg.InputText(key = "client_name_new")],
        [sg.Text("",key="new_client_data")],
        [sg.Button("edit client")],[sg.Button("back")],
    ]

    #window
    Windows = sg.Window('Client Screen',layout_client)

    #read events

    while True:
        event, values = Windows.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'find client':
            client_old_data = client.search_client(values['client_email_old'])
            Windows["old_client_data"].update(client_old_data)
        elif event == 'edit client':
            client_new_data = client.edit_client_test_inteface(values['client_email_old'],values['client_email_new'],values['client_name_new'])
            Windows["new_client_data"].update(client_new_data)
        elif event == "back":
            Windows.Close()
            main_client()

def client_delete_window():
    #layout
    sg.theme('TanBlue')

    layout_client = [
        [sg.Text("Please give the client email that you want to delete")],
        [sg.InputText(key = "client_email_to_delete")],
        [sg.Button('Delete Email')],
        [sg.Text("",key="email_deleted")],
        [sg.Button("back")],
    ]
    #window
    Windows = sg.Window('Client Screen',layout_client)

    #read events

    while True:
        event, values = Windows.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Delete Email':
            delete_client_email = client.delete_client(values['client_email_to_delete'])
            print(f"client: {delete_client_email}")
            Windows["email_deleted"].update(delete_client_email)
        elif event == "back":
            Windows.Close()
            main_client()
