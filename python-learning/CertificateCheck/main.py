import yaml
import ssl
import socket
from datetime import datetime
from prettytable import PrettyTable
import os
import shutil

Days = []
table = PrettyTable()
CertificateInfo = []


def cert_check_for_expiry(filename):
    with open(filename, 'r') as stream:
        try:
            yaml_data = yaml.safe_load(stream)

        except yaml.YAMLError as exc:

            print(exc)

    for i in yaml_data.get('verifyurl'):
        if i.get('url').count(":") == 2:
            port = int((i.get('url').replace("//", "")).split(":")[-1])
            server = (i.get('url').replace("//", "")).split(":")[-2]
        else:
            port = 443
            server = (i.get('url').replace("//", "")).split(":")[-1]
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=server) as s:
            try:
                s.connect((server, port))
                cert = s.getpeercert()
                subject = dict(x[0] for x in cert['subject'])
                expirydate = datetime.strptime(cert.get('notAfter'), '%b %d %H:%M:%S %Y %Z')
                expirydate.strftime('%d/%m/%Y')
                daysleft = expirydate - datetime.today()
                cert_dict = {}
                cert_dict['CertificateName'] = subject.get('commonName')
                cert_dict['Server'] = server
                cert_dict['Port'] = port
                cert_dict['DaysLeftForExpiration'] = daysleft.days
                cert_dict['ExpiryDate'] = expirydate.strftime('%m/%d/%Y')
                cert_dict['DateToday'] = datetime.today().strftime('%m/%d/%Y')
            except:
                print(f'{server} unreachable on port {port}')
        CertificateInfo.append(cert_dict)
        Days.append(cert_dict['DaysLeftForExpiration'])
    for i in Days:
        if i <= 30:
            print("The certificate needs immediate attention on backend nodes")
            for i in CertificateInfo:
                table.field_names = i.keys()
                table.add_row(i.values())
            print(table)
    if len(set(Days)) == 1:
        print("Certificate is consistent across all the backend nodes and needs immediate action....")
        del Days[:]
    else:
        print("Certificate is inconsistent on the backend node with respect to other nodes in SANS")
        maxdate = max(Days)
        del Days[:]
        print(f"The actual date of expiration is {maxdate}")
        for i in CertificateInfo:
            if i.get('DaysLeftForExpiration') != maxdate:
                table.field_names = i.keys()
                table.add_row(i.values())
        print(table)


def directory_to_traverse():
    source_directory = "C://Users//mmamidibat//repos//Mahesh_Learning//python//python programs//Certyaml"
    destination_directory = os.getcwd()
    for filename in os.listdir(source_directory):
        source_file = os.path.join(source_directory, filename)
        destination_file = os.path.join(destination_directory, filename)
        shutil.copy(source_file, destination_file)
        cert_check_for_expiry(destination_file)
        os.remove(destination_file)


directory_to_traverse()
