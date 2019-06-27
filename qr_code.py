import pyqrcode
from PIL import Image
from pyzbar.pyzbar import decode
from steppermotor_controller import StepperMotorController
import re


class QR:

    def __init__(self):
        self.path = 'qr_codes/'
        self.scale = 20
        self.module_color = [0, 0, 0, 255]  # Black rgba
        self.background = [255, 255, 255, 255]  # White rgba

    # Generate new QR code and save.
    def generateQrCode(self, data, filename=''):
        qr = pyqrcode.create(data)
        if not filename:
            filename = str(data)

        qr.png(self.path + filename, self.scale, self.module_color, self.background)

    # Scan data from QR file.
    def scanQrCode(self, file):
        data = decode(Image.open(self.path + str(file)))
        return re.findall("\'(.*?)\'", str(data[0].data))[0]


if __name__ == "__main__":
    qr = QR()
    SMController = StepperMotorController()
    newNumber = 3
    qr.generateQrCode(newNumber)
    fustCode = qr.scanQrCode(newNumber)
    print(SMController.getHeightForQRCode(fustCode))

