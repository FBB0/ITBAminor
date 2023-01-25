from startup import starting_up
from menupp import *
from connection import Connection
from router import Router
from municipios import Municipio

Municipio.get_municipios_from_csv("municipios.csv")
starting_up()

menu()

print(Connection.total_connections_dict)
Connection.save_connections_to_csv("connections.csv",
                                   Connection.connections_dict)
Connection.save_connections_to_csv("total_connections.csv",
                                   Connection.total_connections_dict)
Router.dict_router_to_csv("routers.csv", Router.router_dict)
