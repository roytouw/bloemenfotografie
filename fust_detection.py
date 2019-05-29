from PIL import Image
from time import sleep
from queue import Queue


class FustDetector:

    def __init__(self):
        self.border = 50
        self.img_height = 300
        self.img_width = 300
        self.x_offset = 3
        self.y_offset = 3
        self.snapshot_location = 'imgs/rainbow.jpg'
        self.moving_average = 5

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

    def get_moving_average(self, values):
        sum = 0
        for i in values:
            sum += i
        return sum / self.moving_average

    def start_monitoring(self):
        q = Queue(self.moving_average)

        # Stack the queue with n values so the moving average can be calculated later.
        for i in range(self.moving_average - 1):
            self.picamera_mock()
            q.put(self.extract_brightness(self.snapshot_location))

        # Enter main loop, put each new snapshot's brightness in queue, calculate moving average,
        # detect if moving average is off enough to depict object is detected.
        while True:
            self.picamera_mock()
            q.put(self.extract_brightness(self.snapshot_location))
            print(self.get_moving_average(q.get_all()))
    #       TODO detect if moving average is off enough to depict object is detected.

    # Refresh the self.snapshot_location with a fresh snapshot.
    def picamera_mock(self):
        sleep(1)
        return


if __name__ == "__main__":
    detector = FustDetector()
    detector.start_monitoring()
    print(detector.extract_brightness('imgs/white.jpg'))
    print(detector.extract_brightness('imgs/black.jpg'))
    print(detector.extract_brightness('imgs/rainbow.jpg'))
    print(detector.extract_brightness('imgs/fust1.png'))
    print(detector.extract_brightness('imgs/fust2.jpg'))


