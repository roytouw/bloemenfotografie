import os
import datetime
from config_loader import ConfigLoader
from fust_detection import FustDetector
from qr_code import QR
from fust_recognizer import FustRecognizer
from steppermotor_controller import StepperMotorController
from motor_driver import MotorDriver
from GUI import GUI


configLoader = ConfigLoader()
configLoader.load_configuration()
fust_detector = FustDetector()
qr = QR()
fust_recognizer = FustRecognizer()
steppermotor_controller = StepperMotorController()
motor_driver = MotorDriver()
gui = GUI()


def onDetection(image):
    print('fust')
    qr_data = qr.scanQrCode(image)
    height = steppermotor_controller.getHeightForQRCode(qr_data)
    motor_driver.rotate(height)
    name = str(datetime.datetime.now()).replace(" ", "")
    command = "fswebcam -d /dev/video0 -r 1600x1200 " + name + ".jpg"
    os.system(command)


def lostDetection(image):
    print('nothing')
    height = steppermotor_controller.getHeightForQRCode(-1)
    motor_driver.rotate(height)


fust_detector.setDetectionHook(onDetection).setNonDetectionHook(lostDetection).start_monitoring()

