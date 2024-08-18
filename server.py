import socket
import time

class TimedAutomaton:
    def __init__(self):
        self.current_state = "client"
        self.transition_time_limit = 2.7
        self.last_transition_time = time.time()

    def transition(self):
        current_time = time.time()
        time_elapsed = current_time - self.last_transition_time

        if time_elapsed > self.transition_time_limit:
            print("Man in the Middle attack!")
            return False

        if self.current_state == "client":
            self.current_state = "server"
            print("Transitioned from client to server.")
        elif self.current_state == "server":
            self.current_state = "client"
            print("Transitioned from server to client.")

        self.last_transition_time = current_time
        return True

def main():
    automaton = TimedAutomaton()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)
    print("Server is listening...")

    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    
    while True:
        if not automaton.transition():
            break  # MITM attack detected

        client_socket.send(b"Hello from server")
        data = client_socket.recv(1024)
        if not data:
            break  
        print(f"Received from client: {data.decode()}")

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
