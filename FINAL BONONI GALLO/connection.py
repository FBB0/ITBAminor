import csv
import datetime


class Connection():
    connections_dict = dict()  # open connections
    total_connections_dict = dict()  # all connections open and closed
    computers_dict = dict()

    def __init__(self, acces_point, start_time, mac, ip):
        if len(acces_point.ip_set) > 0:
            self.IP = ip
            self.mac = mac
            self.acces_point = acces_point  # router
            self.start_time = start_time
            self.router_id = acces_point.id
            #acces_point.num_connections += 1
            self.connection_id = str(
                self.IP)+str(self.mac)+str(self.acces_point.id)
            self.timed_connection_id = self.connection_id + \
                str(self.start_time)

        else:
            print("There are more than 20 computers connected")

    def add_connection(self):

        Connection.connections_dict.update({self.connection_id: self})
        self.acces_point.connected_mac.add(self.mac)
        Connection.computers_dict.update(
            {self.mac: [self.mac, self.acces_point, self.IP]})
       # return Connection.connections_dict, Connection.computers_dict

    def add_to_total(self):
        Connection.total_connections_dict.update(
            {self.timed_connection_id: self})

    # deletes connection between computer and router

    def delete_connection(connection_name):
        print("--", Connection.connections_dict.get(connection_name))
        self = Connection.connections_dict.get(connection_name)
        Connection.connections_dict.pop((connection_name))

        #self.acces_point.num_connections -= 1
        self.acces_point.ip_set.add(self.IP)
        self.acces_point.connected_mac.remove(self.mac)
        print(Connection.computers_dict)
        print("\n\n---------------")
        Connection.computers_dict.pop(self.mac)
        print("\n\n---------------")
        print(Connection.computers_dict)
        self.IP = None

        # return Connection.connections_dict, Connection.computers_dict, Connection.total_connections_dict

    def arrayVIEW():
        array = []
        print(Connection.connections_dict)
        for key in Connection.connections_dict:
            list = []
            list.append(Connection.connections_dict[key].mac)
            list.append(Connection.connections_dict[key].acces_point.id)
            list.append(Connection.connections_dict[key].connection_id)
            array.append(list)
        return array

    def save_connections_to_csv(filename, dictionary):
        fieldnames = ["connection_id", "IP", "MAC", "router id",
                      "start time"]

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for key, value in dictionary.items():
                print(value)
                writer.writerow(
                    {'connection_id': key, 'IP': value.IP, 'MAC': value.mac, "router id": value.router_id, "start time": value.start_time})
