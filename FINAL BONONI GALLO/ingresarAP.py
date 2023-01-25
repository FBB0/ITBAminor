import PySimpleGUI as sg

def ingresarAP():
    layout = [  [sg.Text('ID*'), sg.Input(key='-ID-')],
                [sg.Text('Identificador*'), sg.Input(key='-IDENT-')],
                [sg.Text('Ubicacion'), sg.Input(key='-UBI-')],
                [sg.Text('Latitud*'), sg.Input(key='-LAT-')],
                [sg.Text('Longitud*'), sg.Input(key='-LON-')],
                [sg.Text('ID Municipio*'), sg.Input(key='-MUNID-')],
                [sg.Text('ID Provincia*'), sg.Input(key='-PROVID-')],
                [sg.Text('ID Departamento*'), sg.Input(key='-DEPID-')],
                [sg.Button('Crear'),sg.Button('Atras')]
    ]

    window = sg.Window('Ingresar nuevo punto de acceso', layout, element_justification='r')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Atras':
            break
        elif event=='Crear':
            if values['-ID-'] == '' or values['-IDENT-'] == '' or values['-LAT-'] == '' or values['-LON-'] == '' or values['-MUNID-'] == '' or values['-PROVID-'] == '' or values['-DEPID-'] == '':
                mensaje='Los campos con * no pueden quedar vacios'
                sg.popup(mensaje)
                break
            valoresAP=values
            window.close()
            return valoresAP
    window.close()
    