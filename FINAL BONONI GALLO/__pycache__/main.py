from router import Router
import time
import datetime
from connection import Connection
from load_data import readcsvrouters
import csv
from municipios import Municipio, Provincia, Departamento


if __name__ == '__main__':

    print(starting_up())
    # print(Connection.computers_dict)
    running = True
    print(
        "Welcome to the wifi system. The given cvs-file has already been loaded in.")
    while running == True:
        print(
            "What do you want to do?\n1. Import routers from csv-file\n2. Add router\n3. Add computer connection \n4. Delete computer connection \n5.Find the  connections of a router"
        )
        print(
            "6. All connections\n7. Number of connections in a municipio\n8. Number of connections in a departamento"
        )
        print(
            "9. Number of connections in a provincia\n10. all connections between certain times "
        )
        question = int(input(""))
        if question == 0:
            running = False
        elif question == 1:
            try:
                file = input("csv_filename:")  # change to ui
                with open(file, 'r') as csvfile:
                    # creating a csv writer object
                    csvwriter = csv.DictReader(csvfile)
                    for lines in csvwriter:
                        print(lines)
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
            except:
                print("The inputted file cannot be found")
                #raise ValueError("The inputted file cannot be found")
        elif question == 2:
            # change to ui
            id = input("id: ")
            identificador = input("identificador: ")
            ubicacion = input("ubicacion: ")
            latitud = input("latitud: ")
            longitud = input("longitud: ")
            municipio_id = input("municipio_id: ")
            provincia_id = input("provincia_id")
            id_departamento = input("id_departamento")
            if id not in Router.router_dict:
                # print(Provincia.provincia_dict)
                if provincia_id in Provincia.provincia_dict:
                    if id_departamento in Departamento.departamento_dict:
                        if municipio_id in Municipio.municipio_dict:
                            r1 = Router(id, identificador, ubicacion, latitud, longitud,
                                        municipio_id, provincia_id, id_departamento)
                        else:
                            print("Municipio does not exist.")
                    else:
                        print("Departamento does not exist.")
                else:
                    print("Provincia does not exist")
            else:
                print("The router id already exists.")
        elif question == 3:
            mac = input("MAC: ")
            router_id = input("router id: ")

            if mac not in Connection.computers_set and router_id in Router.router_dict:
                r1 = Router.router_dict[str(router_id)]
                time_now = datetime.datetime.now()
                c1 = Connection(r1, time_now, mac)

            else:
                print(
                    "Either the MAC does already exist or the router id does not yet exist"
                )
        elif question == 4:
            mac = input("MAC: ")
            if mac in Connection.computers_set:

                c1 = Connection.connections_dict[(mac)]
                c1.delete_connection()
            else:
                print("MAC is not connected to any router")
        elif question == 5:
            router_id = input("router id")
            if router_id in Router.router_dict:
                r1 = Router.router_dict[str(router_id)]

                print(r1.connected_mac)
            else:
                print("Router does not exist")
        elif question == 6:
            print(Connection.connections_dict)

        elif question == 7:
            mun_count = Municipio.get_num_municipios()
            print(mun_count)
            chosen_mun = input("municipio_id")
            chosen_dep = input("departamento_id")
            chosen_prov = input("id_provincia")
            chosen = chosen_mun + chosen_prov + chosen_dep
            print(chosen)
            if chosen in mun_count:
                print(mun_count[chosen])
            else:
                print(
                    "Chosen municipio_id, departamento_id and provincia_id does not exist or has 0 connections"
                )

        elif question == 8:
            dep_count = Departamento.get_num_departamento()
            print(dep_count)
            chosen_dep = input("departamento_id")
            chosen_prov = input("id_provincia")
            chosen = chosen_dep + chosen_prov
            if chosen in dep_count:
                print(dep_count[chosen])
            else:
                print(
                    "Chosen combination of provincia_id and departamento_id does not exist or has 0 connections"
                )

        elif question == 9:
            prov_count = Provincia.get_num_provincia()
            print(prov_count)
            chosen_prov = input("id_provincia")
            chosen = chosen_prov
            if chosen in prov_count:
                print(prov_count[chosen])
            else:
                print("Chosen provincia_id does not exist or has 0 connections")
        elif question == 10:
            try:
                t = input("start time: (%d/%m/%Y %H:%M)")
                t_end = input("end time: (%d/%m/%Y %H:%M)")
                t_new = (datetime.datetime.strptime(t, "%d/%m/%Y %H:%M"))
                t2_new = (datetime.datetime.strptime(
                    t_end, "%d/%m/%Y %H:%M"))

                for i in Connection.total_connections_dict.values():
                    print(i.start_time, type(i.start_time))
                    if t2_new >= i.start_time and t_new <= i.start_time:
                        print(i.connection_id, i.start_time)

            except:
                print("One of the times was not entered correctly")
        elif question == 11:
            # add municipios
            print("mun")
        else:
            print("That made no sense to me, try again!")

    Connection.save_connections_to_csv("connections.csv",
                                       Connection.connections_dict)
    Connection.save_connections_to_csv("total_connections.csv",
                                       Connection.total_connections_dict)
    Router.dict_router_to_csv("routers.csv", Router.router_dict)
