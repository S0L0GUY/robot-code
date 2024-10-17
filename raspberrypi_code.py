import socket
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 5005)) # Port ID

while True:
    data, addr = sock.recvfrom(1024) # Buffer size
    controller_data = json.loads(data.decode('utf-8'))
    print(controller_data)