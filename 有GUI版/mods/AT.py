#!/usr/bin/python
# -*- coding: UTF-8 -*-

import serial
import time
import colorama

flag = 1
ser = 0

try:
    ser = serial.Serial("/dev/ttyUSB2", 115200, timeout=0.1)
except:
    try:
        print("無法連接 正在嘗試更換port")
        ser = serial.Serial("/dev/ttyUSB3", 115200, timeout=0.1)
    except:
        print("沒有可用的COM 請確認硬體狀態")
        flag = 0
    else:
        print("串列阜連接成功 COM3")
else:
    print("串列阜連接成功 COM2")


def GPS():
    # print("1")
    if flag:
        # print("2")
        ser.write("AT+CGPSINFO\r".encode())  # display GPS information
        # print("3")
        temp = ser.readlines()[1].decode("UTF-8")
        if temp.find("CGPSINFO") != -1:  # find "CGPSINFO" in GPS information
            # print("Success getData: ",temp) DEBUG
            return temp  # array[1] is the information that we want
        else:
            print("GPS Fail")
            time.sleep(1.5)
            GPS()
    else:
        print("沒有GPS設備,回傳預設座標")
        return "+CGPSINFO:2245.200007,N,12022.475822,E,150418,104221.0,87.6,0.0,46.6"


def so():
    return "+CGPSINFO:2245.200007,N,12022.475822,E,150418,104221.0,87.6,0.0,46.6"
