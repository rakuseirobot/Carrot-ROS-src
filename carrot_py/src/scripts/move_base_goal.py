#!/usr/bin/env python
import serial,time,sys,struct
import rospy
from actionlib_msgs.msg import GoalStatusArray
from move_base_msgs.msg import MoveBaseActionGoal

i=255
"""

    
"""
def callback(data):
    global i
    pub=rospy.Publisher("move_base/goal",MoveBaseActionGoal,queue_size=5)
    position=MoveBaseActionGoal()
    position.goal.target_pose.header.frame_id="base_link"
    position.goal.target_pose.pose.position.x=0
    position.goal.target_pose.pose.position.y=0
    position.goal.target_pose.pose.orientation.w=0
    if not i==data.status_list[0].status:
        if data.status_list[0].status==3 or data.status_list[0].status==0:
            print("GoalReached")
            position.header.stamp = rospy.Time.now()
            position.goal.target_pose.header.stamp = rospy.Time.now()
            pub.publish(position)
        else:
            print("moving...")
        i=data.status_list[0].status
    else:
        return
def wait():
    rospy.init_node('goal_notify', anonymous=True)
    rospy.Subscriber('move_base/status',GoalStatusArray, callback)
    rospy.spin()

if __name__ == '__main__':
    wait()