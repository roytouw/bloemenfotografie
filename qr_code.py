import pyqrcode


class QR:

    def __init__(self):
        self.path = 'qr_codes/'
        self.scale = 20
        self.module_color = [0, 0, 0, 255] # Black rgba
        self.background = [255, 255, 255, 255] # White rgba

    def generateQrCode(self, data, filename=''):
        qr = pyqrcode.create(data)
        if not filename:
            filename = str(data)

        qr.png(self.path + filename, self.scale, self.module_color, self.background)


if __name__ == "__main__":
    qr = QR()
    qr.generateQrCode('test')

