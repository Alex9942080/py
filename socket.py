import socket, thread, time

def main():
    # my code here
    #server()
    #client()

if __name__ == "__main__":
    main()


def client():
    HOST = ''
    PORT = 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall('Hello, world')
    data = s.recv(1024)
    s.close()
    print 'Received', repr(data)

def server():
    HOST = ''
    PORT = 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print 'Connected by', addr
    while 1:
        data = conn.recv(1024)
        if not data: break
        conn.sendall(data)
    conn.close()
