#!/usr/bin/env python
import serial,time,sys,struct
import rospy
from carrot_stm.msg import stm_carrot

def callback(data):
    print(data)

def stm():
    rospy.init_node('stm_serial', anonymous=True)
    rospy.Subscriber('stm',stm_carrot, callback)

    rospy.spin()

if __name__ == '__main__':
    stm()