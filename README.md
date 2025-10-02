# Robot Motor Control for Raspberry Pi

A simple and robust Python-based robot motor control system designed to run on a Raspberry Pi with a DROK L298 Dual H-Bridge Motor Driver. This code makes your robot's motors run continuously without any controller input.

## Table of Contents
- [Hardware Requirements](#hardware-requirements)
- [Pin Connections and Wiring](#pin-connections-and-wiring)
- [Raspberry Pi Setup](#raspberry-pi-setup)
- [Software Installation](#software-installation)
- [Running the Code](#running-the-code)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Safety Notes](#safety-notes)

---

## Hardware Requirements

### Essential Components
- **Raspberry Pi** (Model 3B, 3B+, 4, or Zero W recommended)
- **DROK DC Motor Driver** - L298 Dual H Bridge Motor Speed Controller
  - Specs: DC 6.5V-27V, 7A PWM Motor Regulator, 160W with Optocoupler Isolation
  - [Amazon Link](https://a.co/d/6dGAlb0)
- **Two DC Motors** (12V recommended, compatible with your motor driver voltage range)
- **Power Supply/Battery**
  - 12V battery recommended (7Ah or higher for longer runtime)
  - Options:
    - [ExpertPower 12v 7ah Rechargeable Sealed Lead Acid Battery](https://a.co/d/d4gsVd8)
    - [Tenergy NiMH Battery Pack 12V 2000mAh](https://a.co/d/dOvbrWA)
- **Jumper Wires** (Female-to-Female recommended)
  - [80 Piece Female to Female Jumper Wires](https://a.co/d/cXCbcr1)

### Optional Components
- **Robot Chassis**
  - [Robot Tank Chassis Metal](https://a.co/d/c2apBfQ) - Best Pick
- **Micro SD Card** (16GB or larger, Class 10)
- **Power bank or separate 5V supply** for Raspberry Pi

**Estimated Total Cost: ~$56-80** (depending on components chosen)

---

## Pin Connections and Wiring

### L298 Motor Driver Connection Overview

The L298 motor driver controls two motors (left and right) with PWM speed control and direction control.

#### Raspberry Pi GPIO to L298 Motor Driver

| Raspberry Pi GPIO | L298 Motor Driver Pin | Function |
|-------------------|-----------------------|----------|
| GPIO 12 (PWM0)    | ENA                   | Left motor PWM speed control |
| GPIO 13 (PWM1)    | ENB                   | Right motor PWM speed control |
| GPIO 4            | IN1                   | Left motor direction control 1 |
| GPIO 25           | IN2                   | Left motor direction control 2 |
| GPIO 24           | IN3                   | Right motor direction control 1 |
| GPIO 23           | IN4                   | Right motor direction control 2 |
| GND               | GND                   | Common ground |

#### L298 Motor Driver to Motors and Power

| L298 Pin | Connection |
|----------|------------|
| OUT1     | Left Motor (+) |
| OUT2     | Left Motor (-) |
| OUT3     | Right Motor (+) |
| OUT4     | Right Motor (-) |
| +12V     | Battery Positive (12V) |
| GND      | Battery Negative (Ground) |
| +5V      | **DO NOT CONNECT** (optional 5V output from regulator) |

### Detailed Wiring Steps

1. **Connect Power to L298 Driver:**
   - Connect battery **positive (+)** to L298 **+12V** terminal
   - Connect battery **negative (-)** to L298 **GND** terminal

2. **Connect Motors to L298 Driver:**
   - Left motor wires to **OUT1** and **OUT2**
   - Right motor wires to **OUT3** and **OUT4**
   - Note: If a motor spins backward, swap its two wires

3. **Connect Raspberry Pi to L298 Driver:**
   - Use jumper wires to connect the GPIO pins as listed in the table above
   - **Important:** Connect Raspberry Pi **GND** to L298 **GND** for common ground
   - **DO NOT** connect Raspberry Pi 5V to motor power (keep them separate)

4. **Power the Raspberry Pi:**
   - Use a separate 5V power supply (USB power adapter) for the Raspberry Pi
   - Or use a DC-DC converter to step down 12V to 5V for the Pi (if you know what you're doing)

### Wiring Diagram
For a visual wiring diagram, see: [Wiring Diagram](https://www.tldraw.com/s/v2_c_sRXHDCU-p6VVEBGza9NZv?d=v-887.-64.1920.953.eGgpUsz7OhJ7m6jL8Jj8d)

For L298 motor driver details, see: [Motor Controller User Manual](https://www.handsontec.com/dataspecs/module/7A-160W%20motor%20control.pdf)

---

## Raspberry Pi Setup

### 1. Install Raspberry Pi OS

1. Download **Raspberry Pi OS Lite** (or Desktop if you want GUI) from [raspberrypi.com](https://www.raspberrypi.com/software/)
2. Use **Raspberry Pi Imager** to flash the OS to your SD card
3. Before ejecting, configure WiFi and SSH:
   - In Raspberry Pi Imager, click the gear icon for advanced options
   - Enable SSH
   - Set username and password
   - Configure WiFi (if needed)

### 2. Boot and Access Raspberry Pi

1. Insert SD card into Raspberry Pi
2. Connect power
3. SSH into your Pi:
   ```bash
   ssh pi@raspberrypi.local
   # Or use the IP address: ssh pi@192.168.1.xxx
   ```

### 3. Update System

```bash
sudo apt update
sudo apt upgrade -y
```

### 4. Enable GPIO and Interfaces

GPIO is typically enabled by default, but verify:
```bash
sudo raspi-config
```
- Navigate to **Interface Options** → **Enable** any needed interfaces
- Reboot: `sudo reboot`

---

## Software Installation

### 1. Install Python and Required Libraries

```bash
# Install Python 3 and pip (usually pre-installed)
sudo apt install python3 python3-pip git -y

# Install gpiozero library for GPIO control
sudo apt install python3-gpiozero -y
```

### 2. Clone or Download the Code

If you have this code in a Git repository:
```bash
cd ~
git clone https://github.com/S0L0GUY/robot-code.git
cd robot-code
```

Or create the files manually by copying the code from this repository.

### 3. Verify File Structure

Your directory should look like this:
```
robot-code/
├── main.py
├── constants.py
├── subsystems/
│   └── drivetrain.py
└── README.md
```

---

## Running the Code

### 1. Navigate to Code Directory

```bash
cd ~/robot-code
```

### 2. Run the Motor Control Script

```bash
python3 main.py
```

### 3. Stop the Motors

To stop the motors, press **Ctrl+C** in the terminal. The script will gracefully stop the motors and exit.

```
Initializing drivetrain...
Starting motors at full speed forward...
Press Ctrl+C to stop the motors
^C
Stopping motors...
Motors stopped. Exiting.
```

### 4. Run on Startup (Optional)

To make the motors start automatically when the Raspberry Pi boots:

1. Create a systemd service:
   ```bash
   sudo nano /etc/systemd/system/robot-motors.service
   ```

2. Add the following content:
   ```ini
   [Unit]
   Description=Robot Motor Control
   After=multi-user.target

   [Service]
   Type=simple
   User=pi
   WorkingDirectory=/home/pi/robot-code
   ExecStart=/usr/bin/python3 /home/pi/robot-code/main.py
   Restart=on-failure

   [Install]
   WantedBy=multi-user.target
   ```

3. Enable and start the service:
   ```bash
   sudo systemctl enable robot-motors.service
   sudo systemctl start robot-motors.service
   ```

4. Check status:
   ```bash
   sudo systemctl status robot-motors.service
   ```

5. To stop the service:
   ```bash
   sudo systemctl stop robot-motors.service
   ```

---

## Customization

### Adjust Motor Speed

Edit `main.py` and change the speed values in the `set_drive_speed()` function:

```python
# Full speed forward (1.0 = 100%)
drivetrain.set_drive_speed(1.0, 1.0)

# Half speed forward (0.5 = 50%)
drivetrain.set_drive_speed(0.5, 0.5)

# Turn right (left motor faster)
drivetrain.set_drive_speed(1.0, 0.5)

# Turn left (right motor faster)
drivetrain.set_drive_speed(0.5, 1.0)

# Spin in place (motors opposite directions)
drivetrain.set_drive_speed(1.0, -1.0)
```

### Change GPIO Pins

If you need to use different GPIO pins, edit `constants.py`:

```python
LEFT_MOTOR_PIN = 12   # PWM pin for left motor speed (ENA)
RIGHT_MOTOR_PIN = 13  # PWM pin for right motor speed (ENB)

IN_1_PIN = 4   # Left motor direction pin 1
IN_2_PIN = 25  # Left motor direction pin 2
IN_3_PIN = 24  # Right motor direction pin 1
IN_4_PIN = 23  # Right motor direction pin 2
```

---

## Troubleshooting

### Motors Don't Move

1. **Check Power:**
   - Verify battery is charged and connected to L298 +12V and GND
   - Check that battery voltage is sufficient (at least 6.5V)

2. **Check Wiring:**
   - Verify all GPIO connections match the pin table
   - Ensure common ground between Raspberry Pi and L298
   - Check jumper wire connections are secure

3. **Check Motor Connections:**
   - Ensure motors are connected to OUT1-OUT4
   - Try swapping motor wires if needed

4. **Test GPIO:**
   ```bash
   # Test if gpiozero is working
   python3 -c "from gpiozero import LED; led = LED(4); led.on()"
   ```

### Motors Spin Wrong Direction

- Swap the two wires for that motor on the L298 driver (e.g., swap OUT1 and OUT2 for left motor)
- Or modify the code to invert the direction logic in `drivetrain.py`

### Permission Denied Errors

If you get GPIO permission errors:
```bash
sudo usermod -a -G gpio pi
# Log out and back in
```

Or run with sudo (not recommended for production):
```bash
sudo python3 main.py
```

### Motors Run at Different Speeds

This is normal due to motor variations. You can compensate in code:
```python
# If left motor is slower, increase its speed slightly
drivetrain.set_drive_speed(1.0, 0.9)
```

### Raspberry Pi Brownout/Crashes

- The Pi and motors should have **separate power supplies**
- Motor startup current can cause voltage drops
- Use a capacitor (1000µF or larger) across motor driver power input
- Ensure battery can supply enough current (7A recommended)

---

## Safety Notes

⚠️ **Important Safety Information:**

1. **Always have an easy way to disconnect power** (emergency stop switch recommended)
2. **Keep fingers and objects away from moving parts** when motors are running
3. **Start with low speeds** when testing (0.3-0.5) before going to full speed
4. **Secure your robot** on blocks or prevent it from falling off surfaces during testing
5. **Never connect motor power directly to Raspberry Pi GPIO pins** - this will destroy your Pi
6. **Use separate power supplies** for Raspberry Pi (5V) and motors (12V)
7. **Double-check wiring** before powering on - reversed polarity can damage components
8. **Ensure adequate ventilation** - motor drivers can get hot during operation
9. **Use appropriate wire gauge** for motor current (18-22 AWG recommended)
10. **Monitor battery voltage** - don't over-discharge batteries

---

## Additional Resources

- **Raspberry Pi GPIO Pinout:** https://pinout.xyz/
- **gpiozero Documentation:** https://gpiozero.readthedocs.io/
- **L298 Motor Driver Datasheet:** https://www.handsontec.com/dataspecs/module/7A-160W%20motor%20control.pdf

## License

MIT License - see LICENSE file

---

## Support and Contributing

For issues, questions, or contributions, please visit the GitHub repository:
https://github.com/S0L0GUY/robot-code

---

**Happy building! 🤖**