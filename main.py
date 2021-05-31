#!/usr/bin/python3

# Wouter van Velzen (19093861@student.hhs.nl)

import time
import pigpio

I2C_ADDR = 0x09


def i2c(pi, id = 0, tick = 0):

    s, b, d = pi.bsc_i2c(I2C_ADDR)
    if b:
        if d[0] == ord('t'):  # 116 send 'HH:MM:SS'
            print("sent = {} FR = {} received = {} [{}]".format(s >> 16, s & 0xFFF, b, d))
            s, b, d = pi.bsc_i2c(I2C_ADDR, "{}*".format(time.asctime()[11:19]))
            print("sent = {} FR = {} received = {} [{}]".format(s >> 16, s & 0xFFF, b, d))
        elif d[0] == ord('d'):
            print("sent = {} FR= {} received = {} [{}]".format(s >> 16, s & 0xFFF, b, d))
            s, b, d = pi.bsc_i2c(I2C_ADDR, "{}*".format(time.asctime()[:10]))
            print("sent = {} FR = {} received = {} [{}]".format(s >> 16, s & 0xFFF, b, d))


def main():
    print("Hi")
    pi = pigpio.pi()
    if not pi.connected:
        print("[ERROR] can't connect to PI GPIO.")
        exit()

    # Respond to BSC slave activity
    e = pi.event_callback(pigpio.EVENT_BSC, i2c(pi))
    pi.bsc_i2c(I2C_ADDR) # Configure BSC as I2C slave

    time.sleep(600)

    e.cancel()
    pi.bsc_i2c(0)
    pi.stop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
