import PySimpleGUI as sg
from municipios import Provincia



def inputPROV():
    layout = [
        [sg.Text('Ingrese los datos de  la provincia que desea visualizar')],
        [sg.Text('ID Provincia'), sg.Input(key='-PROVID-')],
        [sg.Button('Ver'),sg.Button('Atras')]
    ]
   
    window = sg.Window('Provincia', layout,element_justification='r')

    
    try:
        while True:
            event, values = window.read()
            if event == "Atras" or event == sg.WIN_CLOSED:
                break
            elif event == 'Ver':
                idPRO=values['-PROVID-']
                prov_count = Provincia.get_num_provincia()
                variable=prov_count[idPRO][1]
                popup_message = "La cantidad de conexiones para la region seleccionada es de: " +str(variable)
                sg.popup(popup_message)
                window.close()  
        window.close()
    except Exception:
        popup_message = "Debe introducir ID valido para una provincia con al menos 1 conexión"
        sg.popup(popup_message)    
    window.close()


if __name__ == '__main__':    
    inputPROV()