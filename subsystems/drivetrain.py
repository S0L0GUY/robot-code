import constants as constant
from gpiozero import PWMOutputDevice, DigitalOutputDevice # type: ignore

class Drivetrain:
    """
    A class used to represent the Drivetrain subsystem of a robot.
    Attributes
    ----------
    left_motor : PWMOutputDevice
        The motor controller for the left motor.
    right_motor : PWMOutputDevice
        The motor controller for the right motor.
    Methods
    -------
    __init__()
        Initializes the Drivetrain with motor controllers for the left and right motors.
    """
    def __init__(self):
        self.left_motor = PWMOutputDevice(constant.LEFT_MOTOR_PIN)
        self.right_motor = PWMOutputDevice(constant.RIGHT_MOTOR_PIN)

        self.in_1 = DigitalOutputDevice(constant.IN_1_PIN)
        self.in_2 = DigitalOutputDevice(constant.IN_2_PIN)
        self.in_3 = DigitalOutputDevice(constant.IN_3_PIN)
        self.in_4 = DigitalOutputDevice(constant.IN_4_PIN)

    def set_drive_speed(self, left_speed, right_speed):
        """
        Sets the speed of the left and right motors of the drivetrain.
        Parameters:
        left_speed (float): The speed to set for the left motor. Positive values move the motor forward, negative values move it backward, and zero stops the motor.
        right_speed (float): The speed to set for the right motor. Positive values move the motor forward, negative values move it backward, and zero stops the motor.
        The method also controls the state of the motor direction pins (in_1, in_2 for the left motor and in_3, in_4 for the right motor) based on the speed values.
        """
    
        # Set the speed of the left motor
        if left_speed > 0:
            self.left_motor.set(left_speed)
            self.in_1.on()
            self.in_2.off()
        elif left_speed < 0:
            self.left_motor.set(-left_speed)
            self.in_1.off()
            self.in_2.on()
        elif left_speed == 0:
            self.left_motor.set(left_speed)
            self.in_1.off()
            self.in_2.off()

        # Set the speed of the right motor
        if right_speed > 0:
            self.right_motor.set(right_speed)
            self.in_3.on()
            self.in_4.off()
        elif right_speed < 0:
            self.right_motor.set(-right_speed)
            self.in_3.off()
            self.in_4.on()
        elif right_speed == 0:
            self.right_motor.set(right_speed)
            self.in_3.off()
            self.in_4.off()