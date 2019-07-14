from PIL import Image as img
import math

def crop_image(filename):
    # This function is called from the main.py and crops the image.
    # Once the image is cropped, it is saved to a file on the users
    # network.

    foto = img.open(filename)
    size = width, height = foto.size
    foto_stdr_save_location = 'standard_save_location/'     # Standard folder to save cropped image to if network folder is not set

    # crop with pillow tuple, (x1, y1, x2, y2)
    toppixel = -5                   # y1
    leftpixel = -5                  # x1
    rightpixel = -5                 # x2
    bottomrow = size[1]             # y2

    padding = 50                        # user config, in px
    thresholdValue = 5                  # user config, color must be atleast this % different
    fust_color = (229,204,176)          # user config, color of a fust in RGB
    color_differentiation = 0.01        # user config, as % color differentiation
    fust_edge_length = 10               # user config, length of detection for fust
    ratio = [4,3]                       # user config, image output ratio
    network_folder = ''                 # user config, save location for cropped images

    threshold = 255 * ( 1 - (thresholdValue / 100) )

    max_color = max(1, fust_color[0],fust_color[1], fust_color[2])
    color_relation = (fust_color[0]/max_color,fust_color[1]/max_color, fust_color[2]/max_color)
    fust_edge_counter = 0

    foto_rgb_list = list(foto.getdata())
    
    # find left, right and top pixels that are under the threshold value
    for i in range(len(foto_rgb_list)):
        y = math.floor(i / size[0])
        x = i - y * size[0]
        pixel = foto_rgb_list[i]
        for p in range(0,3):
            if pixel[p] <= threshold:
                if toppixel < 0:
                    toppixel = y
                if leftpixel < 0 or x < leftpixel:
                    leftpixel = x
                if rightpixel < 0 or x > rightpixel:
                    rightpixel = x
                break
        if bottomrow == size[1]:
            delta_max = max(1, pixel[0], pixel[1], pixel[2])
            delta_color = (pixel[0]/delta_max,pixel[1]/delta_max, pixel[2]/delta_max)
            count = 0
            for p in range(0,3):
                if delta_color[p] <= color_relation[p] + color_differentiation and delta_color[p] >=  color_relation[p] - color_differentiation:
                    count += 1
            if count == 3:
                fust_edge_counter += 1
            else:
                fust_edge_counter = 0
            if fust_edge_counter > fust_edge_length:
                bottomrow = y
        elif leftpixel >= 0 and rightpixel >= 0: # ignore inbetween space
            # i += rightpixel - leftpixel
            break
    
    # Adding padding for cropped image
    leftpixel -= padding
    rightpixel += padding
    toppixel -= padding
    bottomrow += padding
    
    # Add padding for ratio
    crop_width = rightpixel - leftpixel
    crop_height = bottomrow - toppixel
    
    crop_ratio = crop_width / crop_height
    user_ratio = ratio[0] / ratio[1]
    print('crop r', crop_ratio)
    print('user r', user_ratio)

    delta_ratio = crop_ratio - user_ratio
    
    if delta_ratio > 0:
        p = crop_height * delta_ratio
        print('delta r > 0, p = ',p)
        toppixel -= math.floor(p/2)
        bottomrow += math.ceil(p/2)
    elif delta_ratio < 0:
        p = crop_width * -delta_ratio
        print('delta r < 0, p = ',p)
        rightpixel += math.floor(p/2)
        leftpixel -= math.ceil(p/2)

    if leftpixel < 0:
        leftpixel = 0
    if rightpixel > size[0]-1 or rightpixel < 0:
        rightpixel = size[0]-1
    if toppixel < 0:
        toppixel = 0
    if bottomrow > size[1]:
        bottomrow = size[1]

    foto_cropped = foto.crop((leftpixel, toppixel, rightpixel, bottomrow))
    if not network_folder:
        foto_cropped.save(foto_stdr_save_location + filename)
    else:
        foto_cropped.save(network_folder + filename)