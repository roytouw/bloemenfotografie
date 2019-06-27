class StepperMotorController:

    def __init__(self):
        self.qr_map = {
            1: 100,
            2: 120,
            3: 140
        }

        self.width_map = {
            range(0, 200): 100,
            range(200, 400): 120
        }

    def getHeightForQRCode(self, code):
        if int(code) in self.qr_map:
            return self.qr_map[int(code)]
        else:
            raise Exception("qr_map doesn't contain requested key")

    def getHeightForWidth(self, width):
        for key in self.width_map:
            if int(width) in key:
                return self.width_map[key]


if __name__ == "__main__":
    controller = StepperMotorController()
    height = controller.getHeightForWidth(205.5)
    print(height)
