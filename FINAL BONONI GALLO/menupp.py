import PySimpleGUI as sg
from gesAP import gesAP
from conexiones import menuConexiones


def menu():
    layout= [
        [sg.Text('Bienvenido al sistema de gestion de PAIS DIGITAL')],
        [sg.Text('Para comenzar a operar seleccione una opcion')],
        [sg.Text('')],
        [sg.Button('Gestionar Puntos de Acceso')],
        # [sg.Button('Gestionar Municipios')],
        [sg.Button('Conexiones')],
        [sg.Button('Salir')]
    ]

    window=sg.Window('Pais Digital', layout, size=(400,200), element_justification='c')



    while True:
        event,values=window.read()
        if event == sg.WIN_CLOSED or event == 'Salir':
            break
        elif event == 'Gestionar Puntos de Acceso':
            gesAP()
        elif event == 'Conexiones':
            menuConexiones() 
    window.close()
    
    return True


if __name__ == '__main__':
    menu()