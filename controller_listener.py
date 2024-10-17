import pygame
import time
import os
import json

current_controller_name = ""

# Initialize Pygame and Joystick
pygame.init()
pygame.joystick.init()

if os.name == 'nt':
    os_type = "win"

def clear_screen():
    """Check the operating system and clear the terminal."""    
    if os_type == "win":
        os.system('cls')
    else:
        os.system('clear')

def get_controller_inputs(joystick):
    """Get all inputs from the controller."""
    inputs = {}
    
    # Get axis values
    for i in range(joystick.get_numaxes()):
        inputs[f"axis_{i}"] = round(joystick.get_axis(i), 2)
    
    # Get button values
    for i in range(joystick.get_numbuttons()):
        inputs[f"button_{i}"] = joystick.get_button(i)
    
    # Get hat values
    for i in range(joystick.get_numhats()):
        inputs[f"hat_{i}"] = joystick.get_hat(i)
    
    return inputs

# Main loop to capture all controller values
while True:
    # Check if a joystick is connected
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()

        if current_controller_name != joystick.get_name():
            clear_screen()
            print(f"Connected to controller: {joystick.get_name()}")

        current_controller_name = joystick.get_name()

        pygame.event.pump()
            
        # Get all controller inputs
        inputs = get_controller_inputs(joystick)
            
        # Store inputs in JSON file
        with open('json_files/controller_inputs.json', 'w') as f:
            json.dump(inputs, f)

    else:
        clear_screen()
        print("no controller detected")

# Quit Pygame
pygame.quit()