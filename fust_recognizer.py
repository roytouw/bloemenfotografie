from PIL import Image, ImageDraw
from numpy import mean, median, mod


class FustRecognizer:

    def __init__(self):
        self.path = 'fust'
        self.background = (255, 255, 255)
        self.treshold = 300
        self.shade = 0

    # def loadImage(self):
    #     fust_image = Image.open('imgs/fust_alfa.jpg')
    #     draw = ImageDraw.Draw(fust_image)

    # Turn pixels close enough to white black.
    def colorize(self):
        input_image = Image.open('imgs/fust3.jpg')
        input_pixels = input_image.load()

        output_image = Image.new("RGB", input_image.size)
        draw = ImageDraw.Draw(output_image)

        for x in range(output_image.width):
            for y in range(output_image.height):
                r, g, b = input_pixels[x, y]
                if self.distance2(self.background, input_pixels[x, y]) < self.treshold:
                    r = int(r * self.shade)
                    g = int(g * self.shade)
                    b = int(b * self.shade)
                draw.point((x, y), (r, g, b))
        return output_image
        # output_image.save("imgs/colorized.png")

    def distance2(self, color1, color2):
        r1, g1, b1 = color1
        r2, g2, b2 = color2
        return (r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2

    def getWidth(self, image, height):
        test = image.load()
        left, right = 0, 0
        for x in range(image.width):
            if test[x, height] != (0, 0, 0):  # If not black
                left = x
                break

        for x in range(image.width - 1, 0, -1):  # Loop from right to left.
            if test[x, height] != (0, 0, 0):  # If not black
                right = x
                break

        width = right - left
        return width

    def getWidthOverRange(self, image, botom, top, offset):
        measurements = []
        for y in range(botom, top, offset):
            measurements.append(self.getWidth(image, y))

        print(mean(measurements))
        print(median(measurements))


if __name__ == "__main__":
    recognizer = FustRecognizer()
    colorized_image = recognizer.colorize()
    recognizer.getWidthOverRange(colorized_image, 100, 300, 10)
    # print(recognizer.distance2((255, 255, 255), (254, 254, 253)))
