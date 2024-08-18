import socket
import threading

class MITMAttacker:
    def __init__(self, target_host, target_port, listen_port):
        self.target_host = target_host
        self.target_port = target_port
        self.listen_port = listen_port

    def handle_client(self, client_socket):
        # Connect to target server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.connect((self.target_host, self.target_port))

            while True:
                # Receive data from the client
                client_data = client_socket.recv(4096)
                if not client_data:
                    break

                # Forward data from client to server
                server_socket.send(client_data)

                # Receive data from the server
                server_response = server_socket.recv(4096)
                if not server_response:
                    break

                # Forward data from server to client
                client_socket.send(server_response)

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0', self.listen_port))
        server.listen(5)
        print(f"[*] Listening on {self.listen_port}")

        while True:
            client_socket, client_address = server.accept()
            print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

if __name__ == "__main__":
    mitm = MITMAttacker(target_host='127.0.0.1', target_port=12345, listen_port=9999)
    mitm.start()
