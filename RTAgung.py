import cv2
import numpy as np


class RTAgung:
    def __init__(self, image):
        self.image = image

    def update_img(self, image):
        self.image = image

    def show_img(self, image=None):
        if image is None:
            image = self.image
        cv2.imshow('image effect', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def describe(self, image=None):
        if image is None:
            image = self.image
        print(image.shape)
        print(image[:2][:2])

    def to_grayscale(self, image=None):
        if image is None:
            image = self.image
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        return image

    def to_negative(self, image=None):
        if image is None:
            image = self.image
        image = cv2.bitwise_not(image)
        return image

    def brightening(self, value, image=None):
        if image is None:
            image = self.image
        image = image.astype('int16')
        image += value
        image = np.where(image > 255, 255,
                              np.where(image < 0, 0, image))
        image = image.astype('uint8')
        return image


file = "D:\\Photo\\1 Syawwal 1440H\\_MG_9252.JPG"

img = cv2.imread(file)
# img = np.ones((400, 400)) * 125
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, (400, 400), interpolation=cv2.INTER_CUBIC)

rta = RTAgung(img)
