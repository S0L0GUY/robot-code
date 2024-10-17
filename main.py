import os
import json
from debug_function_library import Debug as db
import psutil
import socket

# Define the Raspberry Pi's IP address and the port you're sending to
raspberry_pi_ip = '192.168.0.100'  # Replace with your Raspberry Pi's IP
port = 5005  # Port defined in the receiver code

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

controller_data = ""

# I dont remember how im going to send the data...

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
    print("Driver Station\n\n")

    while program_running('controller_listener.py'):
        # TODO: Make the robot stop while this is true.
        print("controller listener not running")

    old_controller_data = controller_data

    with open('json_files/controller_inputs.json', 'r') as file:
        controller_data = json.load(file)

    if old_controller_data != controller_data:
        sock.sendto(controller_data.encode('utf-8'), (raspberry_pi_ip, port))
