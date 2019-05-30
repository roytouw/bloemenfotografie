from PIL import Image
from time import sleep
from queue import Queue
import datetime
# from picamera import PiCamera
from shutil import copyfile


class FustDetector:

    def __init__(self):
        self.border = 50
        self.img_height = 300
        self.img_width = 300
        self.x_offset = 3
        self.y_offset = 3
        self.snapshot_location = 'imgs/black.jpg'
        self.moving_average = 10
        self.detection_trigger = 30.05
        self.log_location = 'measurements.txt'
        # self.camera = PiCamera(resolution=(300, 300), framerate=30)
        # self.camera.iso = 100
        sleep(2)
        # self.camera.shutter_speed = camera.exposure_speed
        # self.camera.exposure_mode = 'off'
        # g = self.camera.awb_gains
        # self.camera.awb_mode = 'off'
        # self.camera_awb_gains = g

    def log(self, brightness, red, green, blue, moving_avg):
        with open(self.log_location, 'a') as log:
            d = datetime.datetime.now()
            log.write("%d:%d:%d,%f,%f,%f,%f,%f\n" % (d.hour, d.minute, d.second, brightness, red, green, blue, moving_avg))
            log.close()

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
        return (r + g + b) / 3, r, g, b

    def get_moving_average(self, values):
        sum = 0
        for i in values:
            sum += i
        return sum / self.moving_average

    def object_detection(self, moving_average, calibration_average):
        diff = abs(moving_average - calibration_average)
        if diff > self.detection_trigger:
            return True
        else:
            return False

    # Refresh the self.snapshot_location with a fresh snapshot.
    # Give true to save photos in /detection_photos/.
    def take_photo(self, save=False):
        sleep(0.25)
        # self.camera.capture(self.snapshot_location)
        if save:
            d = datetime.datetime.now()
            dest = "detection_photos/%d_%d_%d_%d_%d_%d.jpg" % (d.year, d.month, d.day, d.hour, d.minute, d.second)
            copyfile(self.snapshot_location, dest)

    def start_monitoring(self):
        q = Queue(self.moving_average)

        # Stack the queue with n values so the moving average can be calculated later.
        for i in range(self.moving_average):
            self.take_photo(True)
            photo_data = self.extract_brightness(self.snapshot_location)
            q.put(photo_data[0])

        cal_moving_average = self.get_moving_average(q.get_all())

        # Enter main loop, put each new snapshot's brightness in queue, calculate moving average,
        # detect if moving average is off enough to depict object is detected.
        while True:
            self.take_photo(True)
            photo_data = self.extract_brightness(self.snapshot_location)
            q.put(photo_data[0])
            moving_average = self.get_moving_average(q.get_all())
            print(moving_average)
            self.log(*photo_data, moving_average)
    #       TODO detect if moving average is off enough to depict object is detected.


if __name__ == "__main__":
    detector = FustDetector()
    detector.start_monitoring()
    # print(detector.extract_brightness('imgs/white.jpg'))
    # print(detector.extract_brightness('imgs/black.jpg'))
    # print(detector.extract_brightness('imgs/rainbow.jpg'))
    # print(detector.extract_brightness('imgs/fust1.png'))
    # print(detector.extract_brightness('imgs/fust2.jpg'))


