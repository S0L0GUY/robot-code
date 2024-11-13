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
    the forward and rotational velocities. It then sets the drivetrain's motor
    speeds accordingly.
    """
    left_speed = forward_velocity + rotation_velocity
    right_speed = forward_velocity - rotation_velocity
    
    drivetrain.Drivetrain.set_drive_speed(left_speed, right_speed)