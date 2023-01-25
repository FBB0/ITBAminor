
from connection import Connection
import csv
import datetime


class Router():
    router_dict = dict()

    def __init__(self, id, identificador, ubicacion, latitud, longitud, municipio_id, provincia_id, id_departamento):
        self.id = str(id)
        self.identificador = str(identificador)
        self.ubicacion = str(ubicacion)
        self.latitud = str(latitud)
        self.longitud = str(longitud)
        self.municipio_id = str(municipio_id)
        self.provincia_id = str(provincia_id)
        self.id_departamento = str(id_departamento)

        self.ip_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                       11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
        self.num_connections = 20-len(self.ip_set)
        self.connected_mac = set()

        Router.router_dict.update({self.id: (self)})

    # probably use a dictionary to store as the max is 20 connections, does not make it useful to use a tree

    # add and quit router, adding is already done in line 20
    # def agregar_router(self):
       # self.num_connections += 1

    # if a router is deleted, delete it from the dict of routers and all connections must be deleted
    def arrayVIEW():
        array = []
        for key in Router.router_dict:
            list = []
            list.append(Router.router_dict[key].id)
            list.append(Router.router_dict[key].identificador)
            list.append(Router.router_dict[key].ubicacion)
            list.append(Router.router_dict[key].latitud)
            list.append(Router.router_dict[key].longitud)
            list.append(Router.router_dict[key].municipio_id)
            list.append(Router.router_dict[key].provincia_id)
            list.append(Router.router_dict[key].id_departamento)
            array.append(list)
        return array

    def delete_router(id):

        print("------", Router.router_dict[id].connected_mac)
        print(Connection.computers_dict)
        for i in Router.router_dict[id].connected_mac:
            IP = Connection.computers_dict[i][2]
            acces_point = Connection.computers_dict[i][1]
            connection_name = str(Connection.computers_dict[i][2])+str(
                Connection.computers_dict[i][0])+str(Connection.computers_dict[i][1].id)
            print(connection_name)
            # Connection.connections_dict, Connection.computers_dict = Connection.delete_connection(
            #     connection_name)
            Connection.connections_dict.pop(connection_name)
        Router.router_dict.pop(id)

    def dict_router_to_csv(filename, dictionary):
        fieldnames = ["id", "identificador", "ubicacion", "latitud",
                      "longitud", "municipio_id", "provincia_id", "id_departamento"]
        with open(filename, 'w', newline='') as csvfile:

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for key, value in dictionary.items():
                # print(value)
                writer.writerow(
                    {'id': key, 'identificador': value.identificador, 'ubicacion': value.ubicacion, "latitud": value.latitud, "longitud": value.longitud, "municipio_id": value.municipio_id, "provincia_id": value.provincia_id, "id_departamento": value.id_departamento})

    def online_connections(filename):
        with open(filename, 'r') as csvfile:
            # creating a csv writer object

            csvwriter = csv.DictReader(csvfile)
            for lines in csvwriter:
                #print(Router.router_dict[lines.get("router id")])
                acces_point = Router.router_dict[lines.get("router id")]

                if len(acces_point.ip_set) > 0:
                    print(lines.get("IP"))

                    IP = int(lines.get("IP"))
                    acces_point.ip_set.remove(IP)
                    con1 = Connection(Router.router_dict[lines.get(
                        "router id")], lines.get("start time"), lines.get("MAC"), IP)

                    # Connection.total_connections_dict, Connection.connections_dict, Connection.computers_dict =
                    con1.add_connection()

                else:
                    print("There are already 20 computers connected")
        # return Connection.total_connections_dict,  Connection.connections_dict, Connection.computers_dict

    def old_connections(filename, dict):
        with open(filename, 'r') as csvfile:
            # creating a csv writer object
            csvwriter = csv.DictReader(csvfile)
            for lines in csvwriter:
                print("Line:", lines)
                acces_point = Router.router_dict[lines.get("router id")]

                start_time = lines.get("start time")
                mac = lines.get("MAC")
                con1 = Connection(acces_point,
                                  start_time, mac, lines.get("IP"))
                # Connection.total_connections_dict, Connection.connections_dict, Connection.computers_dict =
                # con1.add_connection()
                #Connection.connections_dict, Connection.computers_dict, Connection.total_connections_dict = con1.delete_connection()
                con1.add_to_total()

        # return Connection.computers_dict, Connection.connections_dict


if __name__ == '__main__':
    print(Router.arrayVIEW())
