#!/usr/bin/env python  
import rospy

from std_msgs.msg import Int16
from project1_solution.msg import TwoInts

def two_ints_callback(data, my_pub):
    int_a = data.a
    int_b = data.b

    sum_ints = data.a + data.b

    rospy.loginfo(rospy.get_caller_id() + "the two ints are %d and %d, and their sum is: %d", int_a, int_b, sum_ints)

    # publish sum of two ints to the publisher
    my_pub.publish(sum_ints)


def two_sum():
    pass
   


if __name__ == "__main__":
     # initialize node
    rospy.init_node('two_sum_publisher',anonymous=True)
    
    # declare publisher object from publisher class, topicName, msgType, queue sizee
    my_pub = rospy.Publisher('sum', Int16, queue_size=10)

    # subscribe to two_ints
    rospy.Subscriber('two_ints', TwoInts, two_ints_callback, my_pub)

    rospy.spin()

   