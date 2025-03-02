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
i2c = busio.I2C(SCL, SDA)
# Create a simple PCA9685 class instance for the Motor FeatherWing's default address.
pca = PCA9685(i2c, address=0x60)
pca1 = PCA9685(i2c, address=0x60)
pca.frequency = 1600
pca1.frequency = 1600
# Motor 1 is channels 9 and 10 with 8 held high.
# Motor 2 is channels 11 and 12 with 13 held high.
# Motor 3 is channels 3 and 4 with 2 held high.
# Motor 4 is channels 5 and 6 with 7 held high.

pca1.channels[8].duty_cycle = 0xFFFF
pca1.channels[13].duty_cycle = 0xFFFF

pca.channels[7].duty_cycle = 0xFFFF

pca.channels[2].duty_cycle = 0xFFFF

stepper_motor_EL = stepper.StepperMotor(
    pca.channels[4], pca.channels[3], pca.channels[5], pca.channels[6]
)

stepper_motor_AZ = stepper.StepperMotor(
    pca.channels[9], pca.channels[10], pca.channels[11], pca.channels[12],
)

for i in range(100):

    stepper_motor_EL.onestep()
    stepper_motor_AZ.onestep()

    time.sleep(0.01)


for i in range(100):

    stepper_motor_EL.onestep(direction=stepper.BACKWARD)
    stepper_motor_AZ.onestep(direction=stepper.BACKWARD)

    time.sleep(0.01)


#for j in range(20):
#	for i in range(100):
#		stepper_motor_EL.onestep()

pca.deinit()
