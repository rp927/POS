from netconnect import *

if __name__ == '__main__':
    host = 'localhost'
    port = 6667
    connect = NetConnect(host, port)
    connect.client_server()