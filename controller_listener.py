import pygame
import time
import os
import json

if os.name == 'nt':
    os_type = "win"

# Initialize Pygame and Joystick
pygame.init()
pygame.joystick.init()

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
    clear_screen()
    
    # Check if a joystick is connected
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        print(f"Controller connected: {joystick.get_name()}")
        print(f"Number of axes: {joystick.get_numaxes()}")
        print(f"Number of buttons: {joystick.get_numbuttons()}")
        print(f"Number of hats: {joystick.get_numhats()}")

        while True:
            pygame.event.pump()
            
            # Get all controller inputs
            inputs = get_controller_inputs(joystick)
            
            # Store inputs in JSON file
            with open('controller_inputs.json', 'w') as f:
                json.dump(inputs, f, indent=4)
            
            # Print current inputs
            clear_screen()
            print(json.dumps(inputs, indent=4))
            
            time.sleep(0.1)  # Adjust the delay as needed
    else:
        print("no controller detected")

# Quit Pygame
pygame.quit()