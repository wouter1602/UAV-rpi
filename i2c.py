#!/usr/bin/python3

import pigpio
import time


class I2C:
    def __init__(self, address):
        self._pi_address = address
        self._pi = pigpio.pi()
        if not self._pi.connected:
            print("[ERROR] can't connect to PI GPIO.")
            exit()

        self._e = self._pi.event_callback(pigpio.EVENT_BSC, self.read_i2c)
        self._pi.bsc_i2c(self._pi_address)

    def read_i2c(self, id, ticks):
        s, b, d = self._pi.bsc_i2c(self._pi_address)

        if b:
            if d[0] == ord('t'):  # 116 send 'HH:MM:SS'
                print("sent = {} FR = {} received = {} [{}]".format(s >> 16, s & 0xFFF, b, d))
                s, b, d = self._pi.bsc_i2c(self._pi_address, "{}*".format(time.asctime()[11:19]))
                print("sent = {} FR = {} received = {} [{}]".format(s >> 16, s & 0xFFF, b, d))
            elif d[0] == ord('d'):
                print("sent = {} FR= {} received = {} [{}]".format(s >> 16, s & 0xFFF, b, d))
                s, b, d = self._pi.bsc_i2c(self._pi_address, "{}*".format(time.asctime()[:10]))
                print("sent = {} FR = {} received = {} [{}]".format(s >> 16, s & 0xFFF, b, d))
            elif d[0] == ord('D'):
                print("sent = {} FR= {} received = {} [{}]".format(s >> 16, s & 0xFFF, b, d))
                for i in d:
                    if i == ord('\t'):
                        print("Tab found")

    def convert_to_ints(self, bytes: bytearray):
        print("L")

    def __del__(self):
        self._e.cancel()
        self._pi.bsc_i2c(0)
        self._pi.stop()
