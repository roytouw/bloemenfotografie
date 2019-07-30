from PIL import Image as img
import json
from math import floor


class FustRecognizerAlt:
    def __init__(self):
        with open('config.json', 'r') as crop_config:
            self.data = json.load(crop_config)
        self.color_difference_threshold = self.data['crop_config']['color_differentiation']


    def identify(self, filename):
        fust_img = img.open(filename)
        foto_rgb_list = list(fust_img.getdata())
        start_index = floor(len(foto_rgb_list) / 1.5)
        for i in foto_rgb_list[start_index:]:
            pixel = pixel = foto_rgb_list[i]
            delta_max = max(1, pixel[0], pixel[1], pixel[2])
            delta_color = (pixel[0] / delta_max, pixel[1] / delta_max, pixel[2] / delta_max)
            # TODO find way to know how far you need to count, also height
            # might be useful inorder to find the starting point
