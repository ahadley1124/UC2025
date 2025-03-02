# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
# This example uses an Adafruit Stepper and DC Motor FeatherWing to run a Stepper Motor.
#   https://www.adafruit.com/product/2927
import time
from board import SCL, SDA
import busio
# Import the PCA9685 module. Available in the bundle and here:
#   https://github.com/adafruit/Adafruit_CircuitPython_PCA9685
from adafruit_pca9685 import PCA9685
from adafruit_motor import stepper
#board init
i2c = busio.I2C(SCL, SDA)
# Create a simple PCA9685 class instance for the Motor FeatherWing's default address.
pca = PCA9685(i2c, address=0x60)
pca.frequency = 1600
# Motor 1 is channels 9 and 10 with 8 held high.
# Motor 2 is channels 11 and 12 with 13 held high.
# Motor 3 is channels 3 and 4 with 2 held high.
# Motor 4 is channels 5 and 6 with 7 held high.

pca.channels[7].duty_cycle = 0xFFFF
pca.channels[2].duty_cycle = 0xFFFF

#creating the stepper motor objects
stepper_motor_EL = stepper.StepperMotor(
    pca.channels[4], pca.channels[3], pca.channels[5], pca.channels[6]
)

stepper_motor_AZ = stepper.StepperMotor(
    pca.channels[9], pca.channels[10], pca.channels[11], pca.channels[12],
)

#Globals
horizontal = 360
vertical = 360


#util functions
def degrees_to_steps(degree):
    step = degree/1.8
    return int(step)


def step_AZ(steps, reverse=False):
    for step in range(steps):
        if reverse == True:
            stepper_motor_AZ.onestep(direction=stepper.BACKWARD)
        else:
            stepper_motor_AZ.onestep()
            time.sleep(0.01)
        
def step_EL(steps, reverse=False):
    for step in range(steps):
        if reverse == True:
            stepper_motor_EL.onestep(direction=stepper.BACKWARD)
        else:
            stepper_motor_EL.onestep()
            time.sleep(0.01)

#test to make sure it can rotate properly
def calibration():
    AZ_Steps = degrees_to_steps(horizontal)
    EL_Steps = degrees_to_steps(vertical)
    step_AZ(AZ_Steps)
    step_EL(EL_Steps)
        
def inputLocation():
    curr_az = 0
    curr_el = 0

    input_az = input("Enter the Heading for the anteanna to face: ")
    input_el = input("Input the elevation to face the antenna above the horizon: ")
    
    AZ_Steps = degrees_to_steps(float(input_az))
    EL_Steps = degrees_to_steps(float(input_el))
    
    #check for max rotation
    if AZ_Steps + curr_az <= 200:
        step_AZ(AZ_Steps)
    else:
        step_it = -200 + AZ_Steps
        curr_az = curr_az - step_it
        step_AZ(step_it, reverse=True)

    if curr_az - AZ_Steps <= -200:
        step_AZ(AZ_Steps)
    else:
        step_it = 200 - AZ_Steps
        curr_az = curr_az + step_it
        step_AZ(step_it, reverse=True)
    
    #do the same for EL for it to work

#for i in range(100):
#    stepper_motor_EL.onestep()
#    stepper_motor_AZ.onestep()
#    time.sleep(0.01)
#
#for i in range(100):
#    stepper_motor_EL.onestep(direction=stepper.BACKWARD)
#    stepper_motor_AZ.onestep(direction=stepper.BACKWARD)
#    time.sleep(0.01)
#
#for j in range(20):
#	for i in range(100):
#		stepper_motor_EL.onestep()

if __name__ == '__main__':
    calibration()
    inputLocation()
    
    
    pca.deinit()
