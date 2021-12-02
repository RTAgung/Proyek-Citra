import cv2
import numpy as np


class RTA_Func:
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

    def edge_detection(self, image=None):
        if image is None:
            image = self.image
        kernel = np.array([[-1, -1, -1],
                           [-1, 8, -1],
                           [-1, -1, -1]])
        image = self.to_grayscale(image)
        image = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
        return image


# file = "ndr.JPG"
# img = cv2.imread(file)
# img = cv2.resize(img, (400, 400), interpolation=cv2.INTER_CUBIC)
#
# rta = RTAgung(img)
#
# # to_grayscale
# rta.show_img(rta.to_grayscale())
#
# # to_negative
# rta.show_img(rta.to_negative())
#
# # brightening
# rta.show_img(rta.brightening(100))
#
# # edge_detection
# rta.show_img(rta.edge_detection())
