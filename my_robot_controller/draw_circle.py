#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircleNode(Node):

    def __init__(self):
        super().__init__("draw_circle")
        self.get_logger().info("Draw circle node has been started")
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.__i = 0

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 2.5
        msg.angular.z = 1.0
          
        self.cmd_vel_pub_.publish(msg)
        self.get_logger().info(f"Publishing: {msg}")
        self.__i += 1



def main(args=None):
    rclpy.init(args=args)

    circle_node = DrawCircleNode()
    rclpy.spin(circle_node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()