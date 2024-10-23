import os
import json
import time
import psutil
import socket

# Define the Raspberry Pi's IP address and the port you're sending to
RPI_IP = '172.20.10.5'  # Replace with your Raspberry Pi's IP
PORT = 5005  # Port defined in the receiver code

# Define what the controller looks like without any input
NO_DATA = {'axes': {'axis_0': 0.0, 'axis_1': 0.0, 'axis_2': 0.0, 'axis_3': 0.0, 'axis_4': -1.0, 'axis_5': -1.0}, 'buttons': {'button_0': 0, 'button_1': 0, 'button_2': 0, 'button_3': 0, 'button_4': 0, 'button_5': 0, 'button_6': 0, 'button_7': 0, 'button_8': 0, 'button_9': 0, 'button_10': 0, 'button_11': 0, 'button_12': 0, 'button_13': 0, 'button_14': 0, 'button_15': 0}, 'hats': {'hat_0': [...]}}

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Start the controller listener
os.system('start python controller_listener.py')

def clear_screen():
    """Check the operating system and clear the terminal."""    
    os.system('cls' if os.name == 'nt' else 'clear')

def send_data(data):
    """
    Args:
        data (json): the data that will be sent.

    Convert the data to JSON and send it to the server.
    """
    # Connect to the server
    sock.connect((RPI_IP, PORT))

    json_data = json.dumps(data).encode('utf-8')
    sock.sendall(json_data)

while True:
    clear_screen()
    print("Driver Controller\n\n")

    with open('json_files/controller_inputs.json', 'r') as file:
        controller_data = json.load(file)

    send_data(controller_data)

    print("Sent DATA")

    # Add a small delay to reduce CPU usage
    time.sleep(0.1)

    if input() == '':
        break

clear_screen()
print("Program E-STOP Called")

while True:
    send_data(NO_DATA)