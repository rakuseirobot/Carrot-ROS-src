#!/usr/bin/env python
import serial,time,sys,struct,threading
import rospy
from carrot_stm.msg import stm_carrot
from geometry_msgs.msg import Twist

def send_stm(flag,data):
    stm_msg.flag=flag
    stm_msg.data=data
    stm_pub.publish(stm_msg)

def callback(data):
    global past
    if not past == None:
        if not data.linear.x==past.linear.x:
            send_stm(2,int(data.linear.x*10000+10000))
        if not data.linear.y==past.linear.y:
            send_stm(1,int(data.linear.y*(-10000)+10000))
        if not data.angular.z==past.angular.z:
            send_stm(3,int(data.angular.z*0.7*(-10000)+10000))
    else:
        pass
    past=data
    

def main():
    rospy.init_node('carrot', anonymous=True)
    rospy.Subscriber('/my_robo/diff_drive_controller/cmd_vel', Twist, callback, queue_size=10)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        sys.exit()


stm_pub = rospy.Publisher('/stm', stm_carrot, queue_size=10)
stm_msg = stm_carrot()
past=None


if __name__ == '__main__':
    main()
