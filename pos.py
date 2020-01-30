from pathlib import Path
from netconnect import *
import threading

class Server:
    def __init__(self,host,port):
        self.host = host
        self.port = port

    def run_server(self, host, port):
        connect = NetConnect(host, port)
        connect.server()

    def run_pos(self):
        exec(Path(f'POS/main.py').read_text())

    def run(self):
        t1 = threading.Thread(target=self.run_server, args=[self.host,self.port, ])
        t2 = threading.Thread(target=self.run_pos)
        t1.start()
        t2.start()

if __name__ == '__main__':
    host = 'localhost'
    port = 5555
    server = Server(host,port)
    server.run()


