from RTAgung import RTAgung
import cv2
import numpy as np

class Zahra:
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

    def tresholding(self, th=128, image=None):
        if image is None:
            image = self.image
        #convert ke grayscale
        img_gray = RTAgung(image).to_grayscale()
        #fungsi tresholding
        th, img_gray_th = cv2.threshold(img_gray, th, 255, cv2.THRESH_OTSU)
        return(img_gray_th)

    def mirroring(self, key, image=None):
        if image is None:
            image = self.image
        img_flip = cv2.flip(image,key) 
        return(img_flip)

    def sharpening(self, image=None):
        if image is None:
            image = self.image
        kernel = np.array([[0, -1, 0],
                           [-1, 5,-1],
                           [0, -1, 0]])
        img_sharp = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
        return(img_sharp)

file = "ndr.JPG"

img = cv2.imread(file)
img = cv2.resize(img, (400, 400), interpolation=cv2.INTER_CUBIC)

zahra = Zahra(img)

#tresholding
img = zahra.tresholding(th=190)
zahra.show_img(img)

#mirroring
key = 1     # key: 1->cermin ke kiri; 0->cermin ke atas; -1->cermin ke kiri & atas
img = zahra.mirroring(key)
zahra.show_img(img)

#sharpening
img = zahra.sharpening()
zahra.show_img(img)