# sudo apt-get install python3-gpiozero
# go to https://gpiozero.readthedocs.io/en/latest/api_output.html for documentation

from gpiozero import LED
from time import sleep

led = LED(27) # Pin number

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)