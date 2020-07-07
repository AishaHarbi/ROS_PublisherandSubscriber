#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
    
def talker():
    rospy.init_node('talker')
    rate = rospy.Rate(1) # this defines the publish rate
    pub = rospy.Publisher('chatter', String, queue_size=10)    
    hello_str = "hello world %s" % rospy.get_time()
    while not rospy.is_shutdown(): 
        # put everything in a while loop to keep publishiing topic
        pub.publish(hello_str)
        rospy.loginfo(hello_str)
        rate.sleep() # this make sure that the topic is publishing at 1 Hz
   
if __name__ == '__main__':
     try:
          talker()
     except rospy.ROSInterruptException:
          pass
