#!/usr/bin/env python
import serial,time,sys,struct
import rospy
from sensor_msgs.msg import Joy

Header=chr(0xFF)
i=1

ser = serial.Serial('/dev/ttyAMA0',115200,timeout=10)
def to_Byte(data):
    high = chr(int((data>>8)&0xFF))
    low = chr(int(data&0xFF))
    return high,low

def callback(data):
    global i
    rospy.loginfo(data)
    h,l=to_Byte(0000)
    try:
        ser.write(Header)
        ser.write(chr(2))
        ser.write(h)
        ser.write(l)
    except Exception as e:
        print(e)
    time.sleep(0.1)
    i+=1
    if i>=0xFFFF:
        i=0

def main():
    global i
    rospy.init_node('serial_test', anonymous=True)
    rospy.Subscriber('joy', Joy, callback, queue_size=1)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        ser.close()
        sys.exit()

if __name__ == '__main__':
    main()
