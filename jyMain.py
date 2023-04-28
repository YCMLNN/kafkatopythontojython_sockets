import socket
import time

# Create a socket object for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Specify the server's IP address and port number
host = '127.0.0.1'
port = 10000  # Replace this with the assigned_port value from the server script

# Keep trying to connect to the server until a connection is established
connected = False
while not connected:
    try:
        client_socket.connect((host, port))
        connected = True
    except socket.error as e:
        # Print an error message and retry the connection after 1 second
        print("Connection failed, retrying in 1 second...")
        time.sleep(1)

# Print a message indicating that the client is connected to the server
print("Connected to {}:{}".format(host, port))

# Continuously receive data from the server and print it to the console
try:
    while True:
        # Receive 1024 bytes of data from the server and decode it as UTF-8
        data = client_socket.recv(1024).decode("utf-8")
        print("Received from server: " + data)
except KeyboardInterrupt:
    # Exit the loop on KeyboardInterrupt (e.g., Ctrl+C)
    pass

# Close the client socket connection
client_socket.close()
