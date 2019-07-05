import RPi.GPIO as GPIO
import time


class MotorDriver:

    def __init__(self):
        self.sleep_initial = 0.0024
        self.sleep_final = 0.0020
        self.out1 = 12
        self.out2 = 11
        self.out3 = 13
        self.out4 = 15
        self.sleep = 0.0024
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.out1, GPIO.OUT)
        GPIO.setup(self.out2, GPIO.OUT)
        GPIO.setup(self.out3, GPIO.OUT)
        GPIO.setup(self.out4, GPIO.OUT)

    # Destructor, cleanup.
    def __del__(self):
        GPIO.cleanup()

    def rotate(self, rotation):
        print(rotation)
        if rotation > 0 and rotation < 40000:
            i = 0
            for y in range(rotation, 0, -1):
                if i == 0:
                    self.pos0()
                elif i == 1:
                    self.pos1()
                elif i == 2:
                    self.pos2()
                elif i == 3:
                    self.pos3()
                elif i == 4:
                    self.pos4()
                elif i == 5:
                    self.pos5()
                elif i == 6:
                    self.pos6()
                elif i == 7:
                    self.pos7()
                else:
                    i = 0
                    continue
                time.sleep(self.test(y, rotation))
                i += 1

        elif rotation > -40000 and rotation < 0:
            i = 7
            for y in range(rotation, 0, 1):
                if i == 0:
                    self.pos0()
                elif i == 1:
                    self.pos1()
                elif i == 2:
                    self.pos2()
                elif i == 3:
                    self.pos3()
                elif i == 4:
                    self.pos4()
                elif i == 5:
                    self.pos5()
                elif i == 6:
                    self.pos6()
                elif i == 7:
                    self.pos7()
                else:
                    i = 7
                    continue
                time.sleep(self.test(-y, -rotation))
                i -= 1

    def test(self, y, rotation):
        coefficient = 0.0000018
        limit = 400
        if rotation < limit * 2:
            return self.sleep_initial
        elif y <= limit:
            return self.sleep_initial - y * coefficient
        elif y >= limit and (rotation - y) >= limit:
            return self.sleep_initial - limit * coefficient
        elif (rotation -y) <= limit:
            return self.sleep_initial - (rotation - y) * coefficient
            
    def pos0(self):
        GPIO.output(self.out1, GPIO.HIGH)
        GPIO.output(self.out2, GPIO.LOW)
        GPIO.output(self.out3, GPIO.LOW)
        GPIO.output(self.out4, GPIO.LOW)
#        time.sleep(self.sleep)

    def pos1(self):
        GPIO.output(self.out1, GPIO.HIGH)
        GPIO.output(self.out2, GPIO.HIGH)
        GPIO.output(self.out3, GPIO.LOW)
        GPIO.output(self.out4, GPIO.LOW)
#        time.sleep(self.sleep)

    def pos2(self):
        GPIO.output(self.out1, GPIO.LOW)
        GPIO.output(self.out2, GPIO.HIGH)
        GPIO.output(self.out3, GPIO.LOW)
        GPIO.output(self.out4, GPIO.LOW)
#        time.sleep(self.sleep)

    def pos3(self):
        GPIO.output(self.out1, GPIO.LOW)
        GPIO.output(self.out2, GPIO.HIGH)
        GPIO.output(self.out3, GPIO.HIGH)
        GPIO.output(self.out4, GPIO.LOW)
#        time.sleep(self.sleep)

    def pos4(self):
        GPIO.output(self.out1, GPIO.LOW)
        GPIO.output(self.out2, GPIO.LOW)
        GPIO.output(self.out3, GPIO.HIGH)
        GPIO.output(self.out4, GPIO.LOW)
#        time.sleep(self.sleep)

    def pos5(self):
        GPIO.output(self.out1, GPIO.LOW)
        GPIO.output(self.out2, GPIO.LOW)
        GPIO.output(self.out3, GPIO.HIGH)
        GPIO.output(self.out4, GPIO.HIGH)
#        time.sleep(self.sleep)

    def pos6(self):
        GPIO.output(self.out1, GPIO.LOW)
        GPIO.output(self.out2, GPIO.LOW)
        GPIO.output(self.out3, GPIO.LOW)
        GPIO.output(self.out4, GPIO.HIGH)
#        time.sleep(self.sleep)

    def pos7(self):
        GPIO.output(self.out1, GPIO.HIGH)
        GPIO.output(self.out2, GPIO.LOW)
        GPIO.output(self.out3, GPIO.LOW)
        GPIO.output(self.out4, GPIO.HIGH)
#        time.sleep(self.sleep)


if __name__ == "__main__":
    driver = MotorDriver()
    driver.rotate(-9000)
#    driver.rotate(9000)
#    print(driver.test(0, 100))
#    print(driver.test(90, 100))
#    print(driver.test(300, 10000))
#    print(driver.test(400, 10000))
#    print(driver.test(800, 10000))
#    print(driver.test(9999, 10000))
