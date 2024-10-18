import pygame
import time
import os
import json

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

# Initialize the joystick if any are connected
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
else:
    print("No controller connected")
    exit()  # Exit if no joystick is found

# Main loop to capture all controller values
try:
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Get controller inputs
        controller_data = get_controller_inputs(joystick)
        
        # Write controller inputs to a JSON file
        with open('json_files/controller_inputs.json', 'w') as f:
            json.dump(controller_data, f)
        
        # Print the captured data (optional, for debugging)
        print(controller_data)
        
        time.sleep(0.5)  # Add a small delay to avoid overwhelming the system with too many writes
except KeyboardInterrupt:
    print("Exiting program.")
finally:
    pygame.quit()
