import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 10000  # Replace this with the assigned_port value from the server script

connected = False
while not connected:
    try:
        client_socket.connect((host, port))
        connected = True
    except socket.error as e:
        print("Connection failed, retrying in 1 second...")
        time.sleep(1)

print("Connected to {}:{}".format(host, port))

try:
    while True:
        data = client_socket.recv(1024).decode("utf-8")
        print("Received from server: " + data)
except KeyboardInterrupt:
    pass  # Exit the loop on KeyboardInterrupt (e.g., Ctrl+C)

client_socket.close()
