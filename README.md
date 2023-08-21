# basic_DOS_protection

This is a simple Python script that limits the number of connections from the same IP address. You can adjust the maximum number of connections per IP and the ban time as needed.

## How it works

- The script creates a server that listens for incoming connections on a specified host and port.
- When a client connects, it checks the number of connections from the client's IP address.
- If the number of connections exceeds the maximum allowed, it bans the IP address for a specified ban time.
- If the IP address is not banned, the script handles the connection as usual (in this example, it echoes back received data).

## Configuration

You can configure the following parameters at the beginning of the script:

- `MAX_CONNECTIONS_PER_IP`: The maximum number of connections allowed from the same IP address before banning.
- `BAN_TIME`: The duration (in seconds) for which an IP address is banned when it exceeds the maximum connections.

## Usage

1. Modify the `MAX_CONNECTIONS_PER_IP` and `BAN_TIME` values according to your requirements.
2. Run the script, and it will listen on the specified host and port.
3. When a client connects, the script will keep track of the number of connections from the same IP address and apply the ban if necessary.

Make sure to implement your desired handling logic in the `handle_client` function according to your specific use case.

Please note that this script is a basic example and may need additional features and error handling for production use.
