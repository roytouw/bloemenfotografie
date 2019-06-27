from PIL import Image, ImageDraw
from numpy import mean, median, mod


class FustRecognizer:

    def __init__(self):
        self.path = 'fust'
        self.background = (255, 255, 255)
        self.treshold = 300
        self.shade = 0
        self.vertical_crop = (100, 0)  # top and bottom
        self.measurement_band = (100, 300, 10) # Measurements made on vertical axis from, till, offset.

    def crop(self, image):
        input_pixels = image.load()

        width, height = image.width, image.height - (self.vertical_crop[0] + self.vertical_crop[1])

        output_image = Image.new("RGB", (width, height))
        draw = ImageDraw.Draw(output_image)

        for x in range(width):
            for y in range(self.vertical_crop[0], height):
                draw.point((x, y), input_pixels[x, y])

        return output_image

    # Turn pixels close enough to white black.
    def colorize(self, image):
        input_pixels = image.load()
        output_image = Image.new("RGB", image.size)
        draw = ImageDraw.Draw(output_image)

        for x in range(output_image.width):
            for y in range(output_image.height):
                r, g, b = input_pixels[x, y]
                if self.distance2(self.background, input_pixels[x, y]) < self.treshold:
                    r = int(r * self.shade)
                    g = int(g * self.shade)
                    b = int(b * self.shade)
                draw.point((x, y), (r, g, b))
        output_image.save("imgs/colorized.png")
        return output_image

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

    def getWidthOverRange(self, image):
        measurements = []
        for y in range(self.measurement_band[0], self.measurement_band[1], self.measurement_band[2]):
            measurements.append(self.getWidth(image, y))

        # print(mean(measurements))
        # print(median(measurements))
        return median(measurements)


if __name__ == "__main__":
    recognizer = FustRecognizer()
    input_image = Image.open('imgs/fust3.jpg')
    cropped_image = recognizer.crop(input_image)
    colorized_image = recognizer.colorize(cropped_image)
    # width = recognizer.getWidthOverRange(colorized_image, 100, 300, 10)
    # print(recognizer.distance2((255, 255, 255), (254, 254, 253)))
