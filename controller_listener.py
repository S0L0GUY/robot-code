import pygame
import json
import os

class ControllerListener:
    def __init__(self, file_path='json_files/controller_inputs.json'):
        # Initialize pygame
        pygame.init()

        # Create directory if it doesn't exist
        if not os.path.exists('json_files'):
            os.makedirs('json_files')

        # File path to store inputs
        self.file_path = file_path

        # Dictionary to store controller inputs
        self.controller_inputs = {
            "axes": {},
            "buttons": {},
            "hats": {}
        }

    def save_inputs_to_json(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.controller_inputs, f, indent=4)

    def capture_controller_inputs(self):
        '''
        Main program to capture controller inputs
        '''
        # Check if a controller is connected
        if pygame.joystick.get_count() == 0:
            print("No controller connected!")
            return

        # Initialize the first joystick (controller)
        joystick = pygame.joystick.Joystick(0)
        joystick.init()

        print(f"Connected to: {joystick.get_name()}")

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                # Capture axis movement
                for i in range(joystick.get_numaxes()):
                    axis_value = joystick.get_axis(i)
                    self.controller_inputs['axes'][f'axis_{i}'] = axis_value
                
                # Capture button presses
                for i in range(joystick.get_numbuttons()):
                    button_value = joystick.get_button(i)
                    self.controller_inputs['buttons'][f'button_{i}'] = button_value
                
                # Capture hat (D-pad) movement
                for i in range(joystick.get_numhats()):
                    hat_value = joystick.get_hat(i)
                    self.controller_inputs['hats'][f'hat_{i}'] = hat_value

                # Save the inputs to the JSON file
                self.save_inputs_to_json()

            pygame.time.wait(100)

        # Quit pygame when done
        pygame.quit()