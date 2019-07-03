from config_loader import ConfigLoader
from fust_detection import FustDetector
from qr_code import QR
from fust_recognizer import FustRecognizer
from steppermotor_controller import StepperMotorController
from motor_driver import MotorDriver


configLoader = ConfigLoader()
configLoader.load_configuration()
fust_detector = FustDetector()
qr = QR()
fust_recognizer = FustRecognizer()
steppermotor_controller = StepperMotorController()
motor_driver = MotorDriver()


def onDetection(image):
    print('fust')
#    qr_data = qr.scanQrCode(image)
#    fust_width = fust_recognizer.getWidthOverRange(image)
#    qr_height = steppermotor_controller.getHeightForQRCode(qr_data)
#    detected_height = steppermotor_controller.getHeightForWidth(fust_width)
    height = steppermotor_controller.getHeightForQRCode(3)
    motor_driver.rotate(height)

#   TODO move stepper motor and take the proper photo.


def lostDetection(image):
    print('nothing')
    height = steppermotor_controller.getHeightForQRCode(1)
    motor_driver.rotate(height)


fust_detector.setDetectionHook(onDetection).setNonDetectionHook(lostDetection).start_monitoring()

