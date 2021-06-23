#!/usr/bin/python3

# Wouter van Velzen (19093861@student.hhs.nl)
import numpy as np

from i2c import I2C
from markers import Video
import cv2 as cv
import time

# import pigpio

I2C_ADDR = 0x09


def main():
    print("Hi")
    # i2ctmp = I2C(0x09)

    video = Video(False)

    while True:
        markers_found = video.detect_markers()
        if markers_found is not None:
            for i in range(markers_found.shape[ 0 ]):
                print("[INFO]: Marker {:d} Found at [{:d},{:d}]".format(markers_found[ i, 0 ], markers_found[ i, 1 ],
                                                                        markers_found[ i, 2 ]))
        else:
            print("[INFO]: No markers found")

        print("\n")

        cv.imshow("Feed", video.frame)
        if cv.waitKey(1) == 27:
            break  # esc to quit

    cv.destroyAllWindows()

    # time.sleep(600)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
