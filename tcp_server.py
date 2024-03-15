import socket
import http_server

http_server = http_server.HTTPServer()

class TCP:
    def __init__(self, SERVER_HOST, SERVER_PORT) -> None:
        self.SERVER_HOST = SERVER_HOST
        self.SERVER_PORT = SERVER_PORT
    def start(self):

        srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        srv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv_sock.bind((self.SERVER_HOST, self.SERVER_PORT))
        srv_sock.listen(5)
        print(f'Server now listening on port: {self.SERVER_PORT}')
        print(f'Listening at {srv_sock.getsockname()}')

        while True:
            client_connection, client_address = srv_sock.accept()
            print(f'Connected from {client_address}')
            
            data = client_connection.recv(1024)
            response = http_server.handle_request(data)

            client_connection.sendall(response)
            client_connection.close()


if __name__ == '__main__':
    srv = TCP('0.0.0.0', 6969)
    srv.start()