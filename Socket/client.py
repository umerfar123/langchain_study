import socket
import threading

SERVER_IP = '192.168.1.3'
PORT = 5050
ADDR = (SERVER_IP,PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = '!Disconnect'


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * len(HEADER - len(send_length))
    
    client.send(send_length)
    client.send(message)