import constants as constant
import gpiozero # type: ignore

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

def set_drive_speed(self, left_speed, right_speed):
    """
    Sets the speed of the left and right motors of the drivetrain.
    Parameters:
    left_speed (float): The speed to set for the left motor.
    right_speed (float): The speed to set for the right motor.
    Returns:
    None
    """
    self.left_motor.set(left_speed)
    self.right_motor.set(right_speed)