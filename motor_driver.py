import RPi.GPIO as GPIO
import time

class MotorDriver:

    def __init__(self):
        self.sleep = 0.01
        self.out1 = 13
        self.out2 = 11
        self.out3 = 15
        self.out4 = 12


    def rotate(self, rotation):
