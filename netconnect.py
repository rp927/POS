import socket
from pathlib import Path
import sys


class NetConnect:
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port

    def set_hostname(self, hostname):
        self.hostname = hostname

    def set_message(self, message):
        self.message = bytes(message, encoding="utf-8")

    def get_hostname(self):
        return self.hostname

    def get_port(self):
        return self.port

    def get_message(self):
        if self.message:
            return self.message
        else:
            return

    def send_message(self,sock,message,ip,port):
        sock.sendto(message,(ip,port))

    def rec_message(self,sock):
        data, addr = sock.recvfrom(1024)
        return data, addr

    def message_generator(self,message):
        orig_stdout = sys.stdout
        file = open('text.txt','w')
        sys.stdout = file
        if '.py' in message or '.c' in message:
            exec(Path(f'toolkit/{message}').read_text())
        else:
            print(message)
        file.close()
        sys.stdout = orig_stdout
        file = open("text.txt")
        read = file.read()
        return read


    def client(self,message = "Connection Established"):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        name = self.hostname
        port = int(self.port)
        self.send_message(sock,message.encode(),name,port)


    def server(self):
        name = self.hostname
        port = int(self.port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((name,port))
        while True:
            data, addr = sock.recvfrom(1024)
            while data != None:
                print(data.decode())
                message = data.decode()
                message = self.message_generator(message)
                self.send_message(sock, message.encode(), name, 6667)
                data = None

    def client_server(self):
        name = self.hostname
        port = int(self.port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((name,port))
        while True:
            data, addr = sock.recvfrom(1024)
            while data != None:
                print(data.decode())
                self.message_generator(data.decode())
                data = None


