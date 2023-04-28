import socket
import time
import random

from kafka import KafkaConsumer
import json


# Kafka configuration
kafka_topic = "low-frequency"
kafka_bootstrap_servers = "172.29.10.2:9092"

# Kafka consumer
consumer = KafkaConsumer(
	kafka_topic,
	bootstrap_servers=[kafka_bootstrap_servers],
	value_deserializer=lambda x: x,
	auto_offset_reset='earliest'
)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
start_port = 10000
end_port = 11000

assigned_port = None
for port in range(start_port, end_port + 1):
	try:
		server_socket.bind((host, port))
		assigned_port = port
		break
	except socket.error:
		continue

if assigned_port is not None:
	server_socket.listen(1)
	print("Server listening on {}:{}".format(host, assigned_port))

	conn, addr = server_socket.accept()
	print("Connection from: {}".format(addr))

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
			# conn.send(str(record).encode("utf-8"))
	except KeyboardInterrupt:
		pass

	conn.close()

else:
	print("No available port found in the specified range.")

""" 	try:
		for message in consumer:
			if random.randint(1, 6) == 6:
				conn.send(message.value)  # Send the message from the Kafka topic to the socket
			time.sleep(1)  # Send a message every second
	except KeyboardInterrupt:
		pass  # Exit the loop on KeyboardInterrupt (e.g., Ctrl+C) """

	
	# try:
	#     for message in consumer:
	#         if random.randint(1, 6) == 6:
	#             conn.send(message.value)  # Send the message from the Kafka topic to the socket
	#         time.sleep(1)  # Send a message every second
	# except KeyboardInterrupt:
	#     pass  # Exit the loop on KeyboardInterrupt (e.g., Ctrl+C)

