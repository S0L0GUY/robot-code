# sudo apt-get install python3-gpiozero
# go to https://gpiozero.readthedocs.io/en/latest/api_output.html for documentation

from gpiozero import LED
import socket
import json

button_name = "" # Replace with button #
led = LED(27) # Pin number

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 5005)) # Port ID

while True:
    data, addr = sock.recvfrom(1024) # Buffer size
    controller_data = json.loads(data.decode('utf-8'))
    
    if controller_data[button_name] == 1:
        led.on()
    else:
        led.off()