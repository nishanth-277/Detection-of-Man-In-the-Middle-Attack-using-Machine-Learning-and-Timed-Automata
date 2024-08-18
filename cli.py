import socket
import time

class TimedAutomaton:
    def __init__(self):
        self.current_state = "server"
        self.transition_time_limit = 4
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

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))
    print("Connected to server")

    while True:
        if not automaton.transition():
            print("MITM attack detected!")
            break

        client_socket.send(b"Hello from client")
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received from server: {data.decode()}")

    client_socket.close()

if __name__ == "__main__":
    main()
