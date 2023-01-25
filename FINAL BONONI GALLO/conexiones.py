import PySimpleGUI as sg
from nuevaconexion import tablaAPs
from desconectar import tablaConexiones
from conexionEnTiempos import inputTiempos
from verCantCon import cantCon
from connection import Connection

from router import Router
import datetime


def menuConexiones():
    layout = [
        [sg.Button('Nueva conexion')],
        [sg.Button('Desconectar')],
        [sg.Button('Ver numero de conexiones activas en una region')],
        [sg.Button('Ver conexiones dentro de un lapso de tiempo')],
        [sg.Button('Atras')]
    ]

    window = sg.Window('Conexiones', layout, size=(
        400, 200), element_justification='c')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Atras':
            break
        elif event == 'Nueva conexion':
            try:
                idAP, MAC = tablaAPs(Router.arrayVIEW())
                if idAP not in Router.router_dict:
                    popup_message = "El punto de acceso ingresado no existe"
                    sg.popup(popup_message)
                elif MAC in Connection.computers_dict:
                    popup_message = "El MAC ingresado ya existe"
                    sg.popup(popup_message)
                else:

                    time_now = datetime.datetime.now()
                    IP = Router.router_dict[idAP].ip_set.pop()
                    con = Connection(
                        Router.router_dict[idAP], time_now, MAC, IP)
                    # Connection.total_connections_dict, Connection.connections_dict, Connection.computers_dict =
                    con.add_connection()
                    con.add_to_total()
            except Exception:
                popup_message = "No se pudo conectar"
                sg.popup(popup_message)
        elif event == 'Desconectar':
            try:
                ID_Conexion = tablaConexiones(Connection.arrayVIEW())

                # Connection.connections_dict, Connection.computers_dict, Connection.total_connections_dict =

                Connection.delete_connection(ID_Conexion)

            except Exception:
                None
        elif event == 'Ver numero de conexiones activas en una region':
            cantCon()
        elif event == 'Ver conexiones dentro de un lapso de tiempo':

            inputTiempos()

    window.close()


if __name__ == '__main__':
    menuConexiones()
