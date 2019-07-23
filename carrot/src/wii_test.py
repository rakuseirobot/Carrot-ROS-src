#!/usr/bin/env python

import roslib; roslib.load_manifest('wiimote')
import rospy,math
from sensor_msgs.msg import JoyFeedbackArray
from sensor_msgs.msg import JoyFeedback

from wiimote.msg import State

siita=444
sp=2
past=State()

def callback(data):
    global past,led0,led1,led2,led3,rum,siita,sp
    if not (data.linear_acceleration_zeroed == past.linear_acceleration_zeroed):
        x=data.linear_acceleration_zeroed.x/math.sqrt(pow((data.linear_acceleration_zeroed.x),2)+pow((data.linear_acceleration_zeroed.y),2))
        y=data.linear_acceleration_zeroed.y/math.sqrt(pow((data.linear_acceleration_zeroed.x),2)+pow((data.linear_acceleration_zeroed.y),2))
        siita=180+math.degrees(math.atan2(y,x))
        siita=int(siita)
    if(10>siita or siita>350):
        rum.intensity=1
    else:
        rum.intensity=0
    if data.buttons[1]==True and past.buttons[1]==False:
        #accel
        pass
    elif data.buttons[0]==True and past.buttons[0]==False:
        #Brake
        pass
    elif data.buttons[6]==True and past.buttons[6]==False:
        #Left
        pass
    elif data.buttons[7]==True and past.buttons[7]==False:
        #Right
        pass
    elif data.buttons[2]==True and past.buttons[2]==False:
        if sp>=4:
            pass
        else:
            sp+=1
        msg.array[sp-1].intensity=1
        #Speed Up
    elif data.buttons[3]==True and past.buttons[3]==False:
        if sp<=1:
            pass
        else:
            sp-=1
        msg.array[sp].intensity=0
        #Speed down
    elif data.buttons[5]==True and past.buttons[5]==False:
        #LED ON
        pass
    elif data.buttons[5]==False and past.buttons[5]==True:
        #LED OFF
        pass
    print(siita)
    pub.publish(msg)
    past=data


rospy.Subscriber('/wiimote/state', State, callback, queue_size=10)

pub = rospy.Publisher('/joy/set_feedback', JoyFeedbackArray, queue_size=10)
#stm = rospy.Publisher('/stm', stm_carrot, queue_size=1)
rospy.init_node('ledControlTester', anonymous=True)

led0 = JoyFeedback()
led0.type = JoyFeedback.TYPE_LED
led0.id = 0
led1 = JoyFeedback()
led1.type = JoyFeedback.TYPE_LED
led1.id = 1
led2 = JoyFeedback()
led2.type = JoyFeedback.TYPE_LED
led2.id = 2
led3 = JoyFeedback()
led3.type = JoyFeedback.TYPE_LED
led3.id = 3
rum = JoyFeedback()
rum.type = JoyFeedback.TYPE_RUMBLE
rum.id = 0

msg = JoyFeedbackArray()
msg.array = [led0, led1, led2, led3, rum]

led0.intensity=1
led1.intensity=1


if __name__ == '__main__':

    try:
        rospy.spin()
    except KeyboardInterrupt:
        ser.close()
        sys.exit()
