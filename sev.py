import socket
import time
import pickle

class TimedAutomaton:
    def __init__(self):
        self.current_state = "client"
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

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)
    print("Server is listening...")

    # IRTT calculation
    start_time_irtt = time.time()
    client_socket, client_address = server_socket.accept()
    end_time_irtt = time.time()
    IRTT = end_time_irtt - start_time_irtt-0.76637
    print("IRTT:", IRTT)

    # TTOC calculation
    start_time_ttoc = time.time()
    client_socket.recv(1024)
    end_time_ttoc = time.time()
    TTOC = end_time_ttoc - start_time_ttoc+0.24373

    print("TTOC:", TTOC)

    # Calculate MITR and MATR based on your application logic
    MITR = 0.010792
    MATR = 0.048848

    while True:
        if not automaton.transition():
            # Run machine learning model to detect MITM attack
            # Pass the calculated parameters to the ML model
            with open('random_forest_model2.pkl', 'rb') as file:
                ml_model = pickle.load(file)
            prediction = ml_model.predict([[IRTT, TTOC, MITR, MATR]])
            if prediction[0] == 1:
                print("Man in the Middle attack detected by ML model!")
            else:
                print("Continuing connection...")
            break

        client_socket.send(b"Hello from server")
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received from client: {data.decode()}")

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
