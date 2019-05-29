from PIL import Image


class FustDetector:

    def __init__(self):
        self.border = 50
        self.img_height = 300
        self.img_width = 300
        self.x_offset = 3
        self.y_offset = 3

    def extract_brightness(self, image):
        r, g, b = 0, 0, 0
        im = Image.open(image)
        im = im.resize((self.img_width, self.img_height))
        pix = im.load()
        for i in range(0, self.img_width,  self.x_offset):
            for j in range(0, self.img_height, self.y_offset):
                r += pix[i, j][0]
                g += pix[i, j][1]
                b += pix[i, j][2]
        x_pixelcount = self.img_width / self.x_offset
        y_pixelcount = self.img_height / self.y_offset
        pixelcount = x_pixelcount * y_pixelcount
        r, g, b = r / pixelcount, g / pixelcount, b / pixelcount
        return (r + g + b) / 3


if __name__ == "__main__":
    detector = FustDetector()
    print(detector.extract_brightness('imgs/white.jpg'))
    print(detector.extract_brightness('imgs/black.jpg'))
    print(detector.extract_brightness('imgs/rainbow.jpg'))
