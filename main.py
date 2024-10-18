import os
import json
from debug_function_library import Debug as db
import psutil
import socket

# Define the Raspberry Pi's IP address and the port you're sending to
raspberry_pi_ip = '172.20.10.5'  # Replace with your Raspberry Pi's IP
port = 5005  # Port defined in the receiver code

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

controller_data = ""

db.clear()
db.write("SYSTEM", "program starting")

db.write("SYSTEM", "starting controller listener")
os.system('start python controller_listener.py')

def clear_screen():
    """Check the operating system and clear the terminal."""    
    os.system('cls' if os.name == 'nt' else 'clear')

def program_running(file_name):
    """Check if a program with the given file name is running."""
    for process in psutil.process_iter(['name']):
        try:
            if process.name().lower() == file_name.lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

while True:
    clear_screen()
    print("Driver Controller\n\n")

    while program_running('controller_listener.py'):
        # TODO: Make the robot stop while this is true.
        print("controller listener not running")

    old_controller_data = controller_data

    with open('json_files/controller_inputs.json', 'r') as file:
        controller_data = json.load(file)

    if old_controller_data != controller_data:
        sock.sendto(json.dumps(controller_data).encode('utf-8'), (raspberry_pi_ip, port))

    if input() == '':
        break

no_data = {"axis_0": 0.0, "axis_1": 0.0, "axis_2": 0.0, "axis_3": 0.0, "axis_4": -1.0, "axis_5": -1.0, "button_0": 0, "button_1": 0, "button_2": 0, "button_3": 0, "button_4": 0, "button_5": 0, "button_6": 0, "button_7": 0, "button_8": 0, "button_9": 0, "button_10": 0, "button_11": 0, "button_12": 0, "button_13": 0, "button_14": 0, "button_15": 0, "hat_0": [0, 0]}
no_data = json.dumps(no_data).encode('utf-8')

clear_screen()
print("Program E-STOP Called")

while True:
    sock.sendto(no_data, (raspberry_pi_ip, port))