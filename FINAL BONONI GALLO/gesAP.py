import PySimpleGUI as sg
from ingresarAP import ingresarAP
from ingresarCSV import cargaCSV
from verAP import tabla
import csv
from router import Router
from municipios import *


def readNEW(dictionary):

    id = dictionary.get('-ID-')
    identificador = dictionary.get('-IDENT-')
    ubicacion = dictionary.get('-UBI-')
    latitud = dictionary.get('-LAT-')
    longitud = dictionary.get('-LON-')
    municipio_id = dictionary.get('-MUNID-')
    provincia_id = dictionary.get('-PROVID-')
    id_departamento = dictionary.get('-DEPID-')
    if id not in Router.router_dict:
        if provincia_id in Provincia.provincia_dict:
            if id_departamento in Departamento.departamento_dict:
                if municipio_id in Municipio.municipio_dict:
                    r1 = Router(id, identificador, ubicacion, latitud, longitud,
                                municipio_id, provincia_id, id_departamento)
                else:
                    popup_message = "Municipio no existe"
                    sg.popup(popup_message)
            else:
                popup_message = "Departamento no existe"
                sg.popup(popup_message)
        else:
            popup_message = "Provincia no existe"
            sg.popup(popup_message)
    else:
        popup_message = "El Punto de Acceso ya existe"
        sg.popup(popup_message)


def gesAP():
    layout = [
        [sg.Button('Ingresar nuevo punto de acceso')],
        [sg.Button('Ingresar CSV')],
        [sg.Button('Eliminar punto de acceso')],
        [sg.Button('Atras')]
    ]

    window = sg.Window('Gestionar Puntos de Acceso', layout,
                       size=(400, 200), element_justification='c')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Atras':
            break
        elif event == 'Ingresar nuevo punto de acceso':
            valores = ingresarAP()
            try:
                readNEW(valores)
            except Exception:
                popup_message = "No se creo ningun nuevo punto de acceso"
                sg.popup(popup_message)
        elif event == 'Ingresar CSV':
            file = cargaCSV()
            try:
                with open(file, 'r') as csvfile:
                    csvwriter = csv.DictReader(csvfile)
                    for lines in csvwriter:
                        r1 = Router(lines.get("id"), lines.get("identificador"),
                                    lines.get("ubicacion"), lines.get(
                                        "latitud"),
                                    lines.get("longitud"), lines.get(
                                        "municipio_id"),
                                    lines.get("provincia_id"), lines.get("id_departamento"))
                # Creates wrong router object, confuses validation

                # print(Router.router_dict.values())
                # print(Router.router_dict.values()==[])
                # if Router.router_dict.values()==[]:
                #     popup_message = "El archivo seleccionado no cumple con el formato"
                #     sg.popup(popup_message)
            except Exception:
                popup_message = "No se cargo"
                sg.popup(popup_message)
        elif event == 'Eliminar punto de acceso':
            AP = tabla(Router.arrayVIEW())
            try:
                Router.delete_router(AP)
            except Exception:
                popup_message = "No se elimino ningun punto de acceso"
                sg.popup(popup_message)
    window.close()


if __name__ == '__main__':
    gesAP()
