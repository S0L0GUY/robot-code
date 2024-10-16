import os
import json
from debug_function_library import Debug as db
import psutil

# I dont remember how im going to send the data...

db.clear()
db.write("SYSTEM", "program starting")

db.write("SYSTEM", "starting controller listener")
os.system('start python controller_listener.py')

def clear_screen():
    """Check the operating system and clear the terminal."""    
    os.system('cls' if os.name == 'nt' else 'clear')

def program_running(file_name):
    for process in psutil.process_iter(['name', 'cmdline']):
        try:
            if process.name().lower() == 'python' or process.name().lower() == 'python.exe':
                cmdline = process.cmdline()
                if len(cmdline) > 1 and file_name in cmdline[1]:
                    return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

while True:
    clear_screen()
    print("Driver Station\n\n")

    while program_running('C:/Users/evagrinn067/Documents/GitHub/robot-code/controller_listener.py'):
        # TODO: Make the robot stop while this is true.
        print("controller listener not running")

    with open('json_files/controller_inputs.json', 'r') as file:
        controller_values = json.load(file)

    # TODO: Wrap and and send data over WI-FI