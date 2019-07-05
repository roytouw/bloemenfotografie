class StepperMotorController:

    def __init__(self):
        self.height = 0

        self.qr_map = {
            -1: 0,
            1: 20000,
            2: 18000,
            3: 8000
        }

        self.width_map = {
            range(0, 200): 800,
            range(200, 400): 1200
        }

    def getHeightForQRCode(self, code):
        if int(code) in self.qr_map:
            move = self.qr_map[int(code)] - self.height
            self.height = self.qr_map[int(code)]
            return move
        else:
            raise Exception("qr_map doesn't contain requested key")

    def getHeightForWidth(self, width):
        for key in self.width_map:
            if int(width) in key:
                move = self.width_map[key] - self.height
                self.height = self.width_map[key]
                return move


if __name__ == "__main__":
    controller = StepperMotorController()
    height = controller.getHeightForQRCode(1)
    print(height)
    height = controller.getHeightForQRCode(2)
    print(height)
    height = controller.getHeightForQRCode(3)
    print(height)
    height = controller.getHeightForQRCode(1)
    print(height)
    height = controller.getHeightForQRCode(3)
    print(height)


# TODO this class should keep notice of height and move accordingly.
