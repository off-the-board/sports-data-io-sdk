import socket
import json


def get_free_port():
    s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind(("localhost", 0))
    address, port = s.getsockname()
    s.close()
    return port


def load_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data
