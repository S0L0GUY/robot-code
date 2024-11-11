import socket
import json
from gpiozero import LED # type: ignore

def compute_controller_inputs(controller_data):
    led = LED(27)
    print("data received")
    if controller_data['buttons']['button_1'] == 1:
        led.on()
    else:
        led.off()

def start_server(host='0.0.0.0', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Listening on {host}:{port}")
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024)
                if not data:
                    break
                try:
                    controller_input = json.loads(data.decode('utf-8'))
                    print(f"Received controller input: {controller_input}")
                    compute_controller_inputs(controller_input)
                except json.JSONDecodeError:
                    print("Received invalid JSON")

if __name__ == "__main__":
    start_server()