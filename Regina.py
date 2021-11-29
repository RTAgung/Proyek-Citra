import cv2
import numpy as np

class Regina:
    def __init__(self, image):
        self.image = image

    def menu(self, number, number2):
        if number == 0:
            new_image = self.sketching()
        elif number == 1:
            new_image = self.bluring(number2)
        elif number == 2:
            new_image = self.equalizationing()
        self.show_img(new_image)

    def show_img(self, imagenew):
        cv2.imshow('image effect', imagenew)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def describe(self):
        print(self.image.shape)

    def sketching(self):
        grey_img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        invert_img = cv2.bitwise_not(grey_img)
        blur_img = cv2.GaussianBlur(invert_img, (21, 21), 0)
        inverted_blur_img = cv2.bitwise_not(blur_img)
        sketch_img = cv2.divide(grey_img, inverted_blur_img, scale=256.0)
        return sketch_img

    def bluring(self, number):
        if number == 0:
            blur_img = cv2.GaussianBlur(self.image, (5, 5), 0)
        elif number == 1:
            blur_img = cv2.blur(self.image, (5, 5))
        elif number == 2:
            blur_img = cv2.medianBlur(self.image, 5)
        elif number == 3:
            blur_img = cv2.bilateralFilter(self.image, 9, 75, 75)
        return blur_img

    def equalizationing(self):
        # convert it to grayscale
        img_yuv = cv2.cvtColor(self.image, cv2.COLOR_BGR2YUV)
        # apply histogram equalization
        img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
        hist_eq = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
        return hist_eq


def resizing(image):
    scale_percent = 70
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (height, width)
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return resized

file = 'play.png'
img = cv2.imread(file)
re_img = resizing(img)
regina = Regina(re_img)

regina.describe()
regina.show_img(re_img)

regina.menu(0,0)
regina.menu(1,0)
regina.menu(2,0)