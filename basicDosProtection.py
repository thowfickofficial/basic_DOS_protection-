import socket
import threading
import time

MAX_CONNECTIONS_PER_IP = 10  # Adjust this value as needed
BAN_TIME = 60  # Ban time in seconds

connection_tracker = {}

def handle_client(client_socket, addr):
    global connection_tracker

    if addr[0] in connection_tracker:
        if connection_tracker[addr[0]] >= MAX_CONNECTIONS_PER_IP:
            print(f"Banning {addr[0]} for {BAN_TIME} seconds.")
            time.sleep(BAN_TIME)
            connection_tracker[addr[0]] = 0
        else:
            connection_tracker[addr[0]] += 1
    else:
        connection_tracker[addr[0]] = 1

    # Your normal handling logic here
    # For example, echoing back received data
    data = client_socket.recv(1024)
    client_socket.send(data)
    client_socket.close()

def main():
    host = "0.0.0.0"
    port = 8080

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"Listening on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")
        
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()

if __name__ == "__main__":
    main()
