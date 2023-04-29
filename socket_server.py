from datetime import datetime
import json
import socket
import urllib.parse


def run_server(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server = ip, port
        sock.bind(server)
        data, addr = sock.recvfrom(1024)

        saved_json_file = read_json_file()
        converted_data = convert_form_data_to_dict(data)
        saved_json_file[str(datetime.now())] = converted_data
        write_json_to_file(saved_json_file)


def convert_form_data_to_dict(data):
    data_parse = urllib.parse.unquote_plus(data.decode())
    data_dict = {key: value for key, value in [
        el.split('=') for el in data_parse.split('&')]}
    return data_dict


def read_json_file():
    with open('storage/data.json', 'r') as fr:
        result = json.loads(fr.read())
    return result


def write_json_to_file(data):
    with open('storage/data.json', 'w') as fw:
        json.dump(data, fw)
