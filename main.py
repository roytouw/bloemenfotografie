from fust_detection import FustDetector
from qr_code import QR
from fust_recognizer import FustRecognizer
from steppermotor_controller import StepperMotorController


fust_detector = FustDetector()
qr = QR()
fust_recognizer = FustRecognizer()
steppermotor_controller = StepperMotorController()


def onDetection(image):
    qr_data = qr.scanQrCode(image)
    fust_width = fust_recognizer.getWidthOverRange(image)
    qr_height = steppermotor_controller.getHeightForQRCode(qr_data)
    detected_height = steppermotor_controller.getHeightForWidth(fust_width)
#   TODO move stepper motor and take the proper photo.


fust_detector.setHook(onDetection).start_monitoring()
