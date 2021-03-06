import cv2
import imutils


class RGBHist:
    def __init__(self, bins):
        self.bins = bins

    def describe(self, image):
        hist = cv2.calcHist([image], [0, 1, 2], None, self.bins, [0, 256, 0, 256, 0, 256])
        # Для улучшения качества анализа - выравнивание гистограмм
        if imutils.is_cv2():
            hist = cv2.normalize(hist)
        else:
            hist = cv2.normalize(hist, hist)
        return hist.flatten()
