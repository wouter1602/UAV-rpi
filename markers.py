#!/usr/bin/python3

import cv2 as cv
import numpy as np


class Video:
    def __init__(self, useTestImg=False):
        self._aruco_dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_250)  # type of tags used

        self._useTestImg = useTestImg
        if self._useTestImg:
            self._cap = cv.imread("./Test_img.jpg")
            self.frame = cv.imread("./Test_img.jpg")
        else:
            self._cap = cv.VideoCapture(0)
            self._cap.set(cv.CAP_PROP_FRAME_WIDTH, 1080)
            self._cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
            _, self.frame = self._cap.read()

    def _get_video(self) -> np.ndarray:
        if self._useTestImg:
            return self.frame
        else:
            _, self.frame = self._cap.read()
            return self.frame

    @staticmethod
    def _convert_to_grayscale(frame: np.ndarray) -> np.ndarray:
        grayscale = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        return grayscale

    def detect_markers(self):
        frame = self._get_video()
        grayscale = self._convert_to_grayscale(frame)
        corners, ids, rejected = cv.aruco.detectMarkers(frame, self._aruco_dictionary)
