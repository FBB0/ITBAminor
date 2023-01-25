import PySimpleGUI as sg
from conexionesPROV import inputPROV
from conexionesDEPT import inputDEPT
from conexionesMUNI import inputMUNI

    
def cantCon():
    layout= [
        [sg.Text('Seleccione la opcion que quiere visualizar')],
        [sg.Button('Conexiones en una Provincia')],
        [sg.Button('Conexiones en un Departamento')],
        [sg.Button('Conexiones en un Municipio')],
        [sg.Button('Atras')]
    ]

    window=sg.Window('Ver cantidad de conexiones', layout, size=(400,200), element_justification='c')



    while True:
        event,values=window.read()
        if event == sg.WIN_CLOSED or event == 'Atras':
            break
        elif event == 'Conexiones en una Provincia':
            inputPROV()
            break
        elif event == 'Conexiones en un Departamento':
            inputDEPT()
            break
        elif event == 'Conexiones en un Municipio':
            inputMUNI()
            break
        
        
    window.close()
    
if __name__ == '__main__':
    cantCon()