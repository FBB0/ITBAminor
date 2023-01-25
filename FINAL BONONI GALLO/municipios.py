import csv
from connection import Connection


class Provincia():
    provincia_dict = dict()

    def __init__(self, provincia_id, provincia):
        self.provincia_id = provincia_id
        self.provincia = provincia
        Provincia.provincia_dict.update({self.provincia_id: self})

    def get_num_provincia():
        num_prov_dict = dict()
        num_dept_dict = Departamento.get_num_departamento()
        print(num_dept_dict.items())
        for key, value in num_dept_dict.items():
            specific_provincia = value[1]
            if specific_provincia in num_prov_dict:
                num = num_prov_dict.get(specific_provincia)[1]
                num_prov_dict.update(
                    {specific_provincia: [value[1], num+value[2]]})
            else:
                num_prov_dict.update(
                    {specific_provincia: [value[1], value[2]]})

        return num_prov_dict


class Departamento():
    departamento_dict = dict()

    def __init__(self, provincia_id, id_departamento, provincia, departamento):
        self.provincia_id = provincia_id
        self.provincia = provincia
        self.id_departamento = id_departamento
        self.departamento = departamento
        Departamento.departamento_dict.update({self.id_departamento: self})

    def get_num_departamento():
        num_dept_dict = dict()
        num_mun_dict = Municipio.get_num_municipios()

        for key, value in num_mun_dict.items():
            specific_departamento = value[1]+value[2]
            if specific_departamento in num_dept_dict:
                num = num_dept_dict.get(specific_departamento)[2]
                num_dept_dict.update(
                    {specific_departamento: [value[1], value[2],  num+value[3]]})
            else:
                num_dept_dict.update(
                    {specific_departamento: [value[1], value[2], value[3]]})
        return num_dept_dict


class Municipio():
    municipio_dict = dict()

    def __init__(self, municipio_id, provincia_id, id_departamento, municipio, provincia, departamento):
        self.provincia_id = provincia_id
        self.provincia = provincia
        self.departamento = departamento
        self.id_departamento = id_departamento
        self.municipio = municipio

        self.num_municipio = 0

        Municipio.municipio_dict.update({municipio_id: self})

    def get_num_municipios():
        num_mun_dict = dict()
        counted_routers = set()
        print("Coonect\n")
        print(Connection.connections_dict.items())
        for key, value in Connection.connections_dict.items():
            specific_municipio = str(value.acces_point.municipio_id)+str(
                value.acces_point.id_departamento)+str(value.acces_point.provincia_id)

            if specific_municipio in num_mun_dict and value.acces_point.id not in counted_routers:

                num = num_mun_dict.get(specific_municipio)[3]
                print("------------", num)
                num_mun_dict.update(
                    {specific_municipio: [value.acces_point.municipio_id, value.acces_point.id_departamento, value.acces_point.provincia_id, num+(20-len(value.acces_point.ip_set))]})  # changed

            elif specific_municipio not in num_mun_dict:
                counted_routers.add(value.acces_point.id)
                print(2, specific_municipio, 20-len(value.acces_point.ip_set),
                      value.acces_point.ip_set, len(value.acces_point.ip_set))
                counted_routers.add(value.acces_point.id)
                num_mun_dict.update(
                    {specific_municipio: [value.acces_point.municipio_id, value.acces_point.id_departamento, value.acces_point.provincia_id, 20-len(value.acces_point.ip_set)]})  # changed
        print(counted_routers)
        return num_mun_dict

    def get_municipios_from_csv(filename):
        with open(filename, 'r') as csvfile:
            # creating a csv writer object
            csvwriter = csv.DictReader(csvfile)
            for lines in csvwriter:
                # print(lines)
                m1 = Municipio(lines.get("municipio_id"), lines.get("provincia_id"), lines.get(
                    "id_departamento"), lines.get("municipio"), lines.get("provincia"), lines.get("departamento"))
                p1 = Provincia(lines.get("provincia_id"),
                               lines.get("provincia"))
                d1 = Departamento(lines.get("provincia_id"), lines.get(
                    "id_departamento"), lines.get("provincia"), lines.get("departamento"))

    def write_municipios_to_csv(filename, dictionary):
        fieldnames = ["id", "identificador", "ubicacion", "latitud", "longitud",
                      "municipio_id", "provincia_id", "id_departamento", "connections"]
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for key, value in dictionary.items():
                # print(value)
                writer.writerow(
                    {'id': key, 'identificador': value.get("identificador"), 'ubicacion': value.get("ubicacion"), "latitud": value.get("latitud"), "longitud": value.get("longitud"), "municipio_id": value.get("municipio_id"), "provincia_id": value.get("provincia_id"), "id_departamento": value.get("id_departamento")})


# Municipio.get_municipios_from_csv("municipios.csv")
