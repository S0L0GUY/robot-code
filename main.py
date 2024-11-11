import json
import socket
import time
from controller_listener import ControllerListener

class ControllerSender:
    def __init__(self, host, port, file_path='json_files/controller_inputs.json'):
        self.host = host
        self.port = port
        self.file_path = file_path

    def send_controller_inputs(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            while True:
                try:
                    s.connect((self.host, self.port))
                    print(f"Connected to Raspberry Pi at {self.host}:{self.port}")
                    break
                except socket.error as e:
                    print(f"Connection error: {e}. Retrying...")

            while True:
                try:
                    with open(self.file_path, 'r') as f:
                        controller_inputs = json.load(f)
                    
                    s.sendall(json.dumps(controller_inputs).encode('utf-8'))
                    print(f"Sent: {controller_inputs}")

                    time.sleep(0.1)
                except KeyboardInterrupt:
                    print("Stopping the sender.")
                    break
                except Exception as e:
                    print(f"An error occurred: {e}")
                    break

if __name__ == "__main__":
    listener = ControllerListener()
    sender = ControllerSender(host='raspberrypi.local', port=65432)

    # listener.capture_controller_inputs()
    sender.send_controller_inputs()