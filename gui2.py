from tkinter import ttk
import tkinter as tk
from netconnect import *
import glob
import datetime
import socket
import time

class GUI:
    def __init__(self,master):
        self.__master = master
        self.__master.title("Client")
        self.__master.geometry("800x600")


        '''Labels'''
        self.__label1 = tk.Label(self.__master,text="Enter IP Address:",font=('Arial',18))
        self.__label2 = tk.Label(self.__master, text="Enter Port: (4000-6552)", font=('Arial', 18))
        self.__label3 = tk.Label(self.__master,text="Returned Message: ",font=('Arial',18))
        self.__label4 = tk.Label(self.__master, text="OPTIONS", font=('Arial', 18))

        '''Entry'''
        self.__entry1 = tk.Entry(bd=5)
        self.__entry2 = tk.Entry(bd=5)

        '''Buttons'''
        self.__button1 = tk.Button(text="Connect",command=self.connect,bd=5)
        self.__button2 = tk.Button(text="Export to Text File", command=self.export, bd=5)
        self.__button3 = tk.Button(text="RUN", command=self.run, bd=5)

        '''Text Field'''
        self.__text1 = tk.Text(master=self.__master,height=10,width=90,bd=5)

        '''Combo Box'''
        self.__cb1 = ttk.Combobox(self.__master,values=self.combo_box_function())
        self.__cb1.set('--Select--')

        '''Pack Order'''
        self.__label1.pack()
        self.__entry1.pack(ipadx=100, ipady=5)
        self.__label2.pack()
        self.__entry2.pack(ipadx=100, ipady=5)
        self.__button1.pack()
        self.__label3.pack()
        self.__text1.pack()
        self.__button2.pack()
        self.__label4.pack()
        self.__cb1.pack()
        self.__button3.pack()


    def combo_box_function(self):
        toolkit = glob.glob('toolkit/*')
        files = []
        for i in toolkit:
            files.append(i[8:])
        return files

    def get_ip(self):
        string = str(self.__entry1.get())
        return string

    def get_port(self):
        string = str(self.__entry2.get())
        return string

    '''BUTTON FUNCTIONS'''
    def connect(self):
        host = self.get_ip()
        port = self.get_port()
        connect = NetConnect(host, port)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        connect.client()
        self.display_text()

    def run(self):
        host = self.get_ip()
        port = self.get_port()
        connect = NetConnect(host, port)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message = self.__cb1.get()
        connect.client(message)
        self.display_text()

    def export(self):
        name = f'{datetime.datetime.now()}.txt'
        file = open(name,'w')
        text = open('text.txt')
        file.write(text.read())
        file.close()

    def display_text(self):
        time.sleep(0.5)
        file = open('text.txt')
        file_read = file.read()
        self.__text1.insert(tk.END, file_read)


