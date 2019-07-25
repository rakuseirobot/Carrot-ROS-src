#!/usr/bin/env python

import roslib; roslib.load_manifest('wiimote')
import rospy,math
from sensor_msgs.msg import JoyFeedbackArray
from sensor_msgs.msg import JoyFeedback
from carrot_stm.msg import stm_carrot

from wiimote.msg import State
siita=0
turn=0
sp=2
past=State()

enable = 0


def callback(data):
    global past,led0,led1,led2,led3,rum,turn,sp
    if not (data.linear_acceleration_zeroed == past.linear_acceleration_zeroed):
        x=data.linear_acceleration_zeroed.x/math.sqrt(pow((data.linear_acceleration_zeroed.x),2)+pow((data.linear_acceleration_zeroed.y),2))
        y=data.linear_acceleration_zeroed.y/math.sqrt(pow((data.linear_acceleration_zeroed.x),2)+pow((data.linear_acceleration_zeroed.y),2))
        turn=180+math.degrees(math.atan2(y,x))
        turn=int(turn)
        if turn > 45 and turn<180:
            turn=45
        elif turn < 315 and turn >180:
            turn = 315
        stm_msg.flag=3
        stm_msg.data=math.sin(math.radians(turn))*10000+10000
        stm_pub.publish(stm_msg)
    if(10>turn or turn>350):
        rum.intensity=1
    else:
        rum.intensity=0
    if data.buttons[1]==True and past.buttons[1]==False:
        #accel
        stm_msg.flag=1
        stm_msg.data=20000
        stm_pub.publish(stm_msg)
        stm_msg.flag=2
        stm_msg.data=10000
        stm_pub.publish(stm_msg)
        siita=0
        enable=1
    elif data.buttons[0]==True and past.buttons[0]==False:
        #Back
        stm_msg.flag=1
        stm_msg.data=0
        stm_pub.publish(stm_msg)
        stm_msg.flag=2
        stm_msg.data=10000
        stm_pub.publish(stm_msg)
        enable=1
        siita=180
    elif data.buttons[6]==True and past.buttons[6]==False:
        #Left
        stm_msg.flag=1
        stm_msg.data=10000
        stm_pub.publish(stm_msg)
        stm_msg.flag=2
        stm_msg.data=0
        stm_pub.publish(stm_msg)
        siita=270
        pass
    elif data.buttons[7]==True and past.buttons[7]==False:
        #Right
        stm_msg.flag=1
        stm_msg.data=10000
        stm_pub.publish(stm_msg)
        stm_msg.flag=2
        stm_msg.data=20000
        stm_pub.publish(stm_msg)
        siita=90
        pass
    elif data.buttons[2]==True and past.buttons[2]==False:
        if sp>=4:
            pass
        else:
            sp+=1
        msg.array[sp-1].intensity=1
        stm_msg.flag=5
        stm_msg.data=10000+2500*sp
        stm_pub.publish(stm_msg)
        #Speed Up
    elif data.buttons[3]==True and past.buttons[3]==False:
        if sp<=1:
            pass
        else:
            sp-=1
        msg.array[sp].intensity=0
        stm_msg.flag=5
        stm_msg.data=10000+2500*sp
        stm_pub.publish(stm_msg)
        #Speed down
    elif data.buttons[5]==True and past.buttons[5]==False:
        #Brake
        stm_msg.flag=4
        stm_msg.data=0b1000000000
        stm_pub.publish(stm_msg)
        enable=0
    elif data.buttons[5]==False and past.buttons[5]==True:
        #Left Brake
        stm_msg.flag=4
        stm_msg.data=0b0000000000
        stm_pub.publish(stm_msg)
        enable=1
    elif data.buttons[10]==True and past.buttons[10]==False:
        #Brake
        stm_msg.flag=4
        stm_msg.data=0b1000000000
        stm_pub.publish(stm_msg)
        enable=0
    elif data.buttons[10]==False and past.buttons[10]==True:
        #Left Brake
        stm_msg.flag=4
        stm_msg.data=0b0000000000
        stm_pub.publish(stm_msg)
        enable=1
    
    pub.publish(msg)
    print(turn)
    past=data


rospy.Subscriber('/wiimote/state', State, callback, queue_size=10)

pub = rospy.Publisher('/joy/set_feedback', JoyFeedbackArray, queue_size=10)
stm_pub = rospy.Publisher('/stm', stm_carrot, queue_size=1)
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

stm_msg = stm_carrot()

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
