#!usr/bin/env python
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class PoseSubscriberNode(Node):

    def __init__(self):
        super().__init__("pose_subscriber")
        self.get_logger().info("Pose subscriber has started")
        self.subscription = self.create_subscription(
            Pose, 
            "/turtle1/pose", 
            self.pose_subscriber_callback,
            10)
        self.__counter = 0

    def pose_subscriber_callback(self, msg: Pose):
        self.__counter +=1
        if self.__counter > 50:
            self.__counter = 0
            self.get_logger().info(f"\nTurtle position is: {str(msg.x)} {str(msg.y)}")

def main(args=None):
    rclpy.init(args=args)

    aNode = PoseSubscriberNode()
    rclpy.spin(aNode)

    rclpy.shutdown()