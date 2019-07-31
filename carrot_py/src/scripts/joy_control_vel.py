#!/usr/bin/env python
import serial,time,sys,struct,threading
import rospy
from sensor_msgs.msg import Joy
from carrot_stm.msg import stm_carrot

def send_stm(flag,data):
    stm_msg.flag=flag
    stm_msg.data=data
    stm_pub.publish(stm_msg)

def callback(data):
    global past
    if not past==None:
        if  (past.axes[0] != data.axes[0]):
            send_stm(3,int((data.axes[0]*-1)*10000+10000))
        elif  (past.axes[2] != data.axes[2]):
            send_stm(1,int((data.axes[2]*-1)*10000+10000))
            if (data.axes[3]==0):                
                send_stm(2,int(data.axes[3]*10000+10000))
        elif (past.axes[3] != data.axes[3]):
            send_stm(2,int(data.axes[3]*10000+10000))
            if (data.axes[2]==0):
                send_stm(1,int((data.axes[2]*-1)*10000+10000))
        elif (past.buttons[6] != data.buttons[6]) or (past.buttons[7] != data.buttons[7]):
            if (data.buttons[6]==1) or (data.buttons[7]==1):
                send_stm(4,0b1000000000)
            else:
                send_stm(4,0)
    else:
        pass
    past=data

def main():
    global i
    rospy.init_node('carrot', anonymous=True)
    rospy.Subscriber('joy', Joy, callback, queue_size=10)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        ser.close()
        sys.exit()


stm_pub = rospy.Publisher('/stm', stm_carrot, queue_size=1)
stm_msg = stm_carrot()
past=None


if __name__ == '__main__':
    main()
