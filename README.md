# kafkatopythontojython_sockets

This repository contains two files, `pyMain.py` and `jyMain.py`, which demonstrate a simple bridge between a Python environment and a Jython environment using Kafka messages and the standard socket library.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The goal of this project is to showcase how to transmit messages between a Python and Jython environment using Kafka and the standard socket library. The Python script `pyMain.py` consumes messages from a Kafka topic, serializes them as JSON, and sends them to the Jython script `jyMain.py` over a socket connection. The Jython script receives the messages and prints them to the console.

## Requirements

To run this project, you will need:

- Python 3.x
- Jython 2.7.x
- Kafka (with a running Kafka broker)
- The following Python libraries:
  - kafka-python (`pip install kafka-python`)

## Usage

1. Clone this repository:
```
git clone https://github.com/YCMLNN/kafkatopythontojython_sockets.git
cd kafkatopythontojython_sockets
```


2. Start the Kafka broker and create a topic for message transmission. Note the topic name and the Kafka broker's address.

3. Replace the `kafka_topic` and `kafka_bootstrap_servers` variables in `pyMain.py` with your Kafka topic name and broker's address.

4. Run the code of pyMain.py file in a Python environment.

6. Run the code of jyMain.py in a Jython environment (or in the case of a utilization with Ignition, in the scripting environment of Ignition). If the connection to the Python script fails, update the `port` variable in `jyMain.py` with the `assigned_port` value printed by the Python script.

7. Send messages to the Kafka topic using a Kafka producer. The Python script will consume the messages, serialize them as JSON, and send them to the Jython script over a socket connection. The Jython script will print the received messages to the console.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more information.
