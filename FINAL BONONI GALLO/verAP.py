import PySimpleGUI as sg

#Datos has to be a list of lists with the strings we want to show, first column has to be reouter ID
#Best option is to import Router class and use a class method to create a single use list of lists with the fields, could be a lambda function in the tabla function call

def tabla(datos=[
        ['1067', 'BUE056-06', '', '-34.742.506', '-60.991.765', 'BUE056','AR-B', '1250'],
        ['867', 'XWR6-06', '', '-34.742.506', '-60.991.765', 'BUE056','AR-B', '1250']
    ], 
          headings=['id','identificador','ubicacion','latitud','longitud','municipio_id','provincia_id','id_departamento']):

    layout = [
        [sg.Text('Seleccione el Punto de acceso que quiere eliminar')],
        [sg.Table(values=datos, headings=headings, max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=False,
                    justification='right',
                    num_rows=10,
                    enable_events=True,
                    key='-tabla-',
                    row_height=35,
                    tooltip='Tabla')],
        [sg.Button('Seleccionar'),sg.Button('Atras')]
    ]

    window = sg.Window("Lista", 
    layout, modal=True)

    try:
        while True:
            event, values = window.read()
            if event == "Atras" or event == sg.WIN_CLOSED:
                break
            elif event == '-tabla-':
                selected_index = values['-tabla-'][0]
                selected_row = datos[selected_index]
                popup_message = "Esta por eliminar el Punto de Acceso con ID: " + selected_row[0] + ' \nSi desea continuar presione OK y luego seleccionar'
                sg.popup(popup_message)
            elif event == 'Seleccionar':
                window.close()
                return selected_row[0]
        window.close()
    except Exception:
        popup_message = "Debe seleccionar algun Punto de acceso"
        sg.popup(popup_message)


if __name__ == '__main__':    
    tabla()