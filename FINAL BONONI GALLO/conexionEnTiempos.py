import PySimpleGUI as sg
import datetime
from connection import Connection


def inputTiempos():
    layout = [[
        sg.Text(
            'Ingrese tiempo de inicio y de finalizacion para el intervalo deseado')
    ],
        [
        sg.CalendarButton("Fecha de inicio",
                          close_when_date_chosen=True,
                          target='-INICIOFECHA-',
                          no_titlebar=False,
                          format='%d/%m/%Y'),
        sg.Input(key='-INICIOFECHA-', size=(10, 1))
    ],
        [
        sg.Text('Horario (HH:MM)'),
        sg.Input(key='-INICIOHORARIO-', size=(10, 1))
    ],
        [
        sg.CalendarButton("Fecha de finalizacion",
                          close_when_date_chosen=True,
                          target='-FINFECHA-',
                          no_titlebar=False,
                          format='%d/%m/%Y'),
        sg.Input(key='-FINFECHA-', size=(10, 1))
    ],
        [
        sg.Text('Horario (HH:MM)'),
        sg.Input(key='-FINHORARIO-', size=(10, 1))
    ], [sg.Button('Confirmar'),
            sg.Button('Atras')]]

    window = sg.Window('Calendar', layout, element_justification='r')

    # try:
    while True:
        event, values = window.read()
        if event == "Atras" or event == sg.WIN_CLOSED:
            break
        elif event == 'Confirmar':
            try:
                strinicio = values['-INICIOFECHA-'] + \
                    ' ' + values['-INICIOHORARIO-']
                strfin = values['-FINFECHA-'] + ' ' + values['-FINHORARIO-']
                popup_message = "Selecciono:" + strinicio + '\ty ' + strfin
                sg.popup(popup_message)
                mayor_menor_lst = list()
                inicio = str(datetime.datetime.strptime(
                    strinicio, "%d/%m/%Y %H:%M"))
                fin = str(datetime.datetime.strptime(strfin, "%d/%m/%Y %H:%M"))

                print(Connection.total_connections_dict)
                for i in Connection.total_connections_dict.values():
                    print(i, i.start_time, type(i.start_time))
                    print(fin, type(fin))
                    if str(fin) >= str(i.start_time) and str(inicio) <= str(i.start_time):
                        mayor_menor_lst.append((i.connection_id, i.start_time))

                conexionesEnTiempo(datos=mayor_menor_lst)
            except Exception:
                popup_message = "The time was entered incorrectly"
                sg.popup(popup_message)

            window.close()
    window.close()
    # except Exception:
    # popup_message = "Debe seleccionar fechas y horarios validos, la primera debe ser anterior a la segunda"
    # sg.popup(popup_message)
    # window.close()


# Datos has to be a list of lists with the strings we want to show, already filtered by time


def conexionesEnTiempo(datos=[['2022-12-12 10:39:47.709717', '1aaa1224'], ['2022-12-12 10:40:04.239883', '2bbb1224'], ['2022-12-12 10:40:11.786330', '331224'], ['2022-12-12 10:40:16.202797', '441224'], ['2022-12-12 10:40:20.648505', '551224'], ['2022-12-12 10:40:54.377271', '1dfsd1224'], ['2022-12-12 11:47:23.814007', '1aaa1224']], headings=['Tiempo Inicio', 'ID_Conexion', ]):

    layout = [[sg.Text('Conexiones dentro del lapso introducido')],
              [
        sg.Table(values=datos,
                 headings=headings,
                 max_col_width=35,
                 auto_size_columns=True,
                 display_row_numbers=False,
                 justification='right',
                 num_rows=10,
                 enable_events=True,
                 key='-tabla-',
                 row_height=35,
                 tooltip='Tabla')
    ], [sg.Button('Atras')]]

    window = sg.Window("Lista", layout, modal=True)

    while True:
        event, values = window.read()
        if event == "Atras" or event == sg.WIN_CLOSED:
            break
        elif event == '-tabla-':
            selected_index = values['-tabla-'][0]
            selected_row = datos[selected_index]
            popup_message = "ID: " + selected_row[1]
            sg.popup(popup_message)
    window.close()


if __name__ == '__main__':
    conexionesEnTiempo()
