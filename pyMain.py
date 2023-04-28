import socket
import json
from kafka import KafkaConsumer

# Kafka configuration
kafka_topic = "low-frequency"
kafka_bootstrap_servers = "172.29.10.2:9092"

# Create a Kafka consumer
consumer = KafkaConsumer(
    kafka_topic,
    bootstrap_servers=[kafka_bootstrap_servers],
    value_deserializer=lambda x: x,
    auto_offset_reset='earliest'
)

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
start_port = 10000
end_port = 11000

# Find an available port in the specified range
assigned_port = None
for port in range(start_port, end_port + 1):
    try:
        server_socket.bind((host, port))
        assigned_port = port
        break
    except socket.error:
        continue

# If an available port is found, start listening for connections
if assigned_port is not None:
    server_socket.listen(1)
    print("Server listening on {}:{}".format(host, assigned_port))

    conn, addr = server_socket.accept()
    print("Connection from: {}".format(addr))

    # Process messages from the Kafka consumer and send them to the client
    try:
        for message in consumer:
            payload = {
                "topic": message.topic,
                "partition": message.partition,
                "offset": message.offset,
                "timestamp": message.timestamp,
                "key": message.key.decode('utf-8'),
                "value": message.value.decode('ascii', errors='ignore')
            }
            json_payload = json.dumps(payload, indent=4)
            conn.send(json_payload.encode('utf-8'))
    except KeyboardInterrupt:
        # Exit the loop on KeyboardInterrupt (e.g., Ctrl+C)
        pass

    # Close the connection
    conn.close()

else:
    print("No available port found in the specified range.")
