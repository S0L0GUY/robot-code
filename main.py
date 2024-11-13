import constants as constant
import commands.drive as drive
import pygame
import json
import os

# Dictionary to store controller inputs
controller_inputs = {
    "axes": {},
    "buttons": {},
    "hats": {}
}

# Initialize pygame
pygame.init()

# Check if a controller is connected
if pygame.joystick.get_count() == 0:
    print("No controller connected!")
    exit()

# Initialize the first joystick (controller)
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Create directory if it doesn't exist
os.makedirs('json_files', exist_ok=True)

def save_inputs_to_json(file_path='json_files/controller_inputs.json'):
    """
    Save controller inputs to a JSON file.
    Args:
        file_path (str): The path to the JSON file where the controller inputs will be saved. 
                         Defaults to 'json_files/controller_inputs.json'.
    Returns:
        None
    """
    with open(file_path, 'w') as f:
        json.dump(controller_inputs, f, indent=4)

def capture_controller_inputs():
    """
    Captures the current state of the controller inputs and returns them as a dictionary.
    
    The function captures the following inputs from the controller:
        - Axis movements
        - Button presses
        - Hat (D-pad) movements
    The captured inputs are stored in a dictionary with the following structure:
        {
            'axes': {
                'axis_0': value,
                'axis_1': value,
                ...
            },
            'buttons': {
                'button_0': value,
                'button_1': value,
                ...
            },
            'hats': {
                'hat_0': value,
                'hat_1': value,
                ...
            }
        }
    Returns:
        dict: A dictionary containing the current state of the controller inputs.
    """
    
    inputs = {
        "axes": {},
        "buttons": {},
        "hats": {}
    }
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # Capture axis movement
        for i in range(joystick.get_numaxes()):
            axis_value = joystick.get_axis(i)
            inputs['axes'][f'axis_{i}'] = axis_value
            
        # Capture button presses
        for i in range(joystick.get_numbuttons()):
            button_value = joystick.get_button(i)
            inputs['buttons'][f'button_{i}'] = button_value
            
        # Capture hat (D-pad) movement
        for i in range(joystick.get_numhats()):
            hat_value = joystick.get_hat(i)
            inputs['hats'][f'hat_{i}'] = hat_value

    return inputs

# Check if a controller is connected
if pygame.joystick.get_count() == 0:
    print("No controller connected!")
    while pygame.joystick.get_count() == 0:
        pass

print(f"Connected to: {joystick.get_name()}")

while True:
    controller_inputs = capture_controller_inputs()
    drive(controller_inputs['axes']['axis_1'], controller_inputs['axes']['axis_2'])