import PySimpleGUI as sg
from municipios import Departamento



def inputDEPT():
    layout = [
        [sg.Text('Ingrese los datos del departamento que desea visualizar')],
        [sg.Text('ID Departamento'), sg.Input(key='-DEPID-')],
        [sg.Text('ID Provincia'), sg.Input(key='-PROVID-')],
        [sg.Button('Ver'),sg.Button('Atras')]
    ]
   
    window = sg.Window('Departamento', layout,element_justification='r')

    
    try:
        while True:
            event, values = window.read()
            if event == "Atras" or event == sg.WIN_CLOSED:
                break
            elif event == 'Ver':
                idDEP=values['-DEPID-']
                idPRO=values['-PROVID-']
                dep_count = Departamento.get_num_departamento()
                chosen=idDEP+idPRO
                variable=dep_count[chosen][2]
                popup_message = "La cantidad de conexiones para la region seleccionada es de: " +str(variable)
                sg.popup(popup_message)
                window.close()  
        window.close()
    except Exception:
        popup_message = "Debe introducir IDs valido para un departamento con al menos 1 conexión"
        sg.popup(popup_message)    
    window.close()



if __name__ == '__main__':    
    inputDEPT()