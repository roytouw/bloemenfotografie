class StepperMotorController:

    def __init__(self):
        self.qr_map = {
            1: 100,
            2: 120,
            3: 140
        }

    def getHeightForQRCode(self, code):
        if int(code) in self.qr_map:
            return self.qr_map[int(code)]
        else:
            raise Exception("qr_map doesn't contain requested key")
