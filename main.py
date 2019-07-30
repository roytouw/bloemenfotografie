import os
import datetime
import _thread
# from config_loader import ConfigLoader
# from fust_detection import FustDetector
# from qr_code import QR
# from fust_recognizer import FustRecognizer
# from steppermotor_controller import StepperMotorController
# from motor_driver import MotorDriver
from GUI import GUI
from crop_foto import crop_image
import sys
from PIL import Image

# configLoader = ConfigLoader()
# configLoader.load_configuration()
# fust_detector = FustDetector()
# qr = QR()
# fust_recognizer = FustRecognizer()
# steppermotor_controller = StepperMotorController()
# motor_driver = MotorDriver()
gui = GUI()

# print(sys.path)
# test_name = "fust_bloemen.png"
# img = Image.open(test_name)
# img = img.resize((800, 800), Image.ANTIALIAS)
# crop_image(test_name)
# # gui.setImage(img)


def on_detection(image):
    print('fust')
    # qr_data = qr.scanQrCode(image)
    # height = steppermotor_controller.getHeightForQRCode(qr_data)
    # motor_driver.rotate(height)
    name = str(datetime.datetime.now()).replace(" ", "")
    # command = "fswebcam -d /dev/video0 -r 1600x1200 --rotate 90 " + name +
    #  ".jpg" os.system(command)
    test_name = "fust_bloemen.png"
    # img = Image.open(name + ".jpg")
    img = Image.open(test_name)
    # crop_image(name + ".jpg")
    # crop_image(test_name)
    img = img.resize((800, 800), Image.ANTIALIAS)
    gui.setImage(img)



def lost_detection(image):
    print('nothing')
    # height = steppermotor_controller.getHeightForQRCode(-1)
    # motor_driver.rotate(height)


# fust_detector.setDetectionHook(on_detection).setNon_detectionHook(
# lost_detection).start_monitoring() _thread.start_new_thread(lambda:
# fust_detector.setDetectionHook(on_detection).setNon_detectionHook(
# lost_detection).start_monitoring(), ())
_thread.start_new_thread(gui.root.mainloop(), ())
