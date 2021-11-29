import cv2
import numpy as np


class RTAgung:
    def __init__(self, image):
        self.image = image

    def update_img(self, image):
        self.image = image

    def show_img(self):
        cv2.imshow('image effect', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def describe(self):
        print(self.image.shape)
        print(self.image[:2][:2])

    def to_grayscale(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)

    def to_negative(self):
        self.image = cv2.bitwise_not(self.image)

    def brightening(self, value):
        self.image = self.image.astype('int16')
        self.image += value
        self.image = np.where(self.image > 255, 255,
                              np.where(self.image < 0, 0, self.image))
        self.image = self.image.astype('uint8')




file = "D:\\Photo\\1 Syawwal 1440H\\_MG_9252.JPG"

img = cv2.imread(file)
# img = np.ones((400, 400)) * 125
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, (400, 400), interpolation=cv2.INTER_CUBIC)

rta = RTAgung(img)

rta.describe()
rta.show_img()

rta.brightening(100)
rta.describe()
rta.show_img()



