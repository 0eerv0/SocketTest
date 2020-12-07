import socket
import threading

HEADER = 64 #message is 64 bytes
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr): #handles connection between client and the server
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) 
        if msg_length :   
            msg_length = int (msg_length)
            msg = conn.recv(msg_length).decode(FORMAT) #decodes messages from bytes to string
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))
    conn.close()

def start(): #handle new connections
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()  #will wait for a new connection and will store the address (ip and port) then it will store an object to allow us to send information
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.activeCount() - 1}") #tells how many threadsare active which means how many connections are active. We put -1 because one thread is always active so to get the actual connections we take one off.

print("[STARTING] Server is starting...")
start()



