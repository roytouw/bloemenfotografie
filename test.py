import utils
from edge_detection import cannyEdgeDetector
imgs = utils.load_data('edge_detection_imgs')
utils.visualize(imgs, 'gray')
detector = cannyEdgeDetector(imgs, sigma=1.4, kernel_size=10, lowthreshold=0.09, highthreshold=0.17, weak_pixel=100)
imgs_final = detector.detect()
utils.visualize(imgs_final, 'gray')
