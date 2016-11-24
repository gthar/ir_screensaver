
import socket
from threadable import Threadable

class SocketHandler(Threadable):
    def __init__(self, port=10000, host='127.0.0.1', max_length=4096, **actions):
        self.actions = actions
        self.max_length = max_length
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(10)
        super().__init__()

    def loop(self):
        client_socket, _ = self.server_socket.accept()
        msg = client_socket.recv(self.max_length).decode()
        print(msg)
        try:
            self.actions[msg]()
        except KeyError:
            print("no action implemented for message '{0}'".format(msg))
