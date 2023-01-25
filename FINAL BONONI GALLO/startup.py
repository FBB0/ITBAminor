import csv
from municipios import Municipio, Departamento, Provincia
from connection import Connection
from router import Router


def starting_up():
    try:
        with open("municipios.csv", 'r') as csvfile:
            csvwriter = csv.DictReader(csvfile)
            for lines in csvwriter:
                print(lines)
                # there are some municipios without municipio_id
                # municipio_id,provincia_id,id_departamento,municipio,provincia,departamento
                m = Municipio(lines.get("municipio_id"), lines.get("provincia_id"), lines.get(
                    "id_departamento"), lines.get("municipio"), lines.get("provincia"), lines.get("departamento"))
                d = Departamento(lines.get("provincia_id"), lines.get(
                    "id_departamento"), lines.get("provincia"), lines.get("departamento"))
                p = Provincia(lines.get("provincia_id"),
                              lines.get("provincia"))
    except Exception:
        None

    try:
        with open("routers.csv", 'r') as csvfile:
            # creating a csv writer object
            csvwriter = csv.DictReader(csvfile)
            for lines in csvwriter:
                # print(lines)
                if lines.get("provincia_id") in Provincia.provincia_dict:
                    if lines.get("id_departamento") in Departamento.departamento_dict:
                        if lines.get("municipio_id") in Municipio.municipio_dict:
                            r1 = Router(lines.get("id"), lines.get("identificador"), lines.get("ubicacion"), lines.get("latitud"), lines.get(
                                "longitud"), lines.get("municipio_id"), lines.get("provincia_id"), lines.get("id_departamento"))
                        else:
                            print("municipio_id does not exist")
                    else:
                        print("id_departamento does not exist")
                else:
                    print("Provincia_id does not exist")

    except Exception:
        None

    try:
        # Connection.total_connections_dict, Connection.connections_dict, Connection.computers_dict =
        Router.online_connections("connections.csv")

    except Exception:
        None
    try:

        # Connection.computers_dict, Connection.total_connections_dict =
        Router.old_connections("total_connections.csv",
                               Connection.computers_dict)
    except Exception:
        None
