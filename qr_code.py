import pyqrcode
from PIL import Image
from pyzbar.pyzbar import decode


class QR:

    def __init__(self):
        self.path = 'qr_codes/'
        self.scale = 20
        self.module_color = [0, 0, 0, 255]  # Black rgba
        self.background = [255, 255, 255, 255]  # White rgba
        # self.qr = qrtools.QR()

    def generateQrCode(self, data, filename=''):
        qr = pyqrcode.create(data)
        if not filename:
            filename = str(data)

        qr.png(self.path + filename, self.scale, self.module_color, self.background)

    def scanQrCode(self, file):
        test = decode(Image.open('qr_codes/picture.jpeg'))
        return test[0].data


if __name__ == "__main__":
    qr = QR()
    qr.generateQrCode(123)
    data = qr.scanQrCode('123')

