#!/usr/bin/env python

import rospy
import actionlib
import tf,sys,time
from nav_msgs.msg import Odometry
import math
from actionlib_msgs.msg import GoalStatusArray
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

waypoints = [
[(-3.99365329742,-1.11783218384,0.0),(0.0,0.0,0.975302602582,-0.220872889683)],
[(-0.185990214348,-0.141303062439,0.0),(0.0,0.0,0.0464989492019,0.998918338866)]
]


i=255
ss = False

def goal_pose(pose): 
    goal_pose = MoveBaseGoal()
    goal_pose.target_pose.header.frame_id = 'map'
    goal_pose.target_pose.pose.position.x = pose[0][0]
    goal_pose.target_pose.pose.position.y = pose[0][1]
    goal_pose.target_pose.pose.position.z = pose[0][2]
    goal_pose.target_pose.pose.orientation.x = pose[1][0]
    goal_pose.target_pose.pose.orientation.y = pose[1][1]
    goal_pose.target_pose.pose.orientation.z = pose[1][2]
    goal_pose.target_pose.pose.orientation.w = pose[1][3]

    return goal_pose


if __name__ == '__main__':
    rospy.init_node('patrol')
    listener = tf.TransformListener()

    client = actionlib.SimpleActionClient('move_base', MoveBaseAction) 
    client.wait_for_server()
    try:
        while True:
            for pose in waypoints: 
                goal = goal_pose(pose)
                client.send_goal(goal)
                try:
                    client.wait_for_result()
                except KeyboardInterrupt:
                    sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(0)