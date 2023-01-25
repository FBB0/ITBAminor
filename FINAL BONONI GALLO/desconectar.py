import PySimpleGUI as sg

# Datos has to be a list of lists with the strings we want to show, first column has to be reouter ID
# Best option is to import Router class and use a class method to create a single use list of lists with the fields, could be a lambda function in the tabla function call


def tablaConexiones(datos=[
        ['AE39TP', '1067', '4AE39TP1067'],
        ['RT48DE', '867', '9RT48DE867']
    ],
        headings=['MAC', 'ID_PuntoAcceso', 'ID_Conexion']):

    layout = [
        [sg.Text('Seleccione la conexion que quiere eliminar')],
        [sg.Table(values=datos, headings=headings, max_col_width=35,
                  auto_size_columns=True,
                  display_row_numbers=False,
                  justification='right',
                  num_rows=10,
                  enable_events=True,
                  key='-tabla-',
                  row_height=35,
                  tooltip='Tabla')],
        [sg.Button('Seleccionar'), sg.Button('Atras')]
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
                popup_message = "Esta por desconectar el dispositivo con MAC: " + \
                    selected_row[0] + \
                    ' \nSi desea continuar presione OK y luego seleccionar'
                sg.popup(popup_message)
            elif event == 'Seleccionar':
                window.close()
                return selected_row[2]
        window.close()
    except Exception:
        popup_message = "Debe seleccionar alguna Conexion"
        sg.popup(popup_message)


if __name__ == '__main__':
    tablaConexiones()
