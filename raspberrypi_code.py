import socket
import json
from gpiozero import LED # type: ignore

led = LED(27)

# Define the port the server will listen on
PORT = 5005
BUFFER_SIZE = 1024

def receive_json():
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the port
    sock.bind(('', PORT))
    sock.listen(1)  # Allow one client to connect

    print(f"Waiting for a connection on port {PORT}...")
    
    conn, addr = sock.accept()
    print(f"Connection from {addr} established.")

    # Receive the JSON data
    json_data = b""
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        json_data += data

    # Decode and load the received JSON
    json_str = json_data.decode('utf-8')
    controller_data = json.loads(json_str)

    print(f"Received JSON data: {controller_data}")

    if controller_data["buttons"]["button_2"] == 1:
        led.on()
    else:
        led.off()

    # Close the connection
    conn.close()
    sock.close()
    
while True:
    receive_json()