import PySimpleGUI as sg
from router import Router
import csv
from municipios import *
import os


def cargaCSV():
    layout = [
        [sg.T("")], [sg.Text("Seleccione CSV: "), sg.Input(),
                     sg.FileBrowse(file_types=(('.csv', '*.csv'),), key="-IN-")],
        [sg.Button("Ingresar"), sg.Button('Atras')]
    ]

    window = sg.Window('Crga de CSV', layout, size=(550, 200))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Atras":
            break
        elif event == "Ingresar":

            window.close()
            archivo = values["-IN-"].replace('/', '\\')
            print(archivo, type(archivo))
            # try:
            count = 0
            with open(archivo, 'r') as inp, open('archivo_edit.csv', 'w', newline='') as out:
                fieldnames = ["id", "identificador", "ubicacion", "latitud",
                              "longitud", "municipio_id", "provincia_id", "id_departamento"]
                writer = csv.writer(out)
                reader = csv.DictReader(inp, fieldnames)
                print(reader)
                writer.writerow(fieldnames)
                for lines in reader:

                    if count > 0:
                        if lines.get("id") in Router.router_dict:
                            popup_message = " Router id in line " + \
                                str(count)+" of the csv file already exist."
                            sg.popup(popup_message)
                        if lines.get("provincia_id") not in Provincia.provincia_dict:
                            popup_message = "Provincia id in line " + \
                                str(count)+" of the csv file is entered wrong."
                            sg.popup(popup_message)
                        if lines.get("id_departamento") not in Departamento.departamento_dict:
                            popup_message = "id_departamento in line " + \
                                str(count)+" of the csv file is entered wrong."
                            sg.popup(popup_message)
                        if lines.get("municipio_id") not in Municipio.municipio_dict:
                            popup_message = "municipio_id in line " + \
                                str(count)+" of the csv file is entered wrong."
                            sg.popup(popup_message)

                        if lines.get("id") not in Router.router_dict:
                            if lines.get("provincia_id") in Provincia.provincia_dict:
                                if lines.get("id_departamento") in Departamento.departamento_dict:
                                    if lines.get("municipio_id") in Municipio.municipio_dict:
                                        writer.writerow([lines.get("id"), lines.get("identificador"), lines.get("ubicacion"), lines.get("latitud"), lines.get(
                                            "longitud"), lines.get("municipio_id"), lines.get("provincia_id"), lines.get("id_departamento")])
                                        #print("---------------", lines)
                                        r1 = Router(lines.get("id"), lines.get("identificador"), lines.get("ubicacion"), lines.get("latitud"), lines.get(
                                            "longitud"), lines.get("municipio_id"), lines.get("provincia_id"), lines.get("id_departamento"))

                    count += 1

                # except Exception:
                #     popup_message = "No se pudo addicionar"
                #     sg.popup(popup_message)
                archivo = 'archivo_edit.csv'
                # os.remove('archivo_edit.csv')

            return archivo

    window.close()


if __name__ == '__main__':
    archivo = cargaCSV()

    print(archivo)
