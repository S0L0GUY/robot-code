#!/usr/bin/env python3
"""
Simple robot motor control script for Raspberry Pi with L298 motor driver.
This script runs the motors continuously forward without any controller input.
"""

import time
from subsystems.drivetrain import Drivetrain

def main():
    """
    Main function to run the motors continuously.
    The motors will run forward at full speed until the script is stopped (Ctrl+C).
    """
    print("Initializing drivetrain...")
    drivetrain = Drivetrain()
    
    print("Starting motors at full speed forward...")
    print("Press Ctrl+C to stop the motors")
    
    try:
        # Set both motors to run forward at full speed (1.0 = 100%)
        # Adjust the speed value (0.0 to 1.0) to control motor speed
        # 1.0 = full speed forward
        # 0.5 = half speed forward
        drivetrain.set_drive_speed(1.0, 1.0)
        
        # Keep the program running
        while True:
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\nStopping motors...")
        drivetrain.set_drive_speed(0, 0)
        print("Motors stopped. Exiting.")

if __name__ == "__main__":
    main()
