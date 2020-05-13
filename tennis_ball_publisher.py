#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import time
import rospkg
import numpy as np
import sys

bridge = CvBridge()

def main(args):
    rospy.init_node('tennis_ball_publisher', anonymous=True)
    image_pub = rospy.Publisher("tennis_ball_image",Image, queue_size=10)
    
    print 'Press "Q" to stop publishing'
    global bridge
    video_capture = cv2.VideoCapture('video/tennis-ball-video.mp4')
    while(True):
        ret, frame = video_capture.read()
        ros_msg = bridge.cv2_to_imgmsg(frame, "bgr8")
        image_pub.publish(ros_msg)
        time.sleep(0.033)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        main(sys.argv)
    except rospy.ROSInterruptException:
        pass