import os
import json
import time
from debug_function_library import Debug as db
import psutil
import socket

# Define the Raspberry Pi's IP address and the port you're sending to
RPI_IP = '172.20.10.5'  # Replace with your Raspberry Pi's IP
PORT = 12345  # Port defined in the receiver code

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

old_controller_data = ""

db.clear()
db.write("SYSTEM", "program starting")

db.write("SYSTEM", "starting controller listener")
os.system('start python controller_listener.py')

def clear_screen():
    """Check the operating system and clear the terminal."""    
    os.system('cls' if os.name == 'nt' else 'clear')

def send_json(file_path):
    # Open and read the JSON file
    with open(file_path, 'r') as file:
        json_data = json.load(file)
    
    # Convert JSON to a string
    json_str = json.dumps(json_data)
    
    # Create a socket connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((RPI_IP, PORT))

    try:
        # Send the JSON data
        sock.sendall(json_str.encode('utf-8'))
        print(f"JSON file {file_path} sent successfully.")
    except Exception as e:
        print(f"Failed to send JSON file: {e}")
    finally:
        # Close the socket
        sock.close()

while True:
    clear_screen()
    print("Driver Controller\n\n")

    send_json('json_files/controller_inputs.json')

    print("Sent DATA")

    # Add a small delay to reduce CPU usage
    time.sleep(0.1)

    if input() == '':
        break

no_data = {
    "axes": {
        "axis_0": 0.0,
        "axis_1": 0.0,
        "axis_2": 0.0,
        "axis_3": 0.0,
        "axis_4": -1.0,
        "axis_5": -1.0
    },
    "buttons": {
        "button_0": 0,
        "button_1": 0,
        "button_2": 0,
        "button_3": 0,
        "button_4": 0,
        "button_5": 0,
        "button_6": 0,
        "button_7": 0,
        "button_8": 0,
        "button_9": 0,
        "button_10": 0,
        "button_11": 0,
        "button_12": 0,
        "button_13": 0,
        "button_14": 0,
        "button_15": 0
    },
    "hats": {
        "hat_0": [
            0,
            0
        ]
    }
}
no_data = json.dumps(no_data).encode('utf-8')

clear_screen()
print("Program E-STOP Called")

while True:
    sock.sendto(no_data, (RPI_IP, PORT))