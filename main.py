import os
import datetime
import _thread
from config_loader import ConfigLoader
from fust_detection import FustDetector
from qr_code import QR
from fust_recognizer import FustRecognizer
from steppermotor_controller import StepperMotorController
from motor_driver import MotorDriver
from GUI import GUI
from PIL import Image


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
    img = Image.open(name + ".jpg")
    img = img.resize((300, 300), Image.ANTIALIAS)
    gui.setImage(img)


def lostDetection(image):
    print('nothing')
    height = steppermotor_controller.getHeightForQRCode(-1)
    motor_driver.rotate(height)


# fust_detector.setDetectionHook(onDetection).setNonDetectionHook(lostDetection).start_monitoring()
_thread.start_new_thread(lambda: fust_detector.setDetectionHook(onDetection).setNonDetectionHook(lostDetection).start_monitoring(), ())
_thread.start_new_thread(gui.root.mainloop(), ())
