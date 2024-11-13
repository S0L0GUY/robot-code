import subsystems.drivetrain as drivetrain
import constants as constant
import gpiozero # type: ignore

def drive(forward_velocity, rotation_velocity):
    """
    Controls the drivetrain by setting the speed of the left and right motors.
    Args:
        forward_velocity (float): The forward velocity component.
        rotation_velocity (float): The rotational velocity component.
    The function calculates the speed for the left and right motors by combining
    the forward and rotational velocities. The speeds are rounded to two decimal
    places before being set on the drivetrain.
    """
    
    left_speed = round(forward_velocity + rotation_velocity, 2)
    right_speed = round(forward_velocity - rotation_velocity, 2)
    
    drivetrain.Drivetrain.set_drive_speed(left_speed, right_speed)