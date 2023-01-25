import PySimpleGUI as sg
from municipios import Municipio



def inputMUNI():
    layout = [
        [sg.Text('Ingrese los datos del municipio que desea visualizar')],
        [sg.Text('ID Municipio'), sg.Input(key='-MUNID-')],
        [sg.Text('ID Departamento'), sg.Input(key='-DEPID-')],
        [sg.Text('ID Provincia'), sg.Input(key='-PROVID-')],
        [sg.Button('Ver'),sg.Button('Atras')]
    ]
   
    window = sg.Window('Municipio', layout,element_justification='r')

    
    try:
        while True:
            event, values = window.read()
            if event == "Atras" or event == sg.WIN_CLOSED:
                break
            elif event == 'Ver':
                idMUN=values['-MUNID-']
                idDEP=values['-DEPID-']
                idPRO=values['-PROVID-']
                mun_count = Municipio.get_num_municipios()
                chosen = idMUN + idDEP + idPRO
                variable=mun_count[chosen][3]
                window.close()
                popup_message = "La cantidad de conexiones para la region seleccionada es de: " +str(variable)
                sg.popup(popup_message)
                window.close()  
        window.close()
    except Exception:
        popup_message = "Debe introducir IDs valido para un departamento con al menos 1 conexión"
        sg.popup(popup_message)    
    window.close()



if __name__ == '__main__':    
    inputMUNI()