#!/usr/bin/env python

import serial,time,sys,struct
import rospy
from carrot_stm.msg import stm_carrot

Header=chr(0xFF)
i=1


ser = serial.Serial('/dev/ttyAMA0',115200,timeout=10)

def to_Byte(data):
    high = chr(int((data>>8)&0xFF))
    low = chr(int(data&0xFF))
    return high,low

def send_stm(flag,data):
    h,l=to_Byte(data)
    try:
        ser.write(Header+chr(flag)+h+l)
        #ser.write(chr(flag))
        #ser.write(h)
        #ser.write(l)
    except Exception as e:
        print(e)

def callback(data):
    send_stm(data.flag,data.data)

def stm():
    rospy.init_node('stm_serial', anonymous=True)
    rospy.Subscriber('stm',stm_carrot, callback)

    rospy.spin()

if __name__ == '__main__':
    stm()