#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase


# colorSensor = ColorSensor(4)
def init_motor():

    # asign the global variable "driveMotor1" to the port A
    driveMotor1 = Motor(Port.A)
    # asign the global variable "driveMotor2" to the port D
    driveMotor2 = Motor(Port.D)

    return driveMotor1, driveMotor2


# publicies driveMotor1 and driveMotor2 so that other functions can use those varialbes
driveMotor1, driveMotor2 = init_motor()


def startUp():
    print("Hello from ev3 dev!")  # prints out message to output tab
    brick.sound.beep()  # plays beep on ev3 brick
    brick.display.text("Running Program...")  # displays text on ev3 brick


def tankMove(speed, degm1, degm2):
    '''
    speed: speed of both motors (max: 1000)
    rotm1: # of degrees motor1 must turn (if positive, then clockwise, if negative, then counterclockwise)
    rotm2: # of degrees motor2 must turn (if positive, then clockwise, if negative, then counterclockwise)
    '''

    init_motor()

    driveMotor1.run_target(speed, degm1, Stop.BRAKE,
                           False)  # run_angle(speed, rotation_angle, stop_type=Stop.COAST, wait=True)
    driveMotor2.run_target(speed, degm2, Stop.BRAKE)
    print("tankMove executed")


def tankMoveRot(speed, rotm1, rotm2):
    '''
    motor1: port to initialize (e.g. Motor(Port.A))
    motor2: another port to initialize (e.g. Motor(Port.B))
    speed: speed of both motors (max: 1000)
    rotm1: # of rotations motor1 must turn (if positive, then clockwise, if negative, then counterclockwise)
    rotm2: # of rotations motor2 must turn (if positive, then clockwise, if negative, then counterclockwise)
    '''

    init_motor()

    driveMotor1.run_target(speed, (rotm1*360), Stop.BRAKE,
                           False)  # run_angle(speed, rotation_angle, stop_type=Stop.COAST, wait=True)
    driveMotor2.run_target(speed, (rotm2*360), Stop.BRAKE)


startUp()

tankMoveRot(500, 10, 10)
