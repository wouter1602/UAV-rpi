#!/usr/bin/python3

# Wouter van Velzen (19093861@student.hhs.nl)

# GPIO 18 (Pin 12) SDA
# GPIO 19 (Pin 35) SCL

from typing import Tuple, List
import numpy as np

from markers import Video
from i2c import I2C

I2C_ADDR = 0x09


def convert_16_to_8(value: int) -> Tuple[int, int]:
    high_byte = ((value >> 8) & 0xFF)
    low_byte = (value & 0xFF)
    return high_byte, low_byte


def create_array(video: Video, i2c: I2C) -> List:
    # markers_array = np.zeros((2*5), dtype=np.uint8)
    # markers_array[0] = 5
    # tmp = convert_16_to_8(np.uint16(0xFF05))
    # markers_array[1] = tmp[0]
    # markers_array[2] = tmp[1]
    # tmp = convert_16_to_8(np.uint16(0x0086))
    # markers_array[3] = tmp[0]
    # markers_array[4] = tmp[1]
    #
    # markers_array[5] = 6
    # tmp = convert_16_to_8(np.uint16(0xFE8F))
    # markers_array[6] = tmp[0]
    # markers_array[7] = tmp[1]
    # tmp = convert_16_to_8(np.uint16(0XA38C))
    # markers_array[8] = tmp[0]
    # markers_array[9] = tmp[1]
    # return markers_array
    markers_array = [5]
    tmp = convert_16_to_8(np.uint16(0xFF05))
    markers_array.append(int(tmp[0]))
    markers_array.append(int(tmp[1]))
    tmp = convert_16_to_8(np.uint16(0x0086))
    markers_array.append(int(tmp[0]))
    markers_array.append(int(tmp[1]))

    markers_array.append(6)
    tmp = convert_16_to_8(np.uint16(0xFE8F))
    markers_array.append(int(tmp[0]))
    markers_array.append(int(tmp[1]))
    tmp = convert_16_to_8(np.uint16(0xA38C))
    markers_array.append(int(tmp[0]))
    markers_array.append(int(tmp[1]))

    tmp_2 = bytearray(markers_array)
    return tmp_2


def main():
    print("Hi")
    i2ctmp = I2C(0x09)

    video = Video(False)

    i2ctmp.data_array = create_array(video, i2ctmp)

    while True:
        markers_found = video.detect_markers()
        if markers_found is not None:
            for i in range(markers_found.shape[0]):
                print("[INFO]: Marker {:d} Found at [{:d},{:d}]".format(markers_found[i, 0], markers_found[i, 1],
                                                                        markers_found[i, 2]))
        # else:
        #     print("[INFO]: No markers found")

        # print("\n")



        # cv.imshow("Feed", video.frame)
        # if cv.waitKey(1) == 27:
        #     break  # esc to quit
    #
    # cv.destroyAllWindows()

    # time.sleep(600)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
