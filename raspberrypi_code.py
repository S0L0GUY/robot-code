# sudo apt-get install python3-gpiozero
# go to https://gpiozero.readthedocs.io/en/latest/api_output.html for documentation

import time
import socket
import json

counter = 0
while True:
    data, addr = sock.recvfrom(1100)
    controller_data = json.loads(data.decode('utf-8'))
    counter += 1
    print(f"Received packet #{counter} at {time.time()}: {controller_data}")