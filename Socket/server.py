import socket
import threading

SERVER_IP = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER_IP,PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = '!Disconnect'

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f'[SERVER] --- New Connection : {addr}')
    while True:
        msg_length = conn.recv(HEADER).decode(FORMAT)           # Blocking Code
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length)
            print(f'[SERVER] --- Msg From Client[{addr}] : {msg}')
            
            if msg == DISCONNECT_MSG:
                break
    print(f'[SERVER] --- Closing Connection To Client : {addr}')
    conn.close()
            
            
def start_server():
    print(f'[SERVER] --- Listening On : {SERVER_IP}')
    server.listen()
    while True:
        conn, addr = server.accept() # Blocking Code
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f'[SERVER] --- Active Connections : {threading.active_count() - 1} ')
        

if __name__ == '__main__':
    start_server()
    