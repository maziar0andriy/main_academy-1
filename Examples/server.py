import socket, select

def broadcast_data (sock, message):
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock:
            try :
                socket.send(message)
            except :
                socket.close()
                CONNECTION_LIST.remove(socket)
     
CONNECTION_LIST = list()
RECV_BUFFER = 4096
ADDR = ("0.0.0.0", 9000)
 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(ADDR)
server_socket.listen(10)

CONNECTION_LIST.append(server_socket)

print("Started!")
while True:
    read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST,[],[])

    for sock in read_sockets:
        if sock == server_socket:
            sockfd, addr = server_socket.accept()
            CONNECTION_LIST.append(sockfd)
            print("Client ({}) connected".format(addr))
            broadcast_data(sockfd, "[%s:%s] entered room\n" % addr)

        else:
            data = sock.recv(RECV_BUFFER)
            print("<Client> {}".format(data))
            if data:
                broadcast_data(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data)              
 
server_socket.close()